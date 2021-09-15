"""Testy pro kontrolu typu a hodnoty pri vyplnovani formularu"""

import pytest

from urpa import AppElement
from urpaform.elements import CheckElement, ComboElement, EditElement, PasswordElement, RadioElement
from urpaform.form import Form


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
    assert isinstance(form.elements[index_1][index_2], expected)


# def test_complete_method_form() -> None:
#     with Form("test form") as test_form:
#         test_form.add(EditElement(AppElement()), "Sunday")
