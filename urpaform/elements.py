"""Classes for elements that can be used in urpaform module."""

from collections import Counter
from typing import Tuple

import urpa
from .constants import ALL_KEYBOARD_IDENTIFIERS


DEFAULT_KEYBOARD = "00000409"
DEFAULT_TEXT_ACTION = "wm_char"


class _FormElement:
    """A private class representing a common element in a form."""

    _TEXT_ACTIONS = {
        "wm_char": "WM_CHAR",
        "hw_alt_code": "HW_Alt_code",
        "hw_scan_virtual": "HW_Scan_Virtual",
        "standard_alt_code": "Standard_Alt_code",
        "standard_scan_virtual": "Standard_Scan_Virtual",
    }

    def __init__(
        self,
        element: urpa.AppElement,
        show_in_log: bool = True,
        allow_check: bool = True,
        text_action: str = DEFAULT_TEXT_ACTION,
        keyboard: str = DEFAULT_KEYBOARD,
    ) -> None:
        """Initiates instances of the _EditElem class.

        Args:
            element: urpa.AppElement
                Editbox maintained by the class.
            show_in_log: bool
                A flag used to log the values.
            allow_check: bool
                A flag used to check the value after being filled in a form.
            text_action: str
                A flag used to set implicit type of writing text, by default is 'wm_char', other options are
                'hw_alt_code', 'hw_scan_virtual', 'standard_alt_code', 'standard_scan_virtual'
            keyboard: str
                A flag used to set the keyboard layout, by default is '00000409' - United States English,
                for other options see ALL_KEYBOARD_IDENTIFIERS in constants.py
        """
        self.element = element
        self.show_in_log = show_in_log
        self.allow_check = allow_check
        if text_action not in self._TEXT_ACTIONS.keys():
            raise ValueError(f"Value in argument text_action must be from: '{self._TEXT_ACTIONS.keys()}'!")
        self.text_action = self._TEXT_ACTIONS[text_action]
        if keyboard.lower() not in ALL_KEYBOARD_IDENTIFIERS:
            raise ValueError(f"Value in argument keyboard must be from: '{ALL_KEYBOARD_IDENTIFIERS}'!")
        if keyboard != "00000409" and "scan_virtual" not in text_action:
            raise ValueError(f"Argument 'keyboard' is available only for argument 'text_action=*_scan_virtual'!")
        self.keyboard = keyboard

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} with element {self.element}."

    def __str__(self) -> str:
        return self.__repr__()


class EditElement(_FormElement):
    """A class used to represent a common Editbox in a form."""

    _VALUE_IS_IN = ("value", "name", "text_value")
    _SEND_METHOD_IS_IN = ("writing", "pasting")

    def __init__(
        self,
        element: urpa.AppElement,
        show_in_log: bool = True,
        allow_check: bool = True,
        value_is_in: str = "value",
        clear_keys: Tuple[str, str] = ("CTRL+A", "DEL"),
        default_value: str = "",
        send_method: str = "writing",
        paste_keys: str = "CTRL+V",
        text_action: str = DEFAULT_TEXT_ACTION,
        keyboard: str = DEFAULT_KEYBOARD,
    ) -> None:
        """Initiates instances of the EditElement class.

        Args:
            element: urpa.AppElement
                Editbox maintained by the class.
            show_in_log: bool
                A flag used to log the values.
            allow_check: bool
                A flag used to check the value after being filled in a form.
            value_is_in: str
                Set the properties where the value is filled.
            clear_keys: Tuple[str, str]
                Keys used to clear the editbox.
            default_value: str
                A string of default value that cannot be removed from the editbox. For example,
                predefined dots for a date.
            send_method: str
                A string to specify the method of sending the value. Default value writing. Overwrite for pasting.
            paste_keys: str
                Keys used to paste into the editbox. Default CTRL+V. Overwrite for other shortcut.
            text_action: str
                A flag used to set implicit type of writing text, by default is 'wm_char', other options are
                'hw_alt_code', 'hw_scan_virtual', 'standard_alt_code', 'standard_scan_virtual'
            keyboard: str
                A flag used to set the keyboard layout, by default is '00000409' - United States English,
                for other options see ALL_KEYBOARD_IDENTIFIERS in constants.py
        """
        if value_is_in not in self._VALUE_IS_IN:
            raise ValueError(f"Value in argument value_is_in must be from: '{self._VALUE_IS_IN}'!")
        self.value_is_in = value_is_in
        self.clear_keys = clear_keys
        self.default_value = default_value
        send_method = send_method.lower()
        if send_method not in self._SEND_METHOD_IS_IN:
            raise ValueError(f"Value in argument send_method must be from: '{self._SEND_METHOD_IS_IN}'!")
        self.send_method = send_method
        self.paste_keys = paste_keys
        super().__init__(element, show_in_log, allow_check, text_action=text_action, keyboard=keyboard)

    @property
    def value(self) -> str:
        """Getter for value."""
        if self.value_is_in == "value":
            return self.element.value()
        if self.value_is_in == "name":
            return self.element.name()
        if self.value_is_in == "text_value":
            return self.element.text_value().rstrip("\n")
        return ""

    @value.setter
    def value(self, value: str) -> None:
        """Setter for value."""
        self.element.set_focus()
        if self.value != value:
            if self.value != self.default_value:
                self._clear()
            if self.send_method == "writing":
                self.element.send_text(value, action=self.text_action, kl=self.keyboard)
            elif self.send_method == "pasting":
                urpa.set_clipboard_text(value)
                self.element.send_key(self.paste_keys)

    def _clear(self) -> None:
        """Clears the editbox."""
        self.element.set_focus()
        for key in self.clear_keys:
            self.element.send_key(key)


