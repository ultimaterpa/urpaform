"""Třídy elementů které lze použít v upraform."""
import urpa


# Třídy reprezentující obecný prvek formuláře.


class _FormElement:
    """Třída reprezentuje obecný prvek formuláře a nelze použít v urpaform."""

    def __init__(self, element, hide=False):
        self.element = element
        self.hide = hide

    def __repr__(self):
        return f"Form: {self.__class__.__name__} with element {self.element}."

    def __str__(self):
        return self.__repr__()


class EditElement(_FormElement):
    """Třída reprezentující obecný editbox formuláře."""

    def __init__(self, element, hide_value=False, in_value=True, clear=None, default_value=""):
        """Inicializace instance třídy _EditElem.

            Args:
                element: urpa.AppElement
                    Editbox který třída obsluhuje.
                in_value: bool
                    True pokud je hodnota editboxu uschována v parametru value.
                clear: 
                    Metoda pro čístění editboxu.
                hide_value: bool
                    False pokud může být hodnota zobrazena v logu.
        """
        self.element = element
        self.hide_value = hide_value
        self.in_value = in_value
        self.clear = __class__.clear_ctrl_a_del if clear is None else clear
        self.default_value = default_value

    @property
    def value(self):
        if self.in_value:
            return self.element.value()
        return self.element.name()

    @value.setter
    def set_value(self, value):
        self.element.set_focus()
        if self.value != value:
            if self.value != self.default_value:
                self.clear(self.element)
            self.element.send_text(value)

    @staticmethod
    def clear_sequence(element, keys):
        element.set_focus()
        for key in keys:
            element.send_key(key)

    @staticmethod
    def clear_ctrl_a_del(element):
        return __class__.clear_sequence(element, ("CTRL+A", "DEL"))

    @staticmethod
    def clear_home_shift_end_del(element):
        return __class__.clear_sequence(element, ("HOME", "SHIFT+END", "DEL"))
