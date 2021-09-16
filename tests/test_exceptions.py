"""Testy pro kontrolu exceptions"""

import pytest

from unittest.mock import Mock

from urpa import AppElement
from urpaform.elements import CheckElement, EditElement, PasswordElement, RadioElement
from urpaform.form import Form, FormError


def test_value_is_in_edit_element_exception() -> None:
    """Wrong value_is_in argument in EditElement"""
    with pytest.raises(ValueError):
        EditElement(AppElement(), value_is_in="valu")


def test_send_method_in_edit_element_exception() -> None:
    """Wrong send_method argument in EditElement"""
    with pytest.raises(ValueError):
        EditElement(AppElement(), send_method="write")


def test_send_method_in_password_element_exception() -> None:
    """Wrong send_method argument in PasswordElement"""
    with pytest.raises(ValueError):
        PasswordElement(AppElement(), send_method="write")


def test_value_check_element_exception() -> None:
    """Wrong value assigned to CheckElement"""
    with pytest.raises(TypeError):
        with Form("test form") as test_form:
            test_form.add(CheckElement(AppElement()), "Tru")


def test_value_radio_element_exception() -> None:
    """Wrong value assigned to RadioElement"""
    with pytest.raises(TypeError):
        with Form("test form") as test_form:
            test_form.add(RadioElement(AppElement()), "Tru")


@pytest.mark.parametrize("param", ["one word", AppElement()])
def test_invalid_form_arguments(param) -> None:
    """Wrong number of argumens for Form.add()"""
    with pytest.raises(TypeError):
        with Form("test form") as test_form:
            test_form.add(param)


def test_complete_method_exception() -> None:
    """Checks complete() method exception inside Form"""

    edit_elem = Mock(EditElement(AppElement()))

    with pytest.raises(FormError):
        test_form = Mock(Form("test form"))
        test_form.add(edit_elem, "Saturday")

        test_form.complete.side_effect = FormError
        test_form.complete()
