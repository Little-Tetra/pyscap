from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://cpe.mitre.org/language/2.0"


@dataclass
class FactRefType:
    """The fact-ref element appears as a child of a logical-test element.

    It is simply a reference to a CPE Name that always evaluates to a
    Boolean result.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"cpe:/([aho](:[A-Za-z0-9\._\-~]*(:[A-Za-z0-9\._\-~]*(:[A-Za-z0-9\._\.\-~]*(:[A-Za-z0-9\._\-~]*)?)?)?)?)?",
        }
    )


@dataclass
class TextType:
    """
    This type allows the xml:lang attribute to associate a specific language
    with an element's string content.
    """

    class Meta:
        name = "textType"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


class OperatorEnumeration(Enum):
    """The OperatorEnumeration simple type defines acceptable operators.

    Each operator defines how to evaluate multiple arguments.
    """
    AND_VALUE = "AND"
    OR_VALUE = "OR"


@dataclass
class LogicalTestType:
    """The logical-test element appears as a child of a platform element, and
    may also be nested to create more complex logical tests.

    The content consists of one or more elements: fact-ref, and logical-
    test children are permitted. The operator to be applied, and
    optional negation of the test, are given as attributes.
    """
    logical_test: List["LogicalTestType"] = field(
        default_factory=list,
        metadata={
            "name": "logical-test",
            "type": "Element",
            "namespace": "",
        }
    )
    fact_ref: List[FactRefType] = field(
        default_factory=list,
        metadata={
            "name": "fact-ref",
            "type": "Element",
            "namespace": "",
        }
    )
    operator: Optional[OperatorEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    negate: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PlatformType:
    """The platform element represents the description or qualifications of a
    particular IT platform type.

    The platform is defined by the logical-test child element. The id
    attribute holds a locally unique name for the platform. There is no
    defined format for this id, it just has to be unique to the
    containing language document. The optional title element may appear
    as a child to a platform element. It provides a human-readable title
    for it. To support uses intended for multiple languages, this
    element supports the ‘xml:lang’ attribute. At most one title element
    can appear for each language. The optional remark element may appear
    as a child of a platform element. It provides some additional
    description. Zero or more remark elements may appear. To support
    uses intended for multiple languages, this element supports the
    ‘xml:lang’ attribute. There can be multiple remarks for a single
    language.
    """
    title: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    remark: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    logical_test: Optional[LogicalTestType] = field(
        default=None,
        metadata={
            "name": "logical-test",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PlatformSpecification:
    """
    This element is the root element of a CPE Language XML documents and
    therefore acts as a container for child platform definitions.
    """

    class Meta:
        name = "platform-specification"
        namespace = "http://cpe.mitre.org/language/2.0"

    platform: List[PlatformType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
