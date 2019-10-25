"""Classes for elements that can be used in urpaform module."""

from collections import Counter

import urpa


class _FormElement:
    """A private class representing a common element in a form."""

    def __init__(self, element, show_in_log=True, allow_check=True):
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

    def __repr__(self):
        return f"{self.__class__.__name__} with element {self.element}."

    def __str__(self):
        return self.__repr__()


class EditElement(_FormElement):
    """A class used to represent a common Editbox in a form."""

    _VALUE_IS_IN = ("value", "name", "text_value")

    def __init__(
        self,
        element,
        show_in_log=True,
        allow_check=True,
        value_is_in="value",
        clear_keys=("CTRL+A", "DEL"),
        default_value="",
        clipboard=False,
        paste_keys="ALT+E+V"
    ):
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
                clear_keys: tuple
                    Keys used to clear the editbox.
                default_value: str
                    A string of default value that cannot be removed from the editbox. For example,
                    predefined dots for a date.
                clipboard: bool
                    A flag used to switch from send_text to use of clipboard and send_key for pasting.
                paste_keys: str
                    Keys used to paste into the editbox. Default ALT+E+V. Overwrite for CTRL+V or other shortcut.
        """
        if value_is_in not in self._VALUE_IS_IN:
            raise ValueError(f"Value in argument value_is_in must be from: '{self._VALUE_IS_IN}'!")
        self.value_is_in = value_is_in
        self.clear_keys = clear_keys
        self.default_value = default_value
        self.clipboard = clipboard
        self.paste_keys = paste_keys
        super().__init__(element, show_in_log, allow_check)

    @property
    def value(self):
        """Getter for value."""
        if self.value_is_in == "value":
            return self.element.value()
        if self.value_is_in == "name":
            return self.element.name()
        if self.value_is_in == "text_value":
            return self.element.text_value().rstrip("\n")

    @value.setter
    def value(self, value):
        """Setter for value."""
        self.element.set_focus()
        if self.value != value:
            if self.value != self.default_value:
                self._clear()
            if self.clipboard:
                urpa.set_clipboard_text(value)
                self.element.send_key(self.paste_keys)
            else:
                self.element.send_text(value)

    def _clear(self):
        """Clears the editbox."""
        self.element.set_focus()
        for key in self.clear_keys:
            self.element.send_key(key)


class PasswordElement(_FormElement):
    """A class used to represent a Passwordbox in a form."""

    def __init__(self, element, show_in_log=False, clear_keys=("CTRL+A", "DEL"), clipboard=False, paste_keys="ALT+E+V"):
        """Iniciates instances of the PasswordElement class.

            Args:
                element: urpa.AppElement
                    Editbox for password maintained by the class.
                show_in_log: bool
                    A flag used to log the values.
                clear_keys: tuple
                    Keys used to clear the editbox.
                clipboard: bool
                    A flag used to switch from send_text to use of clipboard and send_key for pasting.
                paste_keys: str
                    Keys used to paste into the editbox. Default ALT+E+V. Overwrite for CTRL+V or other shortcut.
        """
        self.clear_keys = clear_keys
        self.clipboard = clipboard
        self.paste_keys = paste_keys
        super().__init__(element, show_in_log, allow_check=False)

    @property
    def value(self):
        """Getter for value."""
        return ""

    @value.setter
    def value(self, value):
        """Setter for value."""
        self.element.set_focus()
        self._clear()
        if self.clipboard:
            urpa.set_clipboard_text(value)
            self.element.send_key(self.paste_keys)
        else:
            self.element.send_text(value)

    def _clear(self):
        """Clears the editbox."""
        self.element.set_focus()
        for key in self.clear_keys:
            self.element.send_key(key)


class CheckElement(_FormElement):
    """A class used to represent a Checkbox in a form."""

    @property
    def value(self):
        """Getter for value."""
        return self.element.toggle_state()

    @value.setter
    def value(self, value):
        """Setter for value."""
        if not isinstance(value, bool):
            raise TypeError("Only True or False value is allowed for CheckBox!")
        self.element.set_focus()
        if self.value != value:
            self.element.send_mouse_click()


class RadioElement(_FormElement):
    """A class used to represent a Radio button in a form."""

    @property
    def value(self):
        """Getter for value."""
        return self.element.selected()

    @value.setter
    def value(self, value):
        """Setter for value."""
        if not value is True:
            raise TypeError("Only True value is allowed for RadioButton!")
        self.element.set_focus()
        if self.value != value:
            self.element.send_mouse_click()


class ComboElement(_FormElement):
    """A class used to represent a Combobox in a form."""

    _WALK_SETTER_MAX_COUNT = 3

    def __init__(self, element, show_in_log=True, allow_check=True, walk_type=False):
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
    def value(self):
        """Getter for value."""
        return self.element.value()

    @value.setter
    def value(self, value):
        """Setter for value."""
        if self.walk_type:
            self._walk_setter(value)
        else:
            self._default_setter(value)

    def _default_setter(self, value):
        """Default setter for value."""
        self.element.set_focus()
        if self.value != value:
            self.element.send_text(value)

    def _walk_setter(self, value):
        """Setter for value in a Combobox, where the send_text method
        cannot be used to set the value up.
        """
        walk_setter_counter = Counter()
        self.element.set_focus()
        self.element.send_key("HOME")
        while self.value != value:
            walk_setter_counter.update([self.value])
            if walk_setter_counter.get(self.value, 0) >= self._WALK_SETTER_MAX_COUNT:
                raise ValueError(f"Value: '{value}' cannot be set up in combo box!")
            self.element.send_key("DOWN")
