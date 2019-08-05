"""Třídy elementů které lze použít v upraform."""

# Třídy reprezentující obecný prvek formuláře.


class _FormElement:
    """Třída reprezentuje obecný prvek formuláře a nelze použít v urpaform."""

    def __init__(self, element, show_in_log=True, allow_check=True):
        """Inicializace instance třídy _EditElem.

            Args:
                element: urpa.AppElement
                    Editbox který třída obsluhuje.
                show_in_log: bool
                    Vlajka jestli je možné hodnotu zapsat do logu.
                allow_check: bool
                    Vlajka jestli se má hodnota po vyplnění kontrolovat.
        """
        self.element = element
        self.show_in_log = show_in_log
        self.allow_check = allow_check

    def __repr__(self):
        return f"{self.__class__.__name__} with element {self.element}."

    def __str__(self):
        return self.__repr__()


class EditElement(_FormElement):
    """Třída reprezentující obecný editbox formuláře."""

    def __init__(
        self,
        element,
        show_in_log=True,
        allow_check=True,
        value_in_name=False,
        clear_keys=("CTRL+A", "DEL"),
        default_value="",
    ):
        """Inicializace instance třídy EditElement.

            Args:
                element: urpa.AppElement
                    Editbox který třída obsluhuje.
                show_in_log: bool
                    Vlajka jestli je možné hodnotu zapsat do logu.
                allow_check: bool
                    Vlajka jestli se má hodnota po vyplnění kontrolovat.
                value_in_name: bool
                    Nastavení jestli se vyplněná hodnota nachází ve vlastnosti name nebo value.
                clear_keys: tuple
                    Sada kláves které je třeba stysknout pro vyčistění editboxu.
                default_value: str
                    Řetězec napevno předvyplněné hodnoty, kterou nelze vyčistit. Například
                    předvyplěné tečky pro datum.
        """
        self.value_in_name = value_in_name
        self.clear_keys = clear_keys
        self.default_value = default_value
        super().__init__(element, show_in_log, allow_check)

    @property
    def value(self):
        """Getter pro value."""
        if self.value_in_name:
            return self.element.name()
        return self.element.value()

    @value.setter
    def value(self, value):
        """Setter pro value."""
        self.element.set_focus()
        if self.value != value:
            if self.value != self.default_value:
                self._clear()
            self.element.send_text(value)

    def _clear(self):
        """Vyčistí editbox."""
        self.element.set_focus()
        for key in self.clear_keys:
            self.element.send_key(key)


class PasswordElement(_FormElement):
    """Třidá reprezentující password box."""

    def __init__(self, element, show_in_log=False, allow_check=False, clear_keys=("CTRL+A", "DEL")):
        """Inicializace instance třídy PasswordElement.

            Args:
                element: urpa.AppElement
                    Editbox který třída obsluhuje.
                show_in_log: bool
                    Vlajka jestli je možné hodnotu zapsat do logu.
                allow_check: bool
                    Vlajka jestli se má hodnota po vyplnění kontrolovat.
                value_in_name: bool
                    Nastavení jestli se vyplněná hodnota nachází ve vlastnosti name nebo value.
                clear_keys: tuple
                    Sada kláves které je třeba stysknout pro vyčistění editboxu.
        """
        self.clear_keys = clear_keys
        super().__init__(element, show_in_log, allow_check)

    @property
    def value(self):
        """Getter pro value."""
        return ""

    @value.setter
    def value(self, value):
        """Setter pro value."""
        self.element.set_focus()
        self._clear()
        self.element.send_text(value)

    def _clear(self):
        """Vyčistí editbox."""
        self.element.set_focus()
        for key in self.clear_keys:
            self.element.send_key(key)


class CheckElement(_FormElement):
    """Třída pro Checkbox ve formuláři."""

    @property
    def value(self):
        """Getter pro value."""
        return self.element.toggle_state()

    @value.setter
    def value(self, value):
        """Setter pro value."""
        if not isinstance(value, bool):
            raise TypeError("CheckBox muze mit jen hodnoty True nebo False.")
        self.element.set_focus()
        if self.value != value:
            self.element.send_mouse_click()


class RadioElement(_FormElement):
    """Třída pro Radio button ve formuláři."""

    @property
    def value(self):
        """Getter pro value."""
        return self.element.selected()

    @value.setter
    def value(self, value):
        """Setter pro value."""
        if not isinstance(value, bool):
            raise TypeError("RadioButton muze mit jen hodnoty True nebo False.")
        self.element.set_focus()
        if self.value != value:
            self.element.send_mouse_click()


class ComboElement(_FormElement):
    """Třída pro Combobox ve formuláři."""

    def __init__(self, element, show_in_log=True, allow_check=True, walk_type=False):
        """Inicializace pro Combobox.

            Args:
                element: urpa.AppElement
                    Editbox který třída obsluhuje.
                show_in_log: bool
                    Vlajka jestli je možné hodnotu zapsat do logu.
                allow_check: bool
                    Vlajka jestli se má hodnota po vyplnění kontrolovat.
                walk_type. bool
                    Vlajka jakou metodou se má nastavit hodnota.
        """
        self.walk_type = walk_type
        super().__init__(element, show_in_log, allow_check)

    @property
    def value(self):
        """Getter pro value."""
        return self.element.value()

    @value.setter
    def value(self, value):
        """Setter pro value."""
        if self.walk_type:
            self._walk_setter(value)
        else:
            self._default_setter(value)

    def _default_setter(self, value):
        """Výchozí setter pro value."""
        self.element.set_focus()
        if self.value != value:
            self.element.send_text(value)

    def _walk_setter(self, value):
        """Setter pro value pro Combobox, který nelze vyplnit metodou send_text."""
        self.element.set_focus()
        self.element.send_key("HOME")
        while self.value != value:
            self.element.send_key("DOWN")
