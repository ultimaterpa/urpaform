"""Testy pro kontrolu exceptions"""

import pytest

from urpa import AppElement
from urpaform.elements import CheckElement, EditElement, PasswordElement, RadioElement
from urpaform.form import Form


def test_value_is_in_edit_element_exception() -> None:
    """Spatny value_is_in argument v EditElement"""
    with pytest.raises(ValueError):
        EditElement(AppElement(), value_is_in="valu")


def test_send_method_in_edit_element_exception() -> None:
    """Spatny send_method argument v EditElement"""
    with pytest.raises(ValueError):
        EditElement(AppElement(), send_method="write")


def test_send_method_in_password_element_exception() -> None:
    """Spatny send_method argument v PasswordElement"""
    with pytest.raises(ValueError):
        PasswordElement(AppElement(), send_method="write")


def test_value_check_element_exception() -> None:
    """Spatne prirazena value do CheckElement"""
    with pytest.raises(TypeError):
        with Form("test form") as test_form:
            test_form.add(CheckElement(AppElement()), "Tru")


def test_value_radio_element_exception() -> None:
    """Spatne prirazena value do RadioElement"""
    with pytest.raises(TypeError):
        with Form("test form") as test_form:
            test_form.add(RadioElement(AppElement()), "Tru")


@pytest.mark.parametrize("param", ["one word", AppElement()])
def test_invalid_form_arguments(param) -> None:
    """Spatny pocet argumentu pro Form.add()"""
    with pytest.raises(TypeError):
        with Form("test form") as test_form:
            test_form.add(param)
