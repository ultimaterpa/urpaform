"""There are stored all custom error exceptions"""


class FormError(ValueError):
    """If the Robot can not fill in the form correctly."""


class FormArgumentsError(TypeError):
    """If the arguments are given to Form in the bad type."""


class KeyArgumentError(ValueError):
    """If the value to key argument is not supported."""


class ValueTypeError(TypeError):
    """If the element value type is invalid."""


class UnableToSetValue(ValueError):
    """If the value is unable to set in field."""
