"""Module for filling in forms with UltimateRPA."""

from __future__ import annotations

import logging
from time import sleep
from typing import Any, Iterable, Tuple, Union

import urpa
from .elements import _FormElement

logger = logging.getLogger(__name__)


class Form:
    """A class representing a form."""

    def __init__(self, form_id: str = "default_form_id", attempts: int = 3, delay: int = 0) -> None:
        """Iniciates instance of the Form class.

        Args:
            form_id: str
                A custom ID of the form
            attempts: int
                Specifies the number of attempts for filling the form
            delay: int
                Specifies wait time between each attempt
        """
        self.elements: list = []
        self.form_id = form_id
        self.attempts = attempts
        self.delay = delay

    def __repr__(self) -> str:
        return f"Form: {self.form_id}"

    def __enter__(self) -> Form:
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, exc_tb: Any) -> None:
        self.complete()

    def add(self, *args: Union[Tuple[_FormElement, str], Iterable[Tuple[_FormElement, str]]]) -> None:
        """Add element to form.

        Args:
            *args:
                Case1: _FormElement, string
                    Element, Value
                Case2: Tuple
                    Tuple in format (Element, Value)
        """
        if len(args) == 2 and isinstance(args[0], _FormElement):
            self.elements.append((args[0], args[1]))
        elif all(isinstance(e, tuple) for e in args):
            self.elements.extend(args)
        else:
            raise TypeError(
                "Method expects either two arguments, where first is an element and "
                "second is a value or any number of tuple arguments!"
            )

    def complete(self) -> None:
        """Complete elements in form with values."""
        for attempt in range(1, self.attempts + 1):
            logger.info(f"This is {attempt}. attempt to complete form: '{self.form_id}'.")
            self._fill_values()
            urpa.set_clipboard_text("")
            try:
                self._check_values()
            except FormError:
                continue
            logger.info(f"Form: '{self.form_id}' successfully completed.")
            break
        else:
            raise FormError(f"Fatal error in form: '{self.form_id}'!")

    def _fill_values(self) -> None:
        for element_class, value in self.elements:
            log_value = __class__.log_value(element_class, value)
            logger.info(f"Fill in value: '{log_value}' in form: '{self.form_id}'.")
            element_class.value = value
            if self.delay:
                sleep(self.delay)

    def _check_values(self) -> None:
        for element_class, value in self.elements:
            log_value = __class__.log_value(element_class, value)
            if not element_class.allow_check:
                logger.warning(f"Checking for value: '{log_value}' in form: '{self.form_id}' is not allowed!")
                continue
            logger.info(f"Checking value: '{log_value}' in form: '{self.form_id}'.")
            if element_class.value != value:
                if element_class.show_in_log:
                    logger.error(f"Value in form: '{element_class.value}' is not equal to value: '{log_value}'!")
                else:
                    logger.error("Value in form is not equal to value!")
                raise FormError

    @staticmethod
    def log_value(element_class: _FormElement, value: str) -> str:
        """Return 'value' if element is enable to show_in_log else return '****'"""
        if element_class.show_in_log:
            return value
        return "****"


class FormError(ValueError):
    """If the Robot can not fill in the form correctly."""
