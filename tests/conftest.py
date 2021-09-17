"""There is test configurations and testcases, that are used by test functions"""

import pytest

pytest.MonkeyPatch().syspath_prepend("mock")

from urpa import AppElement

from urpaform.elements import CheckElement, ComboElement, EditElement, PasswordElement, RadioElement
from urpaform.form import Form


@pytest.fixture(name="form", scope="session")
def form_fixture():
    """Form fixture used by some test functions"""
    form = Form()
    form.add(
        (EditElement(AppElement()), "John Doe"),
        (PasswordElement(AppElement()), "1234"),
        (CheckElement(AppElement()), True),
        (RadioElement(AppElement()), True),
        (ComboElement(AppElement()), "Monday"),
    )
    return form
