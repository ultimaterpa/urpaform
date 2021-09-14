"""There are stored all aliases required by urpaform"""

from typing import Iterable, Tuple, Union

from .elements import _FormElement

FORM_ELEMENTS_WITH_VALUES = (
    Union[
        Tuple[_FormElement, Union[str, bool], Union[str, bool]],
        Tuple[_FormElement, Union[str, bool]],
        Iterable[Union[Tuple[_FormElement, Union[str, bool], Union[str, bool]], Tuple[_FormElement, Union[str, bool]]]],
    ],
)
