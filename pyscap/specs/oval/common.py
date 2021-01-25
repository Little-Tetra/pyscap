from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from .enums import MessageLevelEnumeration


@dataclass
class DeprecatedInfoType:
    """The DeprecatedInfoType complex type defines a structure that will be
    used to flag schema-defined constructs as deprecated.

    It holds information related to the version of OVAL when the
    construct was deprecated along with a reason and comment.

    :ivar version: The required version child element details the
        version of OVAL in which the construct became deprecated.
    :ivar reason: The required reason child element is used to provide
        an explanation as to why an item was deprecated and to direct a
        reader to possible alternative structures within OVAL.
    :ivar comment: The optional comment child element is used to supply
        additional information regarding the element's deprecated
        status.
    """
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[0-9]+\.[0-9]+(\.[0-9]+)?(:[0-9]+\.[0-9]+(\.[0-9]+)?)?",
        }
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ElementMapItemType:
    """
    Defines a reference to an OVAL entity using the schema namespace and
    element name.

    :ivar value:
    :ivar target_namespace: The target_namespace attributes indicates
        what XML namespace the element belongs to. If not present, the
        namespace is that of the document in which the
        ElementMapItemType instance element appears.
    """
    value: Optional[str] = field(
        default=None,
    )
    target_namespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class NotesType:
    """The NotesType complex type is a container for one or more note child
    elements.

    Each note contains some information about the definition or tests
    that it references. A note may record an unresolved question about
    the definition or test or present the reason as to why a particular
    approach was taken.
    """
    note: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class SchemaVersionType:
    """
    The core version MUST match on all platform schema versions.

    :ivar value:
    :ivar platform: The platform attribute is available to indicate the
        URI of the target namespace for any platform extension being
        included. This platform attribute is to be omitted when
        specifying the core schema version.
    """
    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"[0-9]+\.[0-9]+(\.[0-9]+)?(:[0-9]+\.[0-9]+(\.[0-9]+)?)?",
        }
    )
    platform: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ElementMapType:
    """
    The ElementMapType is used to document the association between OVAL test,
    object, state, and item entities.

    :ivar test: The local name of an OVAL test.
    :ivar object: The local name of an OVAL object.
    :ivar state: The local name of an OVAL state.
    :ivar item: The local name of an OVAL item.
    """
    test: Optional[ElementMapItemType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    object: Optional[ElementMapItemType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    state: Optional[ElementMapItemType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    item: Optional[ElementMapItemType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GeneratorType:
    """The GeneratorType complex type defines an element that is used to hold
    information about when a particular OVAL document was compiled, what
    version of the schema was used, what tool compiled the document, and what
    version of that tool was used.

    Additional generator information is also allowed although it is not
    part of the official OVAL Schema. Individual organizations can place
    generator information that they feel are important and these will be
    skipped during the validation. All OVAL really cares about is that
    the stated generator information is there.

    :ivar product_name: The optional product_name specifies the name of
        the application used to generate the file. Product names SHOULD
        be expressed as CPE Names according to the Common Platform
        Enumeration: Name Matching Specification Version 2.3.
    :ivar product_version: The optional product_version specifies the
        version of the application used to generate the file.
    :ivar schema_version: The required schema_version specifies the
        version of the OVAL Schema that the document has been written in
        and that should be used for validation. The versions for both
        the Core and any platform extensions used should be declared in
        separate schema_version elements.
    :ivar timestamp: The required timestamp specifies when the
        particular OVAL document was compiled. The format for the
        timestamp is yyyy-mm-ddThh:mm:ss. Note that the timestamp
        element does not specify when a definition (or set of
        definitions) was created or modified but rather when the actual
        XML document that contains the definition was created. For
        example, the document might have pulled a bunch of existing OVAL
        Definitions together, each of the definitions having been
        created at some point in the past. The timestamp in this case
        would be when the combined document was created.
    :ivar any_element: The Asset Identification specification
        (http://scap.nist.gov/specifications/ai/) provides a
        standardized way of reporting asset information across different
        organizations. Asset Identification elements can hold data
        useful for identifying what tool, what version of that tool was
        used, and identify other assets used to compile an OVAL
        document, such as persons or organizations. To support greater
        interoperability, an ai:assets element describing assets used to
        produce an OVAL document may appear at this point in an OVAL
        document.
    """
    product_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    product_version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    schema_version: List[SchemaVersionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class MessageType:
    """The MessageType complex type defines the structure for which messages
    are relayed from the data collection engine.

    Each message is a text string that has an associated level attribute
    identifying the type of message being sent. These messages could be
    error messages, warning messages, debug messages, etc. How the
    messages are used by tools and whether or not they are displayed to
    the user is up to the specific implementation. Please refer to the
    description of the MessageLevelEnumeration for more information
    about each type of message.
    """
    value: Optional[str] = field(
        default=None,
    )
    level: MessageLevelEnumeration = field(
        default=MessageLevelEnumeration.INFO,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DeprecatedInfo(DeprecatedInfoType):
    """The deprecated_info element is used in documenting deprecation
    information for items in the OVAL Language.

    It is declared globally as it can be found in any of the OVAL
    schemas and is used as part of the appinfo documentation and
    therefore it is not an element that can be declared locally and
    based off a global type..
    """

    class Meta:
        name = "deprecated_info"
        namespace = "http://oval.mitre.org/XMLSchema/oval-common-5"


@dataclass
class Notes(NotesType):
    """
    Element for containing notes; can be replaced using a substitution group.
    """

    class Meta:
        name = "notes"
        namespace = "http://oval.mitre.org/XMLSchema/oval-common-5"


@dataclass
class ElementMapping(ElementMapType):
    """The element_mapping element is used in documenting which tests, objects,
    states, and system characteristic items are associated with each other.

    It provides a way to explicitly and programatically associate the
    test, object, state, and item definitions.
    """

    class Meta:
        name = "element_mapping"
        namespace = "http://oval.mitre.org/XMLSchema/oval-common-5"
