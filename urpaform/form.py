"""Module for filling in forms with UltimateRPA."""

import logging

from urpaform.elements import _FormElement

logger = logging.getLogger(__name__)


class Form:
    def __init__(self, form_id="default_form_id", attempts=3):
        self.elements = []
        self.form_id = form_id
        self.attempts = attempts

    def __repr__(self):
        return f"Form: {self.form_id}"

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.complete()

    def add(self, *args):
        if len(args) == 1 and isinstance(args[0], (tuple, list)):
            self.elements.extend(args[0])
        elif len(args) == 2 and isinstance(args[0], _FormElement):
            self.elements.append((args[0], args[1]))
        else:
            raise TypeError(
                "First argument should be tuple or list, then the second one is ommited"
                " or first argument is _FormElement and second is the value!"
            )

    def complete(self):
        for attempt in range(1, self.attempts + 1):
            logger.info("This is %d. attempt to complete form: '%s'.", attempt, self.form_id)
            self._fill_values()
            try:
                self._check_values()
            except FormError:
                continue
            logger.info("Form: '%s' successfully completed.", self.form_id)
            break
        else:
            raise FormError("Fatal error in form: '%s'!" % self.form_id)

    def _fill_values(self):
        for element_class, value in self.elements:
            log_value = __class__.log_value(element_class, value)
            logger.info("Fill in value: '%s' in form: '%s'.", log_value, self.form_id)
            element_class.value = value

    def _check_values(self):
        for element_class, value in self.elements:
            log_value = __class__.log_value(element_class, value)
            if not element_class.allow_check:
                logger.warning(
                    "Checking for value: '%s' in form: '%s' is not allowed!",
                    log_value,
                    self.form_id,
                )
                continue
            logger.info("Checking value: '%s' in form: '%s'.", log_value, self.form_id)
            if element_class.value != value:
                if element_class.show_in_log:
                    logger.error(
                        "Value in form: '%s' is not equal to value: '%s'!",
                        element_class.value,
                        log_value,
                    )
                else:
                    logger.error("Value in form is not equal to value!")
                raise FormError

    @staticmethod
    def log_value(element_class, value):
        if element_class.show_in_log:
            return value
        return "****"


class FormError(ValueError):
    """If the Robot can not fill in the form correctly."""
