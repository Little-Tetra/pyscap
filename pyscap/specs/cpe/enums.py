from enum import Enum


class OperatorEnumeration(Enum):
    """The OperatorEnumeration simple type defines acceptable operators.

    Each operator defines how to evaluate multiple arguments.
    """
    AND_VALUE = "AND"
    OR_VALUE = "OR"
