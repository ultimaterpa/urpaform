"""Testy pro kontrolu typu a hodnoty pri vyplnovani formularu"""

import pytest

from unittest.mock import Mock

from urpa import AppElement
from urpaform.elements import CheckElement, ComboElement, EditElement, PasswordElement, RadioElement
from urpaform.form import Form, FormError


@pytest.mark.parametrize(
    "index, value",
    [
        (0, "John Doe"),
        (1, "1234"),
        (2, True),
        (3, True),
        (4, "Monday"),
    ],
)
def test_field_values_in_form(form, index, value) -> None:
    """Checks exact values inside the Form"""
    assert form.elements[index][1] == value


@pytest.mark.parametrize(
    "index_1, index_2, expected",
    [
        (0, 0, EditElement),
        (0, 1, str),
        (1, 0, PasswordElement),
        (2, 0, CheckElement),
        (2, 1, bool),
        (3, 0, RadioElement),
        (3, 1, bool),
        (4, 0, ComboElement),
        (4, 1, str),
    ],
)
def test_types_in_form(form, index_1, index_2, expected) -> None:
    """Checks types of values inside the Form"""
    assert isinstance(form.elements[index_1][index_2], expected)


def test_complete_method_form() -> None:
    """Checks complete() method"""

    edit_elem = Mock(EditElement(AppElement()))
    edit_elem.value.return_value = "Sunday"

    with Form("test form") as test_form:
        test_form.add(edit_elem, "Sunday")


def test_fill_values() -> None:
    """Checks _fill_values() method"""

    value_to_fill = "Sunday"
    edit_elem = Mock(EditElement(AppElement()))

    test_form = Form("test form")
    test_form.add(edit_elem, value_to_fill)
    test_form._fill_values()

    assert edit_elem.value == value_to_fill


def test_check_values() -> None:
    """Checks _check_values() method"""

    value_to_fill = "Sunday"
    edit_elem = Mock(EditElement(AppElement()))

    test_form = Form("test form")
    test_form.add(edit_elem, value_to_fill)

    with pytest.raises(FormError):
        test_form._check_values()


@pytest.mark.parametrize(
    "show, expected",
    [
        (True, "Sunday"),
        (False, "****"),
    ],
)
def test_log_value(show, expected) -> None:
    """Checks log_value method"""

    value_to_fill = "Sunday"
    edit_elem = EditElement(AppElement(), show_in_log=show)

    test_form = Form("test form")
    test_form.add(edit_elem, value_to_fill)

    assert test_form.log_value(edit_elem, value_to_fill) == expected