class PasswordElement(_FormElement):
    """A class used to represent a Passwordbox in a form."""

    _SEND_METHOD_IS_IN = ("writing", "pasting")

    def __init__(
        self,
        element: urpa.AppElement,
        show_in_log: bool = False,
        clear_keys: Tuple[str, str] = ("CTRL+A", "DEL"),
        send_method: str = "writing",
        paste_keys: str = "CTRL+V",
        text_action: str = DEFAULT_TEXT_ACTION,
        keyboard: str = DEFAULT_KEYBOARD,
    ) -> None:
        """Iniciates instances of the PasswordElement class.

        Args:
            element: urpa.AppElement
                Editbox for password maintained by the class.
            show_in_log: bool
                A flag used to log the values.
            clear_keys: Tuple[str, str]
                Keys used to clear the editbox.
            send_method: str
                A string to specify the method of sending the value. Default value writing. Overwrite for pasting.
            paste_keys: str
                Keys used to paste into the editbox. Default CTRL+V. Overwrite for other shortcut.
            text_action: str
                A flag used to set implicit type of writing text, by default is 'wm_char', other options are
                'hw_alt_code', 'hw_scan_virtual', 'standard_alt_code', 'standard_scan_virtual'
            keyboard: str
                A flag used to set the keyboard layout, by default is '00000409' - United States English,
                for other options see ALL_KEYBOARD_IDENTIFIERS in constants.py
        """
        self.clear_keys = clear_keys
        send_method = send_method.lower()
        if send_method not in self._SEND_METHOD_IS_IN:
            raise ValueError(f"Value in argument send_method must be from: '{self._SEND_METHOD_IS_IN}'!")
        self.send_method = send_method
        self.paste_keys = paste_keys
        super().__init__(element, show_in_log, allow_check=False, text_action=text_action, keyboard=keyboard)

    @property
    def value(self) -> str:
        """Getter for value."""
        return ""

    @value.setter
    def value(self, value: str) -> None:
        """Setter for value."""
        self.element.set_focus()
        self._clear()
        if self.send_method == "writing":
            self.element.send_text(value, action=self.text_action, kl=self.keyboard)
        elif self.send_method == "pasting":
            urpa.set_clipboard_text(value)
            self.element.send_key(self.paste_keys)

    def _clear(self) -> None:
        """Clears the editbox."""
        self.element.set_focus()
        for key in self.clear_keys:
            self.element.send_key(key)


class CheckElement(_FormElement):
    """A class used to represent a Checkbox in a form."""

    @property
    def value(self) -> bool:
        """Getter for value."""
        return self.element.toggle_state()

    @value.setter
    def value(self, value: bool) -> None:
        """Setter for value."""
        if not isinstance(value, bool):
            raise TypeError("Only True or False value is allowed for CheckBox!")
        self.element.set_focus()
        if self.value != value:
            self.element.send_mouse_click()


class RadioElement(_FormElement):
    """A class used to represent a Radio button in a form."""

    @property
    def value(self) -> bool:
        """Getter for value."""
        return self.element.selected()

    @value.setter
    def value(self, value: bool) -> None:
        """Setter for value."""
        if not value is True:
            raise TypeError("Only True value is allowed for RadioButton!")
        self.element.set_focus()
        if self.value != value:
            self.element.send_mouse_click()


class ComboElement(_FormElement):
    """A class used to represent a Combobox in a form."""

    _WALK_SETTER_MAX_COUNT = 3

    def __init__(
        self,
        element: urpa.AppElement,
        show_in_log: bool = True,
        allow_check: bool = True,
        walk_type: bool = False,
        text_action: str = DEFAULT_TEXT_ACTION,
        keyboard: str = DEFAULT_KEYBOARD,
    ):
        """Initiates instances of the Combobox class.

        Args:
            element: urpa.AppElement
                Editbox maintained by the class.
            show_in_log: bool
                A flag used to log the values.
            allow_check: bool
                A flag used to check the value after being filled in a form.
            walk_type: bool
                A flag used to determine the method for setting the value up.
            text_action: str
                A flag used to set implicit type of writing text, by default is 'wm_char', other options are
                'hw_alt_code', 'hw_scan_virtual', 'standard_alt_code', 'standard_scan_virtual'
            keyboard: str
                A flag used to set the keyboard layout, by default is '00000409' - United States English,
                for other options see ALL_KEYBOARD_IDENTIFIERS in constants.py
        """
        self.walk_type = walk_type
        super().__init__(element, show_in_log, allow_check, text_action=text_action, keyboard=keyboard)

    @property
    def value(self) -> str:
        """Getter for value."""
        return self.element.value()

    @value.setter
    def value(self, value: str) -> None:
        """Setter for value."""
        if self.walk_type:
            self._walk_setter(value)
        else:
            self._default_setter(value)

    def _default_setter(self, value: str) -> None:
        """Default setter for value."""
        self.element.set_focus()
        if self.value != value:
            self.element.send_text(value, action=self.text_action, kl=self.keyboard)

    def _walk_setter(self, value: str) -> None:
        """Setter for value in a Combobox, where the send_text method
        cannot be used to set the value up.
        """
        walk_setter_counter: Counter = Counter()
        self.element.set_focus()
        self.element.send_key("HOME")
        while self.value != value:
            walk_setter_counter.update([self.value])
            if walk_setter_counter.get(self.value, 0) >= self._WALK_SETTER_MAX_COUNT:
                raise ValueError(f"Value: '{value}' cannot be set up in combo box!")
            self.element.send_key("DOWN")
