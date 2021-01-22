from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from .enums import SubUseEnumType, StatusType


# Global elements and types

@dataclass
class Status:
    """The acceptance status of an element with an optional date attribute,
    which signifies the date of the status change.

    If an element does not have its own <xccdf:status> element,
    its status is that of its parent element. If there is more than one
    <xccdf:status> for a single element, then every instance of
    the <xccdf:status> element must have a @date attribute, and
    the <xccdf:status> element with the latest date is considered
    the current status.

    :ivar value:
    :ivar date: The date the parent element achieved
        the indicated status.
    """

    class Meta:
        name = "status"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    value: Optional[StatusType] = field(
        default=None,
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ParamType:
    """Type for a parameter used in the <xccdf:model> element, which
    records scoring model information. The contents of this type represent a
    name-value pair, where the name is recorded in the @name attribute and the
    value appears in the element body. <xccdf:param> elements with equal
    values for the @name attribute may not appear as children of the same.

    <xccdf:model> element.

    :ivar value:
    :ivar name: The name associated with the contained
        value.
    """

    class Meta:
        name = "paramType"

    value: Optional[str] = field(
        default=None,
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Model:
    """A suggested scoring model for an.

    <xccdf:Benchmark>, also encapsulating any parameters needed by
    the model. Every model is designated with a URI, which appears here
    as the system attribute. See the XCCDF specification for a list of
    standard scoring models and their associated URIs. Vendors may
    define their own scoring models and provide additional URIs to
    designate them. Some models may need additional parameters; to
    support such a model, zero or more <xccdf:param> elements may
    appear as children of the <xccdf:model> element.

    :ivar param: Parameters provided as input to the
        designated scoring model.
    :ivar system: A URI designating a scoring
        model.
    """

    class Meta:
        name = "model"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    param: List[ParamType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VersionType:
    """
    Type for most <xccdf:version> elements.

    :ivar value:
    :ivar time: The time that this version of the
        associated element was completed.
    :ivar update: A URI indicating a location where updates
        to the associated element may be obtained.
    """

    class Meta:
        name = "versionType"

    value: Optional[str] = field(
        default=None,
    )
    time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    update: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


# Idref types

@dataclass
class IdrefType:
    """
    Data type for elements that contain a reference to another XCCDF element.

    :ivar idref: The id value of another XCCDF
        element
    """

    class Meta:
        name = "idrefType"

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class IdrefListType:
    """
    Data type for elements contain list of references to other XCCDF elements.

    :ivar idref: A space-separated list of id values from other
        XCCDF elements
    """

    class Meta:
        name = "idrefListType"

    idref: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "required": True,
            "tokens": True,
        }
    )


@dataclass
class Cpe2IdrefType:
    """Data type for <xccdf:platform> elements that do not need @override
    attributes. (I.e., <xccdf:platform> elements that are in structures
    that cannot be extended, such as <xccdf:TestResult> and.

    <xccdf:Benchmark> elements.) This is used to identify the
    applicable target platform for its respective parent elements.

    :ivar idref: Should be a CPE 2.3 Applicability Language
        identifier using the Formatted String binding or the value of a
        <cpe:platform-specification> element's @id attribute, the
        latter acting as                     a reference to some
        expression defined using the CPE schema in the
        <xccdf:Benchmark> element's <cpe:platform-
        specification> element.                     The @idref may be
        a CPE Applicability Language identifier using the URI binding,
        although this is less preferred.
    """

    class Meta:
        name = "CPE2idrefType"

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class OverrideableCpe2IdrefType(Cpe2IdrefType):
    """Data type for <xccdf:platform> elements that need.

    @override attributes. (I.e., <xccdf:platform> elements that are in structures
    that can be extended, such as Items and <xccdf:Profile> elements.) This is
    used to identify the applicable target platform for its respective parent elements.

    :ivar override: Used to manage inheritance.
    """

    class Meta:
        name = "overrideableCPE2idrefType"

    override: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


# Text types


@dataclass
class SubType(IdrefType):
    """The type used for <xccdf:sub> elements. The.

    <xccdf:sub> element identifies replacement content that should
    appear in place of the <xccdf:sub> element during text
    substitution. The subType consists of a regular idrefType with an
    additional @use attribute to dictate the behavior of the
    <xccdf:sub> element under substitution. When the @idref is to
    an <xccdf:Value>, the @use attribute indicates whether the
    <xccdf:Value> element's title or value should replace the
    <xccdf:sub> element. The @use attribute is ignored when the
    @idref is to an <xccdf:plain-text> element; the body of the
    <xccdf:plain-text> element is always used to replace the
    <xccdf:sub> element.

    :ivar use: Dictates the nature of the content inserted
        under text substitution processing.
    """

    class Meta:
        name = "subType"

    use: SubUseEnumType = field(
        default=SubUseEnumType.VALUE,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TextType:
    """
    Type for a simple text string with an @override attribute for controlling
    inheritance.

    :ivar value:
    :ivar lang:
    :ivar override: Used to manage inheritance.
    """

    class Meta:
        name = "textType"

    value: Optional[str] = field(
        default=None,
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    override: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class HtmlTextType:
    """
    The type for a string with optional XHTML elements and an @xml:lang
    attribute.

    :ivar w3_org_1999_xhtml_element:
    :ivar lang:
    :ivar override: Used to manage inheritance.
    """

    class Meta:
        name = "htmlTextType"

    w3_org_1999_xhtml_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/1999/xhtml",
            "mixed": True,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    override: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class HtmlTextWithSubType:
    """
    The type for a string with optional XHTML elements, and an @xml:lang
    attribute.

    :ivar sub: Specifies an <xccdf:Value> or
        <xccdf:plain-text> element to be used for text
        substitution
    :ivar w3_org_1999_xhtml_element:
    :ivar lang:
    :ivar override: Used to manage inheritance.
    """

    class Meta:
        name = "htmlTextWithSubType"

    sub: List[SubType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    w3_org_1999_xhtml_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/1999/xhtml",
            "mixed": True,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    override: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ProfileNoteType:
    """Type for an <xccdf:profile-note> within an.

    <xccdf:Rule>. This element contains text that describes
    special aspects of an <xccdf:Rule> relative to one or more
    <xccdf:Profile> elements. This allows an author to document
    things within <xccdf:Rule> elements that are specific to a
    given <xccdf:Profile>. This information might then be
    displayed to a reader based on the selection of a particular
    <xccdf:Profile>. The body text may include XHTML mark-up as
    well as <xccdf:sub> elements.

    :ivar sub: Specifies an <xccdf:Value> or
        <xccdf:plain-text> element to be used for text
        substitution
    :ivar w3_org_1999_xhtml_element:
    :ivar lang:
    :ivar tag: The identifier of this note.
    """

    class Meta:
        name = "profileNoteType"

    sub: List[SubType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    w3_org_1999_xhtml_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/1999/xhtml",
            "mixed": True,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    tag: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TextWithSubType:
    """
    Type for a string with embedded <xccdf:Value> substitutions and an
    @override attribute to help manage inheritance.

    :ivar content:
    :ivar sub: Specifies an <xccdf:Value> or
        <xccdf:plain-text> element to be used for text
        substitution.
    :ivar lang:
    :ivar override: Used to manage inheritance.
    """

    class Meta:
        name = "textWithSubType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    sub: List[SubType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    override: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
