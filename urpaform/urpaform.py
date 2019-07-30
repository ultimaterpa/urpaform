"""Modul pro vyplňování formulářů v nástroji UltimateRPA."""

__version__ = "0.0.001"

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


class Form:
    def __init__(self, form_id="default_form_id", attempts=3):
        self.elements = []
        self.form_id = form_id
        self.attempts = attempts

    def __repr__(self):

        return f"Form: {self.form_id}"

    def add(self, element_class, value):
        self.elements.append((element_class, value))

    def complete(self):
        for attempt in range(1, self.attempts + 1):
            logging.info("This is %d. attempt to complete form: '%s'.", attempt, self.form_id)
            self._fill_values()
            try:
                self._check_values()
            except FormError:
                continue
            logging.info("Form: '%s' successfully completed.", self.form_id)
            break
        else:
            raise FormError("Fatal error in form: '%s'!" % self.form_id)

    def _fill_values(self):
        for element_class, value in self.elements:
            log_value = __class__.log_value(element_class, value)
            logging.info("Fill in value: '%s' in form: '%s'.", log_value, self.form_id)
            element_class.value = value

    def _check_values(self):
        for element_class, value in self.elements:
            log_value = __class__.log_value(element_class, value)
            logging.info("Checking value: '%s' in form: '%s'.", log_value, self.form_id)
            if element_class.value != value:
                if element_class.show_in_log:
                    logging.error(
                        "Value in form: '%s' is not equal to value: '%s'!", element_class.value, log_value
                    )
                else:
                    logging.error("Value in form is not equal to value!")
                raise FormError

    @staticmethod
    def log_value(element_class, value):
        if element_class.show_in_log:
            return value
        return "****"


class FormError(ValueError):
    """Pokud se nepodaří robotovi správně vyplnit formulář."""
