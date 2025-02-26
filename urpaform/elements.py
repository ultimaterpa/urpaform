"""Classes for elements that can be used in urpaform module."""

from collections import Counter
from typing import Tuple

import urpa


class _FormElement:
    """A private class representing a common element in a form."""

    def __init__(self, element: urpa.AppElement, show_in_log: bool = True, allow_check: bool = True) -> None:
        """Initiates instances of the _EditElem class.

        Args:
            element: urpa.AppElement
                Editbox maintained by the class.
            show_in_log: bool
                A flag used to log the values.
            allow_check: bool
                A flag used to check the value after being filled in a form.
        """
        self.element = element
        self.show_in_log = show_in_log
        self.allow_check = allow_check

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} with element {self.element}."

    def __str__(self) -> str:
        return self.__repr__()


class EditElement(_FormElement):
    """A class used to represent a common Editbox in a form."""

    _VALUE_IS_IN = ("value", "name", "text_value")
    _SEND_METHOD_IS_IN = ("writing", "pasting", "setting")
    _CLEAR_METHOD_IS_IN = ("keys", "set_empty_string", "no_clearing")

    def __init__(
        self,
        element: urpa.AppElement,
        show_in_log: bool = True,
        allow_check: bool = True,
        value_is_in: str = "value",
        clear_method: str = "keys",
        clear_keys: Tuple[str, str] = ("CTRL+A", "DEL"),
        default_value: str = "",
        send_method: str = "writing",
        paste_keys: str = "CTRL+V",
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
            clear_method: str
                Method to used for clearing the Element
            clear_keys: Tuple[str, str]
                Keys used to clear the editbox.
            default_value: str
                A string of default value that cannot be removed from the editbox. For example,
                predefined dots for a date.
            send_method: str
                A string to specify the method of sending the value. Default value writing. Overwrite for pasting.
            paste_keys: str
                Keys used to paste into the editbox. Default CTRL+V. Overwrite for other shortcut.
        """
        if value_is_in not in self._VALUE_IS_IN:
            raise ValueError(f"Value in argument value_is_in must be from: '{self._VALUE_IS_IN}'!")
        self.value_is_in = value_is_in
        if clear_method not in self._CLEAR_METHOD_IS_IN:
            raise ValueError(f"Value in argument clear method must be from: '{self._CLEAR_METHOD_IS_IN}'")
        self.clear_method = clear_method
        self.clear_keys = clear_keys
        self.default_value = default_value
        send_method = send_method.lower()
        if send_method not in self._SEND_METHOD_IS_IN:
            raise ValueError(f"Value in argument send_method must be from: '{self._SEND_METHOD_IS_IN}'!")
        self.send_method = send_method
        self.paste_keys = paste_keys
        super().__init__(element, show_in_log, allow_check)

    @property
    def value(self) -> str:
        """Getter for value."""
        if self.value_is_in == "value":
            return self.element.value()
        if self.value_is_in == "name":
            return self.element.name()
        if self.value_is_in == "text_value":
            return self.element.text_value()[:-1]
        return ""

    @value.setter
    def value(self, value: str) -> None:
        """Setter for value."""
        self.element.set_focus()
        if self.value != value:
            if self.value != self.default_value:
                self._clear()
            if self.send_method == "writing":
                self.element.send_text(value)
            elif self.send_method == "pasting":
                urpa.set_clipboard_text(value)
                self.element.send_key(self.paste_keys)
            elif self.send_method == "setting":
                self.element.set_value(value)

    def _clear(self) -> None:
        """Clears the editbox."""
        self.element.set_focus()
        if self.clear_method == "keys":
            for key in self.clear_keys:
                self.element.send_key(key)
        elif self.clear_method == "set_empty_string":
            self.element.set_value("")
        elif self.clear_method == "no_clearing":
            pass


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
        """
        self.clear_keys = clear_keys
        send_method = send_method.lower()
        if send_method not in self._SEND_METHOD_IS_IN:
            raise ValueError(f"Value in argument send_method must be from: '{self._SEND_METHOD_IS_IN}'!")
        self.send_method = send_method
        self.paste_keys = paste_keys
        super().__init__(element, show_in_log, allow_check=False)

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
            self.element.send_text(value)
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
        self, element: urpa.AppElement, show_in_log: bool = True, allow_check: bool = True, walk_type: bool = False
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
        """
        self.walk_type = walk_type
        super().__init__(element, show_in_log, allow_check)

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
            self.element.send_text(value)

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
