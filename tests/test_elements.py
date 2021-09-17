"""Tests, which check all elements from elements.py"""


import pytest

from urpa import AppElement
from urpaform.elements import EditElement, PasswordElement


VALUE_IS_IN = ["value", "name", "text_value"]
SEND_METHOD = ["writing", "pasting"]


@pytest.mark.parametrize("value", VALUE_IS_IN)
def test_value_is_in_editelement(value):
    """Check correct assignment argument values_is_in in EditElement"""

    edit_eleme = EditElement(AppElement(), value_is_in=value)

    assert edit_eleme.value_is_in == value


@pytest.mark.parametrize("value", SEND_METHOD)
def test_send_method_editelement(value):
    """Check correct assignment argument send_method in EditElement"""

    edit_eleme = EditElement(AppElement(), send_method=value)

    assert edit_eleme.send_method == value


@pytest.mark.parametrize("value", SEND_METHOD)
def test_send_method_passwordelement(value):
    """Check correct assignment argument send_method in PasswordElement"""

    password_eleme = PasswordElement(AppElement(), send_method=value)

    assert password_eleme.send_method == value
