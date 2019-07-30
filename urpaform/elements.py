"""Třídy elementů které lze použít v upraform."""

import urpa


# Třídy reprezentující obecný prvek formuláře.


class _FormElement:
    """Třída reprezentuje obecný prvek formuláře a nelze použít v urpaform."""

    def __init__(self, element, show_in_log=True):
        """Inicializace instance třídy _EditElem.

            Args:
                element: urpa.AppElement
                    Editbox který třída obsluhuje.
                show_in_log: bool
                    Vlajka jestli je možné hodnotu zapsat do logu. 
        """
        self.element = element
        self.show_in_log = show_in_log

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
        value_in_name=False,
        clear_keys=("CTRL+A", "DEL"),
        default_value="",
    ):
        """Inicializace instance třídy _EditElem.

            Args:
                element: urpa.AppElement
                    Editbox který třída obsluhuje.
                show_in_log: bool
                    Vlajka jestli je možné hodnotu zapsat do logu.
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
        super().__init__(element, show_in_log)

    @property
    def value(self):
        if self.value_in_name:
            return self.element.name()
        return self.element.value()

    @value.setter
    def value(self, value):
        self.element.set_focus()
        if self.value != value:
            if self.value != self.default_value:
                self._clear()
            self.element.send_text(value)

    def _clear(self):
        self.element.set_focus()
        for key in self.clear_keys:
            self.element.send_key(key)
