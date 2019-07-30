"""Modul pro vyplňování formulářů v nástroji UltimateRPA.

TODO
- nezobrazovat hesla
- docstrings
- pridat akci pro odeslani formulare
- kontrola jestli se nesnažím vyplnit stejný element vícekrát???
- vlastní loggování

"""
__version__ = "0.0.001"

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


class Form:

    def __init__(self, user_id=None, attempts=3):
        self.elements = []
        self.user_id = user_id
        self.attempts = attempts

    def __str__(self):
        # TODO Nesmí zobrazit heslo
        return f"{self.__class__.__name__}: '{self.user_id}'" if self.user_id is not None else self.__repr__()

    def __repr__(self):
        # TODO Nesmí zobrazit heslo
        return repr(self.elements)

    def add(self, element_class, value):
        self.elements.append((element_class, value))

    def complete(self):
        for attempt in range(1, self.attempts + 1):
            logging.info(f"This is {attempt}. attempt to complete form: '{self.user_id}'.")
            self._fill_values()
            try:
                self._check_values()
            except FormError:
                continue
            logging.info(f"Form: '{self.user_id}' successfully completed.")
            break
        else:
            raise FormError(f"Fatal error in form: '{self.user_id}'!")

    def _fill_values(self):
        # TODO Nesmí zobrazit pass
        for element_class, value in self.elements:
            if element_class.hide:
                logging.info(f"Fill in value: '****' in form.")
            else:
                logging.info(f"Fill in value: '{value}' in form.")
            element_class.value = value

    def _check_values(self):
        # TODO Nesmí zobrazit pass
        for element_class, value in self.elements:
            logging.info(f"Checking value: '{value}' in form.")
            if element_class.value != value:
                logging.error(f"Value in form : '{element_class.value}' is not equal to value: '{value}'!")
                raise FormError


class FormError(ValueError):
    """Pokud se nepodaří robotovi správně vyplnit formulář."""
