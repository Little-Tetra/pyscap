from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

from .common import (
    DatatypeEnumeration,
    GeneratorType,
    MessageType,
    SimpleDatatypeEnumeration,
)
from ..common.utils import scap_parser, scap_json_parser, scap_serializer, scap_json_serializer
from ..common.xmldsig import Signature

OVAL_SYSTEM_CHARACTERISTICS_5_NAMESPACE = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5"


class EntityItemIpaddressStringTypeDatatype(Enum):
    """
    :cvar BINARY: The binary datatype is used to represent hex-encoded
        data that is in raw (non-printable) form. This datatype conforms
        to the W3C Recommendation for binary data meaning that each
        binary octet is encoded as a character tuple, consisting of two
        hexadecimal digits {[0-9a-fA-F]} representing the octet code.
        Expected operations within OVAL for binary values are 'equals'
        and 'not equal'.
    :cvar BOOLEAN: The boolean datatype represents standard boolean
        data, either true or false.  This datatype conforms to the W3C
        Recommendation for boolean data meaning that the following
        literals are legal values: {true, false, 1, 0}.  Expected
        operations within OVAL for boolean values are 'equals' and 'not
        equal'.
    :cvar EVR_STRING: The evr_string datatype represents the epoch,
        version, and release fields as a single version string. It has
        the form "EPOCH:VERSION-RELEASE". Comparisons involving this
        datatype should follow the algorithm of librpm's rpmvercmp()
        function. Expected operations within OVAL for evr_string values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', and 'less than or equal'.
    :cvar DEBIAN_EVR_STRING: The debian_evr_string datatype represents
        the epoch, upstream_version, and debian_revision fields, for a
        Debian package, as a single version string. It has the form
        "EPOCH:UPSTREAM_VERSION-DEBIAN_REVISION". Comparisons involving
        this datatype should follow the algorithm outlined in Chapter 5
        of the "Debian Policy Manual"
        (https://www.debian.org/doc/debian-policy/ch-
        controlfields.html#s-f-Version). Note that a null epoch is
        equivalent to a value of '0'. An implementation of this is the
        cmpversions() function in dpkg's enquiry.c. Expected operations
        within OVAL for debian_evr_string values are 'equals', 'not
        equal', 'greater than', 'greater than or equal', 'less than',
        and 'less than or equal'.
    :cvar FILESET_REVISION: The fileset_revision datatype represents the
        version string related to filesets in HP-UX. An example would be
        'A.03.61.00'. For more information, see the HP-UX "Software
        Distributor Administration Guide"
        (http://h20000.www2.hp.com/bc/docs/support/SupportManual/c01919399/c01919399.pdf).
        Expected operations within OVAL for fileset_version values are
        'equals', 'not equal', 'greater than', 'greater than or equal',
        'less than', and 'less than or equal'.
    :cvar FLOAT_VALUE: The float datatype describes standard float data.
        This datatype conforms to the W3C Recommendation for float data
        meaning it is patterned after the IEEE single-precision 32-bit
        floating point type.  The format consists of a decimal followed,
        optionally, by the character 'E' or 'e', followed by an integer
        exponent.  The special values positive and negative infinity and
        not-a-number have are represented by INF, -INF and NaN,
        respectively.  Expected operations within OVAL for float values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', and 'less than or equal'.
    :cvar IOS_VERSION: The ios_version datatype describes Cisco IOS
        Train strings. These are in essence version strings for IOS.
        Please refer to Cisco's IOS Reference Guide for information on
        how to compare different Trains as they follow a very specific
        pattern. Expected operations within OVAL for ios_version values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', and 'less than or equal'.
    :cvar INT_VALUE: The int datatype describes standard integer data.
        This datatype conforms to the W3C Recommendation for integer
        data which follows the standard mathematical concept of the
        integer numbers.  (no decimal point and infinite range)
        Expected operations within OVAL for int values are 'equals',
        'not equal', 'greater than', 'greater than or equal', 'less
        than', 'less than or equal', 'bitwise and', and 'bitwise or'.
    :cvar IPV4_ADDRESS:
    :cvar IPV6_ADDRESS:
    :cvar STRING:
    :cvar VERSION: The version datatype represents a value that is a
        hierarchical list of non-negative integers separated by a single
        character delimiter.  Note that any non-number character can be
        used as a delimiter and that different characters can be used
        within the same version string.  So '#.#-#' is the same as
        '#.#.#' or '#c#c#' where '#' is any non-negative integer.
        Expected operations within OVAL for version values are 'equals',
        'not equal', 'greater than', 'greater than or equal', 'less
        than', and 'less than or equal'. For example '#.#.#' or
        '#-#-#-#' where the numbers to the left are more significant
        than the numbers to the right. When performing an 'equals'
        operation on a version datatype, you should first check the left
        most number for equality. If that fails, then the values are not
        equal. If it succeeds, then check the second left most number
        for equality. Continue checking the numbers from left to right
        until the last number has been checked. If, after testing all
        the previous numbers, the last number is equal then the two
        versions are equal. When performing other operations, such as
        'less than', 'less than or equal', 'greater than, or 'greater
        than or equal', similar logic as above is used. Start with the
        left most number and move from left to right. For each number,
        check if it is less than the number you are testing against. If
        it is, then the version in question is less than the version you
        are testing against. If the number is equal, then move to check
        the next number to the right. For example, to test if 5.7.23 is
        less than or equal to 5.8.0 you first compare 5 to 5. They are
        equal so you move on to compare 7 to 8. 7 is less than 8 so the
        entire test succeeds and 5.7.23 is 'less than or equal' to
        5.8.0. The difference between the 'less than' and 'less than or
        equal' operations is how the last number is handled. If the last
        number is reached, the check should use the given operation
        (either 'less than' and 'less than or equal') to test the
        number. For example, to test if 4.23.6 is greater than 4.23.6
        you first compare 4 to 4. They are equal so you move on to
        compare 23 to 23. They are equal so you move on to compare 6 to
        6. This is the last number in the version and since 6 is not
        greater than 6, the entire test fails and 4.23.6 is not greater
        than 4.23.6. Version strings with a different number of
        components shall be padded with zeros to make them the same
        size. For example, if the version strings '1.2.3' and '6.7.8.9'
        are being compared, then the short one should be padded to
        become '1.2.3.0'.
    """
    BINARY = "binary"
    BOOLEAN = "boolean"
    EVR_STRING = "evr_string"
    DEBIAN_EVR_STRING = "debian_evr_string"
    FILESET_REVISION = "fileset_revision"
    FLOAT_VALUE = "float"
    IOS_VERSION = "ios_version"
    INT_VALUE = "int"
    IPV4_ADDRESS = "ipv4_address"
    IPV6_ADDRESS = "ipv6_address"
    STRING = "string"
    VERSION = "version"


class FlagEnumeration(Enum):
    """The FlagEnumeration simple type defines the valid flags associated with
    a collected object.

    These flags are meant to provide information about how the specified
    object was handled by the data collector. In order to evaluate an
    OVAL Definition, information about the defined objects needs to be
    available. The flags help detail the outcome of attempting to
    collect information related to these objects..

    :cvar ERROR: A flag of 'error' indicates that there was an error
        trying to identify items on the system that match the specified
        object declaration. This flag is not meant to be used when there
        was an error retrieving a specific entity, but rather when it
        could not be determined if an item exists or not. Any error in
        retrieving a specific entity should be represented by setting
        the status of that specific entity to 'error'.
    :cvar COMPLETE: A flag of 'complete' indicates that every matching
        item on the system has been identified and is represented in the
        system characteristics file. It can be assumed that no
        additional matching items exist on the system.
    :cvar INCOMPLETE: A flag of 'incomplete' indicates that a matching
        item exists on the system, but only some of the matching items
        have been identified and are represented in the system
        characteristics file. It is unknown if additional matching items
        also exist. Note that with a flag of 'incomplete', each item
        that has been identified  matches the object declaration, but
        additional items might also exist on the system.
    :cvar DOES_NOT_EXIST: A flag of 'does not exist' indicates that the
        underlying structure is installed on the system but no matching
        item was found. For example, the Windows metabase is installed
        but there were no items that matched the metabase_object. In
        this example, if the metabase itself was not installed, then the
        flag would have been 'not applicable'.
    :cvar NOT_COLLECTED: A flag of 'not collected' indicates that no
        attempt was made to collect items on the system. An object with
        this flag will produce an 'unknown' result during analysis since
        it is unknown if matching items exists on the system or not.
        This is different from an 'error' flag because an 'error' flag
        indicates that an attempt was made to collect items on system
        whereas a 'not collected' flag indicates that an attempt was not
        made to collect items on the system.
    :cvar NOT_APPLICABLE: A flag of 'not applicable' indicates that the
        specified object is not applicable to the system being
        characterized. This could be because the data repository is not
        installed or that the object structure is for a different flavor
        of systems. An example would be trying to collect objects
        related to a Red Hat system off of a Windows system. Another
        example would be trying to collect an rpminfo_object on a Linux
        system if the rpm packaging system is not installed. If the rpm
        packaging system is installed and the specified rpminfo_object
        could not be found, then the flag would be 'does not exist'.
    """
    ERROR = "error"
    COMPLETE = "complete"
    INCOMPLETE = "incomplete"
    DOES_NOT_EXIST = "does not exist"
    NOT_COLLECTED = "not collected"
    NOT_APPLICABLE = "not applicable"


@dataclass
class InterfaceType:
    """The InterfaceType complex type is used to describe an existing network
    interface on the system.

    This information can help identify a specific system on a given
    network.

    :ivar interface_name: The required interface_name element is the
        name of the interface
    :ivar ip_address: The required ip_address element holds the IP
        address for the interface. Note that the IP address can be IPv4
        or IPv6.
    :ivar mac_address: The required mac_address element holds the MAC
        address for the interface. MAC addresses should be formatted
        according to the IEEE 802-2001 standard which states that a MAC
        address is a sequence of six octet values, separated by hyphens,
        where each octet is represented by two hexadecimal digits.
        Uppercase letters should also be used to represent the
        hexadecimal digits A through F.
    """
    interface_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    ip_address: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    mac_address: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ReferenceType:
    """The ReferenceType complex type specifies an item in the system
    characteristics file.

    This reference is used to link global OVAL Objects to specific
    items.
    """
    item_ref: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class StatusEnumeration(Enum):
    """
    The StatusEnumeration simple type defines the valid status messages
    associated with collection of specific information associated with an item.

    :cvar ERROR: A status of 'error' says that there was an error
        collecting information associated with an item as a whole or any
        specific entity. An item would have a status of 'error' if a
        problem occurred that prevented the item from being collected.
        For example, a file_item would have a status of 'error' if a
        handle to the file could not be opened because the handle was
        already in use by another program. See the documentation for
        ItemType for information about when an item entity status of
        'error' should propagate up to the item status level.
    :cvar EXISTS: A status of 'exists' says that the item or specific
        piece of information exists on the system and has been
        collected.
    :cvar DOES_NOT_EXIST: A status of 'does not exist' says that the
        item or specific piece of information does not exist and
        therefore has not been collected. This status assumes that an
        attempt was made to collect the information, but the information
        just does not exist. This can happen when a certain entity is
        only pertinent to particular instances or if the information for
        that entity is not set.
    :cvar NOT_COLLECTED: A status of 'not collected' says that no
        attempt was made to collect the item or specific piece of
        information so it is unknown what the value is and if it even
        exists.
    """
    ERROR = "error"
    EXISTS = "exists"
    DOES_NOT_EXIST = "does not exist"
    NOT_COLLECTED = "not collected"


@dataclass
class VariableValueType:
    """The VariableValueType complex type holds the value to a variable used
    during the collection of an object.

    The required variable_id attribute is the unique id of the variable
    being identified.
    """
    value: Optional[object] = field(
        default=None,
    )
    variable_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:var:[1-9][0-9]*",
        }
    )


@dataclass
class EntityItemAnySimpleType:
    """The EntityItemAnySimpleType type is extended by the entities of an
    individual item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    describes any simple data.

    :ivar value:
    :ivar datatype:
    :ivar mask: The optional mask attribute is used to identify values
        that have been hidden for sensitivity concerns.
        This is used by the Result document which uses the System
        Characteristics schema to format the information found on a
        specific system.                     When the mask attribute is
        set to 'true' on an OVAL Entity or an OVAL Field, the
        corresponding collected value of that OVAL Entity or OVAL Field
        MUST NOT be present in the "results" section of the OVAL Results
        document; the "oval_definitions" section must not be altered and
        must be an exact copy of the definitions evaluated.
        Values MUST NOT be masked in OVAL System Characteristics
        documents that are not contained within an OVAL Results
        document.                     It is possible for masking
        conflicts to occur where one entity has mask set to true and
        another entity has mask set to false.                     A
        conflict will occur when the mask attribute is set differently
        on an OVAL Object and matching OVAL State or when more than one
        OVAL Objects identify the same OVAL Item(s).
        When such a conflict occurs the result is always to mask the
        entity.
    :ivar status: The optional status attribute holds information
        regarding the success of the data collection. For example, if
        there was an error collecting a particular piece of data, then
        the status would be 'error'.
    """
    value: Optional[str] = field(
        default=None,
    )
    datatype: SimpleDatatypeEnumeration = field(
        default=SimpleDatatypeEnumeration.STRING,
        metadata={
            "type": "Attribute",
        }
    )
    mask: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EntityItemBinaryType:
    """The EntityItemBinaryType type is extended by the entities of an
    individual item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    describes simple binary data. The empty string is also allowed for
    cases where there was an error in the data collection of an entity
    and a status needs to be reported.

    :ivar value:
    :ivar datatype:
    :ivar mask: The optional mask attribute is used to identify values
        that have been hidden for sensitivity concerns.
        This is used by the Result document which uses the System
        Characteristics schema to format the information found on a
        specific system.                     When the mask attribute is
        set to 'true' on an OVAL Entity or an OVAL Field, the
        corresponding collected value of that OVAL Entity or OVAL Field
        MUST NOT be present in the "results" section of the OVAL Results
        document; the "oval_definitions" section must not be altered and
        must be an exact copy of the definitions evaluated.
        Values MUST NOT be masked in OVAL System Characteristics
        documents that are not contained within an OVAL Results
        document.                     It is possible for masking
        conflicts to occur where one entity has mask set to true and
        another entity has mask set to false.                     A
        conflict will occur when the mask attribute is set differently
        on an OVAL Object and matching OVAL State or when more than one
        OVAL Objects identify the same OVAL Item(s).
        When such a conflict occurs the result is always to mask the
        entity.
    :ivar status: The optional status attribute holds information
        regarding the success of the data collection. For example, if
        there was an error collecting a particular piece of data, then
        the status would be 'error'.
    """
    value: Optional[Union[bytes, str]] = field(
        default=None,
        metadata={
            "max_length": 0,
            "format": "base16",
        }
    )
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.BINARY,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    mask: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EntityItemBoolType:
    """The EntityItemBoolType type is extended by the entities of an individual
    item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    describes simple boolean data. The empty string is also allowed for
    cases where there was an error in the data collection of an entity
    and a status needs to be reported.

    :ivar value:
    :ivar datatype:
    :ivar mask: The optional mask attribute is used to identify values
        that have been hidden for sensitivity concerns.
        This is used by the Result document which uses the System
        Characteristics schema to format the information found on a
        specific system.                     When the mask attribute is
        set to 'true' on an OVAL Entity or an OVAL Field, the
        corresponding collected value of that OVAL Entity or OVAL Field
        MUST NOT be present in the "results" section of the OVAL Results
        document; the "oval_definitions" section must not be altered and
        must be an exact copy of the definitions evaluated.
        Values MUST NOT be masked in OVAL System Characteristics
        documents that are not contained within an OVAL Results
        document.                     It is possible for masking
        conflicts to occur where one entity has mask set to true and
        another entity has mask set to false.                     A
        conflict will occur when the mask attribute is set differently
        on an OVAL Object and matching OVAL State or when more than one
        OVAL Objects identify the same OVAL Item(s).
        When such a conflict occurs the result is always to mask the
        entity.
    :ivar status: The optional status attribute holds information
        regarding the success of the data collection. For example, if
        there was an error collecting a particular piece of data, then
        the status would be 'error'.
    """
    value: Optional[Union[bool, str]] = field(
        default=None,
        metadata={
            "max_length": 0,
        }
    )
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.BOOLEAN,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    mask: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EntityItemComplexBaseType:
    """
    The EntityItemComplexBaseType complex type is an abstract type that serves
    as the base type for all complex item entities.

    :ivar datatype: The optional datatype attribute determines the type
        of data expected (the default datatype is 'string'). Note that
        the datatype attribute simply defines the type of data as found
        on the system, it is not used during evaluation. An OVAL
        Definition defines how the data should be interpreted during
        analysis. If the definition states a datatype that is different
        than what the system characteristics presents, then a type cast
        must be made.
    :ivar mask: The optional mask attribute is used to identify values
        that have been hidden for sensitivity concerns.
        This is used by the Result document which uses the System
        Characteristics schema to format the information found on a
        specific system.                     When the mask attribute is
        set to 'true' on an OVAL Entity or an OVAL Field, the
        corresponding collected value of that OVAL Entity or OVAL Field
        MUST NOT be present in the "results" section of the OVAL Results
        document; the "oval_definitions" section must not be altered and
        must be an exact copy of the definitions evaluated.
        Values MUST NOT be masked in OVAL System Characteristics
        documents that are not contained within an OVAL Results
        document.                     It is possible for masking
        conflicts to occur where one entity has mask set to true and
        another entity has mask set to false.                     A
        conflict will occur when the mask attribute is set differently
        on an OVAL Object and matching OVAL State or when more than one
        OVAL Objects identify the same OVAL Item(s).
        When such a conflict occurs the result is always to mask the
        entity.
    :ivar status: The optional status attribute holds information
        regarding the success of the data collection. For example, if
        there was an error collecting a particular piece of data, then
        the status would be 'error'.
    """
    datatype: DatatypeEnumeration = field(
        default=DatatypeEnumeration.STRING,
        metadata={
            "type": "Attribute",
        }
    )
    mask: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EntityItemDebianEvrstringType:
    """The EntityItemDebianEVRStringType type is extended by the entities of an
    individual item.

    This type provides uniformity to each entity by including the attributes found in the EntityItemSimpleBaseType. This type represents the epoch, upstream_version, and debian_revision fields, for a Debian package, as a single version string. It has the form "EPOCH:UPSTREAM_VERSION-DEBIAN_REVISION". Note that a null epoch (or '(none)' as returned by dpkg) is equivalent to '0' and would hence have the form 0:UPSTREAM_VERSION-DEBIAN_REVISION. Comparisons involving this datatype should follow the algorithm outlined in Chapter 5 of the "Debian Policy Manual" (https://www.debian.org/doc/debian-policy/ch-controlfields.html#s-f-Version). An implementation of this is the cmpversions() function in dpkg's enquiry.c.

    :ivar value:
    :ivar datatype:
    :ivar mask: The optional mask attribute is used to identify values
        that have been hidden for sensitivity concerns.
        This is used by the Result document which uses the System
        Characteristics schema to format the information found on a
        specific system.                     When the mask attribute is
        set to 'true' on an OVAL Entity or an OVAL Field, the
        corresponding collected value of that OVAL Entity or OVAL Field
        MUST NOT be present in the "results" section of the OVAL Results
        document; the "oval_definitions" section must not be altered and
        must be an exact copy of the definitions evaluated.
        Values MUST NOT be masked in OVAL System Characteristics
        documents that are not contained within an OVAL Results
        document.                     It is possible for masking
        conflicts to occur where one entity has mask set to true and
        another entity has mask set to false.                     A
        conflict will occur when the mask attribute is set differently
        on an OVAL Object and matching OVAL State or when more than one
        OVAL Objects identify the same OVAL Item(s).
        When such a conflict occurs the result is always to mask the
        entity.
    :ivar status: The optional status attribute holds information
        regarding the success of the data collection. For example, if
        there was an error collecting a particular piece of data, then
        the status would be 'error'.
    """

    class Meta:
        name = "EntityItemDebianEVRStringType"

    value: Optional[str] = field(
        default=None,
    )
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.DEBIAN_EVR_STRING,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    mask: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EntityItemEvrstringType:
    """The EntityItemEVRStringType type is extended by the entities of an
    individual item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This type
    represents the epoch, version, and release fields, for an RPM
    package, as a single version string. It has the form "EPOCH:VERSION-
    RELEASE". Note that a null epoch (or '(none)' as returned by rpm) is
    equivalent to '0' and would hence have the form 0:VERSION-RELEASE.
    Comparisons involving this datatype should follow the algorithm of
    librpm's rpmvercmp() function.

    :ivar value:
    :ivar datatype:
    :ivar mask: The optional mask attribute is used to identify values
        that have been hidden for sensitivity concerns.
        This is used by the Result document which uses the System
        Characteristics schema to format the information found on a
        specific system.                     When the mask attribute is
        set to 'true' on an OVAL Entity or an OVAL Field, the
        corresponding collected value of that OVAL Entity or OVAL Field
        MUST NOT be present in the "results" section of the OVAL Results
        document; the "oval_definitions" section must not be altered and
        must be an exact copy of the definitions evaluated.
        Values MUST NOT be masked in OVAL System Characteristics
        documents that are not contained within an OVAL Results
        document.                     It is possible for masking
        conflicts to occur where one entity has mask set to true and
        another entity has mask set to false.                     A
        conflict will occur when the mask attribute is set differently
        on an OVAL Object and matching OVAL State or when more than one
        OVAL Objects identify the same OVAL Item(s).
        When such a conflict occurs the result is always to mask the
        entity.
    :ivar status: The optional status attribute holds information
        regarding the success of the data collection. For example, if
        there was an error collecting a particular piece of data, then
        the status would be 'error'.
    """

    class Meta:
        name = "EntityItemEVRStringType"

    value: Optional[str] = field(
        default=None,
    )
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.EVR_STRING,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    mask: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EntityItemFieldType:
    """The EntityItemFieldType defines an element with simple content that
    represents a named field in a record that may contain any number of named
    fields.

    The EntityItemFieldType is much like all other entities with one
    significant difference, the EntityItemFieldType has a name
    attribute. The required name attribute specifies a name for the
    field. Field names are lowercase and may occur more than once to
    allow for a field to have multiple values. Note that when the mask
    attribute is set to 'true' on a field's parent element the field
    must be masked regardless of the field's mask attribute value.

    :ivar value:
    :ivar name: A string restricted to disallow upper case characters.
    :ivar datatype: The optional datatype attribute determines the type
        of data expected (the default datatype is 'string'). Note that
        the datatype attribute simply defines the type of data as found
        on the system, it is not used during evaluation. An OVAL
        Definition defines how the data should be interpreted during
        analysis. If the definition states a datatype that is different
        than what the system characteristics presents, then a type cast
        must be made.
    :ivar mask: The optional mask attribute is used to identify values
        that have been hidden for sensitivity concerns.
        This is used by the Result document which uses the System
        Characteristics schema to format the information found on a
        specific system.                     When the mask attribute is
        set to 'true' on an OVAL Entity or an OVAL Field, the
        corresponding collected value of that OVAL Entity or OVAL Field
        MUST NOT be present in the "results" section of the OVAL Results
        document; the "oval_definitions" section must not be altered and
        must be an exact copy of the definitions evaluated.
        Values MUST NOT be masked in OVAL System Characteristics
        documents that are not contained within an OVAL Results
        document.                     It is possible for masking
        conflicts to occur where one entity has mask set to true and
        another entity has mask set to false.                     A
        conflict will occur when the mask attribute is set differently
        on an OVAL Object and matching OVAL State or when more than one
        OVAL Objects identify the same OVAL Item(s).
        When such a conflict occurs the result is always to mask the
        entity.
    :ivar status: The optional status attribute holds information
        regarding the success of the data collection. For example, if
        there was an error collecting a particular piece of data, then
        the status would be 'error'.
    """
    value: Optional[object] = field(
        default=None,
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^A-Z]+",
        }
    )
    datatype: DatatypeEnumeration = field(
        default=DatatypeEnumeration.STRING,
        metadata={
            "type": "Attribute",
        }
    )
    mask: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EntityItemFilesetRevisionType:
    """The EntityItemFilesetRevisionType type is extended by the entities of an
    individual item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    represents the version string related to filesets in HP-UX.

    :ivar value:
    :ivar datatype:
    :ivar mask: The optional mask attribute is used to identify values
        that have been hidden for sensitivity concerns.
        This is used by the Result document which uses the System
        Characteristics schema to format the information found on a
        specific system.                     When the mask attribute is
        set to 'true' on an OVAL Entity or an OVAL Field, the
        corresponding collected value of that OVAL Entity or OVAL Field
        MUST NOT be present in the "results" section of the OVAL Results
        document; the "oval_definitions" section must not be altered and
        must be an exact copy of the definitions evaluated.
        Values MUST NOT be masked in OVAL System Characteristics
        documents that are not contained within an OVAL Results
        document.                     It is possible for masking
        conflicts to occur where one entity has mask set to true and
        another entity has mask set to false.                     A
        conflict will occur when the mask attribute is set differently
        on an OVAL Object and matching OVAL State or when more than one
        OVAL Objects identify the same OVAL Item(s).
        When such a conflict occurs the result is always to mask the
        entity.
    :ivar status: The optional status attribute holds information
        regarding the success of the data collection. For example, if
        there was an error collecting a particular piece of data, then
        the status would be 'error'.
    """
    value: Optional[str] = field(
        default=None,
    )
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.FILESET_REVISION,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    mask: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EntityItemFloatType:
    """The EntityItemFloatType type is extended by the entities of an
    individual item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    describes simple float data. The empty string is also allowed for
    cases where there was an error in the data collection of an entity
    and a status needs to be reported.

    :ivar value:
    :ivar datatype:
    :ivar mask: The optional mask attribute is used to identify values
        that have been hidden for sensitivity concerns.
        This is used by the Result document which uses the System
        Characteristics schema to format the information found on a
        specific system.                     When the mask attribute is
        set to 'true' on an OVAL Entity or an OVAL Field, the
        corresponding collected value of that OVAL Entity or OVAL Field
        MUST NOT be present in the "results" section of the OVAL Results
        document; the "oval_definitions" section must not be altered and
        must be an exact copy of the definitions evaluated.
        Values MUST NOT be masked in OVAL System Characteristics
        documents that are not contained within an OVAL Results
        document.                     It is possible for masking
        conflicts to occur where one entity has mask set to true and
        another entity has mask set to false.                     A
        conflict will occur when the mask attribute is set differently
        on an OVAL Object and matching OVAL State or when more than one
        OVAL Objects identify the same OVAL Item(s).
        When such a conflict occurs the result is always to mask the
        entity.
    :ivar status: The optional status attribute holds information
        regarding the success of the data collection. For example, if
        there was an error collecting a particular piece of data, then
        the status would be 'error'.
    """
    value: Optional[Union[float, str]] = field(
        default=None,
        metadata={
            "max_length": 0,
        }
    )
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.FLOAT_VALUE,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    mask: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EntityItemIosversionType:
    """The EntityItemIOSVersionType type is extended by the entities of an
    individual item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    represents the version string for IOS.

    :ivar value:
    :ivar datatype:
    :ivar mask: The optional mask attribute is used to identify values
        that have been hidden for sensitivity concerns.
        This is used by the Result document which uses the System
        Characteristics schema to format the information found on a
        specific system.                     When the mask attribute is
        set to 'true' on an OVAL Entity or an OVAL Field, the
        corresponding collected value of that OVAL Entity or OVAL Field
        MUST NOT be present in the "results" section of the OVAL Results
        document; the "oval_definitions" section must not be altered and
        must be an exact copy of the definitions evaluated.
        Values MUST NOT be masked in OVAL System Characteristics
        documents that are not contained within an OVAL Results
        document.                     It is possible for masking
        conflicts to occur where one entity has mask set to true and
        another entity has mask set to false.                     A
        conflict will occur when the mask attribute is set differently
        on an OVAL Object and matching OVAL State or when more than one
        OVAL Objects identify the same OVAL Item(s).
        When such a conflict occurs the result is always to mask the
        entity.
    :ivar status: The optional status attribute holds information
        regarding the success of the data collection. For example, if
        there was an error collecting a particular piece of data, then
        the status would be 'error'.
    """

    class Meta:
        name = "EntityItemIOSVersionType"

    value: Optional[str] = field(
        default=None,
    )
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.IOS_VERSION,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    mask: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EntityItemIpaddressStringType:
    """The EntityItemIPAddressStringType type is extended by the entities of an
    individual item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    describes any IPv4/IPv6 address, address prefix, or its string
    representation.

    :ivar value:
    :ivar datatype:
    :ivar mask: The optional mask attribute is used to identify values
        that have been hidden for sensitivity concerns.
        This is used by the Result document which uses the System
        Characteristics schema to format the information found on a
        specific system.                     When the mask attribute is
        set to 'true' on an OVAL Entity or an OVAL Field, the
        corresponding collected value of that OVAL Entity or OVAL Field
        MUST NOT be present in the "results" section of the OVAL Results
        document; the "oval_definitions" section must not be altered and
        must be an exact copy of the definitions evaluated.
        Values MUST NOT be masked in OVAL System Characteristics
        documents that are not contained within an OVAL Results
        document.                     It is possible for masking
        conflicts to occur where one entity has mask set to true and
        another entity has mask set to false.                     A
        conflict will occur when the mask attribute is set differently
        on an OVAL Object and matching OVAL State or when more than one
        OVAL Objects identify the same OVAL Item(s).
        When such a conflict occurs the result is always to mask the
        entity.
    :ivar status: The optional status attribute holds information
        regarding the success of the data collection. For example, if
        there was an error collecting a particular piece of data, then
        the status would be 'error'.
    """

    class Meta:
        name = "EntityItemIPAddressStringType"

    value: Optional[str] = field(
        default=None,
    )
    datatype: EntityItemIpaddressStringTypeDatatype = field(
        default=EntityItemIpaddressStringTypeDatatype.STRING,
        metadata={
            "type": "Attribute",
        }
    )
    mask: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EntityItemIpaddressType:
    """The EntityItemIPAddressType type is extended by the entities of an
    individual item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    describes any IPv4/IPv6 address or address prefix.

    :ivar value:
    :ivar datatype:
    :ivar mask: The optional mask attribute is used to identify values
        that have been hidden for sensitivity concerns.
        This is used by the Result document which uses the System
        Characteristics schema to format the information found on a
        specific system.                     When the mask attribute is
        set to 'true' on an OVAL Entity or an OVAL Field, the
        corresponding collected value of that OVAL Entity or OVAL Field
        MUST NOT be present in the "results" section of the OVAL Results
        document; the "oval_definitions" section must not be altered and
        must be an exact copy of the definitions evaluated.
        Values MUST NOT be masked in OVAL System Characteristics
        documents that are not contained within an OVAL Results
        document.                     It is possible for masking
        conflicts to occur where one entity has mask set to true and
        another entity has mask set to false.                     A
        conflict will occur when the mask attribute is set differently
        on an OVAL Object and matching OVAL State or when more than one
        OVAL Objects identify the same OVAL Item(s).
        When such a conflict occurs the result is always to mask the
        entity.
    :ivar status: The optional status attribute holds information
        regarding the success of the data collection. For example, if
        there was an error collecting a particular piece of data, then
        the status would be 'error'.
    """

    class Meta:
        name = "EntityItemIPAddressType"

    value: Optional[str] = field(
        default=None,
    )
    datatype: Optional["EntityItemIpaddressType.Datatype"] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    mask: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        }
    )

    class Datatype(Enum):
        """
        :cvar BINARY: The binary datatype is used to represent hex-
            encoded data that is in raw (non-printable) form. This
            datatype conforms to the W3C Recommendation for binary data
            meaning that each binary octet is encoded as a character
            tuple, consisting of two hexadecimal digits {[0-9a-fA-F]}
            representing the octet code.  Expected operations within
            OVAL for binary values are 'equals' and 'not equal'.
        :cvar BOOLEAN: The boolean datatype represents standard boolean
            data, either true or false.  This datatype conforms to the
            W3C Recommendation for boolean data meaning that the
            following literals are legal values: {true, false, 1, 0}.
            Expected operations within OVAL for boolean values are
            'equals' and 'not equal'.
        :cvar EVR_STRING: The evr_string datatype represents the epoch,
            version, and release fields as a single version string. It
            has the form "EPOCH:VERSION-RELEASE". Comparisons involving
            this datatype should follow the algorithm of librpm's
            rpmvercmp() function. Expected operations within OVAL for
            evr_string values are 'equals', 'not equal', 'greater than',
            'greater than or equal', 'less than', and 'less than or
            equal'.
        :cvar DEBIAN_EVR_STRING: The debian_evr_string datatype
            represents the epoch, upstream_version, and debian_revision
            fields, for a Debian package, as a single version string. It
            has the form "EPOCH:UPSTREAM_VERSION-DEBIAN_REVISION".
            Comparisons involving this datatype should follow the
            algorithm outlined in Chapter 5 of the "Debian Policy
            Manual" (https://www.debian.org/doc/debian-policy/ch-
            controlfields.html#s-f-Version). Note that a null epoch is
            equivalent to a value of '0'. An implementation of this is
            the cmpversions() function in dpkg's enquiry.c. Expected
            operations within OVAL for debian_evr_string values are
            'equals', 'not equal', 'greater than', 'greater than or
            equal', 'less than', and 'less than or equal'.
        :cvar FILESET_REVISION: The fileset_revision datatype represents
            the version string related to filesets in HP-UX. An example
            would be 'A.03.61.00'. For more information, see the HP-UX
            "Software Distributor Administration Guide"
            (http://h20000.www2.hp.com/bc/docs/support/SupportManual/c01919399/c01919399.pdf).
            Expected operations within OVAL for fileset_version values
            are 'equals', 'not equal', 'greater than', 'greater than or
            equal', 'less than', and 'less than or equal'.
        :cvar FLOAT_VALUE: The float datatype describes standard float
            data.  This datatype conforms to the W3C Recommendation for
            float data meaning it is patterned after the IEEE single-
            precision 32-bit floating point type.  The format consists
            of a decimal followed, optionally, by the character 'E' or
            'e', followed by an integer exponent.  The special values
            positive and negative infinity and not-a-number have are
            represented by INF, -INF and NaN, respectively.  Expected
            operations within OVAL for float values are 'equals', 'not
            equal', 'greater than', 'greater than or equal', 'less
            than', and 'less than or equal'.
        :cvar IOS_VERSION: The ios_version datatype describes Cisco IOS
            Train strings. These are in essence version strings for IOS.
            Please refer to Cisco's IOS Reference Guide for information
            on how to compare different Trains as they follow a very
            specific pattern. Expected operations within OVAL for
            ios_version values are 'equals', 'not equal', 'greater
            than', 'greater than or equal', 'less than', and 'less than
            or equal'.
        :cvar INT_VALUE: The int datatype describes standard integer
            data.  This datatype conforms to the W3C Recommendation for
            integer data which follows the standard mathematical concept
            of the integer numbers.  (no decimal point and infinite
            range)  Expected operations within OVAL for int values are
            'equals', 'not equal', 'greater than', 'greater than or
            equal', 'less than', 'less than or equal', 'bitwise and',
            and 'bitwise or'.
        :cvar IPV4_ADDRESS:
        :cvar IPV6_ADDRESS:
        :cvar STRING: The string datatype describes standard string
            data. This datatype conforms to the W3C Recommendation for
            string data.  Expected operations within OVAL for string
            values are 'equals', 'not equal', 'case insensitive equals',
            'case insensitive not equal', 'pattern match'.
        :cvar VERSION: The version datatype represents a value that is a
            hierarchical list of non-negative integers separated by a
            single character delimiter.  Note that any non-number
            character can be used as a delimiter and that different
            characters can be used within the same version string.  So
            '#.#-#' is the same as '#.#.#' or '#c#c#' where '#' is any
            non-negative integer.  Expected operations within OVAL for
            version values are 'equals', 'not equal', 'greater than',
            'greater than or equal', 'less than', and 'less than or
            equal'. For example '#.#.#' or '#-#-#-#' where the numbers
            to the left are more significant than the numbers to the
            right. When performing an 'equals' operation on a version
            datatype, you should first check the left most number for
            equality. If that fails, then the values are not equal. If
            it succeeds, then check the second left most number for
            equality. Continue checking the numbers from left to right
            until the last number has been checked. If, after testing
            all the previous numbers, the last number is equal then the
            two versions are equal. When performing other operations,
            such as 'less than', 'less than or equal', 'greater than, or
            'greater than or equal', similar logic as above is used.
            Start with the left most number and move from left to right.
            For each number, check if it is less than the number you are
            testing against. If it is, then the version in question is
            less than the version you are testing against. If the number
            is equal, then move to check the next number to the right.
            For example, to test if 5.7.23 is less than or equal to
            5.8.0 you first compare 5 to 5. They are equal so you move
            on to compare 7 to 8. 7 is less than 8 so the entire test
            succeeds and 5.7.23 is 'less than or equal' to 5.8.0. The
            difference between the 'less than' and 'less than or equal'
            operations is how the last number is handled. If the last
            number is reached, the check should use the given operation
            (either 'less than' and 'less than or equal') to test the
            number. For example, to test if 4.23.6 is greater than
            4.23.6 you first compare 4 to 4. They are equal so you move
            on to compare 23 to 23. They are equal so you move on to
            compare 6 to 6. This is the last number in the version and
            since 6 is not greater than 6, the entire test fails and
            4.23.6 is not greater than 4.23.6. Version strings with a
            different number of components shall be padded with zeros to
            make them the same size. For example, if the version strings
            '1.2.3' and '6.7.8.9' are being compared, then the short one
            should be padded to become '1.2.3.0'.
        """
        BINARY = "binary"
        BOOLEAN = "boolean"
        EVR_STRING = "evr_string"
        DEBIAN_EVR_STRING = "debian_evr_string"
        FILESET_REVISION = "fileset_revision"
        FLOAT_VALUE = "float"
        IOS_VERSION = "ios_version"
        INT_VALUE = "int"
        IPV4_ADDRESS = "ipv4_address"
        IPV6_ADDRESS = "ipv6_address"
        STRING = "string"
        VERSION = "version"


@dataclass
class EntityItemIntType:
    """The EntityItemIntType type is extended by the entities of an individual
    item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    describes simple integer data. The empty string is also allowed for
    cases where there was an error in the data collection of an entity
    and a status needs to be reported.

    :ivar value:
    :ivar datatype:
    :ivar mask: The optional mask attribute is used to identify values
        that have been hidden for sensitivity concerns.
        This is used by the Result document which uses the System
        Characteristics schema to format the information found on a
        specific system.                     When the mask attribute is
        set to 'true' on an OVAL Entity or an OVAL Field, the
        corresponding collected value of that OVAL Entity or OVAL Field
        MUST NOT be present in the "results" section of the OVAL Results
        document; the "oval_definitions" section must not be altered and
        must be an exact copy of the definitions evaluated.
        Values MUST NOT be masked in OVAL System Characteristics
        documents that are not contained within an OVAL Results
        document.                     It is possible for masking
        conflicts to occur where one entity has mask set to true and
        another entity has mask set to false.                     A
        conflict will occur when the mask attribute is set differently
        on an OVAL Object and matching OVAL State or when more than one
        OVAL Objects identify the same OVAL Item(s).
        When such a conflict occurs the result is always to mask the
        entity.
    :ivar status: The optional status attribute holds information
        regarding the success of the data collection. For example, if
        there was an error collecting a particular piece of data, then
        the status would be 'error'.
    """
    value: Optional[Union[int, str]] = field(
        default=None,
        metadata={
            "max_length": 0,
        }
    )
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.INT_VALUE,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    mask: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EntityItemSimpleBaseType:
    """
    The EntityItemSimpleBaseType complex type is an abstract type that serves
    as the base type for all simple item entities.

    :ivar value:
    :ivar datatype: The optional datatype attribute determines the type
        of data expected (the default datatype is 'string'). Note that
        the datatype attribute simply defines the type of data as found
        on the system, it is not used during evaluation. An OVAL
        Definition defines how the data should be interpreted during
        analysis. If the definition states a datatype that is different
        than what the system characteristics presents, then a type cast
        must be made.
    :ivar mask: The optional mask attribute is used to identify values
        that have been hidden for sensitivity concerns.
        This is used by the Result document which uses the System
        Characteristics schema to format the information found on a
        specific system.                     When the mask attribute is
        set to 'true' on an OVAL Entity or an OVAL Field, the
        corresponding collected value of that OVAL Entity or OVAL Field
        MUST NOT be present in the "results" section of the OVAL Results
        document; the "oval_definitions" section must not be altered and
        must be an exact copy of the definitions evaluated.
        Values MUST NOT be masked in OVAL System Characteristics
        documents that are not contained within an OVAL Results
        document.                     It is possible for masking
        conflicts to occur where one entity has mask set to true and
        another entity has mask set to false.                     A
        conflict will occur when the mask attribute is set differently
        on an OVAL Object and matching OVAL State or when more than one
        OVAL Objects identify the same OVAL Item(s).
        When such a conflict occurs the result is always to mask the
        entity.
    :ivar status: The optional status attribute holds information
        regarding the success of the data collection. For example, if
        there was an error collecting a particular piece of data, then
        the status would be 'error'.
    """
    value: Optional[object] = field(
        default=None,
    )
    datatype: DatatypeEnumeration = field(
        default=DatatypeEnumeration.STRING,
        metadata={
            "type": "Attribute",
        }
    )
    mask: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EntityItemStringType:
    """The EntityItemStringType type is extended by the entities of an
    individual item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    describes simple string data.

    :ivar value:
    :ivar datatype:
    :ivar mask: The optional mask attribute is used to identify values
        that have been hidden for sensitivity concerns.
        This is used by the Result document which uses the System
        Characteristics schema to format the information found on a
        specific system.                     When the mask attribute is
        set to 'true' on an OVAL Entity or an OVAL Field, the
        corresponding collected value of that OVAL Entity or OVAL Field
        MUST NOT be present in the "results" section of the OVAL Results
        document; the "oval_definitions" section must not be altered and
        must be an exact copy of the definitions evaluated.
        Values MUST NOT be masked in OVAL System Characteristics
        documents that are not contained within an OVAL Results
        document.                     It is possible for masking
        conflicts to occur where one entity has mask set to true and
        another entity has mask set to false.                     A
        conflict will occur when the mask attribute is set differently
        on an OVAL Object and matching OVAL State or when more than one
        OVAL Objects identify the same OVAL Item(s).
        When such a conflict occurs the result is always to mask the
        entity.
    :ivar status: The optional status attribute holds information
        regarding the success of the data collection. For example, if
        there was an error collecting a particular piece of data, then
        the status would be 'error'.
    """
    value: Optional[str] = field(
        default=None,
    )
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.STRING,
        metadata={
            "type": "Attribute",
        }
    )
    mask: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EntityItemVersionType:
    """The EntityItemVersionType type is extended by the entities of an
    individual item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    describes version data.

    :ivar value:
    :ivar datatype:
    :ivar mask: The optional mask attribute is used to identify values
        that have been hidden for sensitivity concerns.
        This is used by the Result document which uses the System
        Characteristics schema to format the information found on a
        specific system.                     When the mask attribute is
        set to 'true' on an OVAL Entity or an OVAL Field, the
        corresponding collected value of that OVAL Entity or OVAL Field
        MUST NOT be present in the "results" section of the OVAL Results
        document; the "oval_definitions" section must not be altered and
        must be an exact copy of the definitions evaluated.
        Values MUST NOT be masked in OVAL System Characteristics
        documents that are not contained within an OVAL Results
        document.                     It is possible for masking
        conflicts to occur where one entity has mask set to true and
        another entity has mask set to false.                     A
        conflict will occur when the mask attribute is set differently
        on an OVAL Object and matching OVAL State or when more than one
        OVAL Objects identify the same OVAL Item(s).
        When such a conflict occurs the result is always to mask the
        entity.
    :ivar status: The optional status attribute holds information
        regarding the success of the data collection. For example, if
        there was an error collecting a particular piece of data, then
        the status would be 'error'.
    """
    value: Optional[str] = field(
        default=None,
    )
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.VERSION,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    mask: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class InterfacesType:
    """The InterfacesType complex type is a container for zero or more
    interface elements.

    Each interface element is used to describe an existing network
    interface on the system.

    :ivar interface: Please refer to the description of the
        InterfaceType for more information.
    """
    interface: List[InterfaceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class ItemType:
    """The ItemType complex type specifies an optional message element that is
    used to pass things like error messages during data collection to a tool
    that will utilize the information.

    The required id attribute is a unique (to the file) identifier that
    allows the specific item to be referenced. The required status
    attribute holds information regarding the success of the data
    collection. For example, if an item exists on the system then the
    status would reflect this with a value of 'exists'. If an error
    occurs which is not associated with any item entities, or if an
    error occurs that is associated with an item entity matching an
    associated object entity, then the status would be 'error'. An error
    specific to any particular entity should be addressed at the entity
    level and, for item entities not associated with an object entity,
    not the item level. When creating items, any entities that can
    successfully be collected should be reported. In some cases, when an
    item for a specified object does not exist, it may be beneficial to
    report a partial match of an item showing what entities did exist
    and what entities did not exist for debugging purposes. This is
    especially true when considering items that are collected by objects
    with hierarchical object entities. An example of such a case is when
    a file_object has a path entity equal to 'C:\' and a filename entity
    equal to 'test.txt' where 'test.txt' does not exist in the 'C:\'
    directory. This would result in the creation of a partially matching
    file_item with a status of 'does not exist' where the path entity
    equals 'C:\' and the filename entity equals 'test.txt' with a status
    of 'does not exist'. By showing the partial match, someone reading a
    system-characteristics document can quickly see that a matching
    file_item did not exist because the specified filename did not exist
    and not that the specified path did not exist. Again, please note
    that the implementation of partial matches, when an item for a
    specified object does not exist,  is completely optional.
    """
    message: List[MessageType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 50,
        }
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ObjectType:
    """The ObjectType complex type provides a reference between items collected
    and a related global OVAL Object.

    If an OVAL Object does not exist on the system, then an object
    element is still provided but with the flag attribute set to 'does
    not exist'. For details on how to handle items, when an OVAL Object
    does not exist on the system, please see the ItemType documentation.
    This shows that the object was looked for but not found on the
    system. If no object element is written in this case, users of the
    system characteristics file will not know whether the object was not
    found or no attempt was made to collect it. The required id
    attribute is the id of the global OVAL Object. The required version
    attribute is the specific version of the global OVAL Object that was
    used by the data collection engine. The version is necessary so that
    analysis using a system characteristics file knows exactly what was
    collected. The optional variable_instance identifier is a unique id
    that differentiates each unique instance of an object. Capabilities
    that use OVAL may reference the same definition multiple times and
    provide different variable values each time the definition is
    referenced. This will result in multiple instances of an object
    being included in the OVAL System Characteristics file (definitions
    that do not use variables can only have one unique instance). The
    inclusion of this unique instance identifier allows the OVAL Results
    document to associate the correct objects and items for each
    combination of supplied values. The optional comment attribute
    provides a short description of the object. The required flag
    attribute holds information regarding the outcome of the data
    collection. For example, if there was an error looking for items
    that match the object specification, then the flag would be 'error'.
    Please refer to the description of FlagEnumeration for details about
    the different flag values.

    :ivar message: The optional message element holds an error message
        or some other string that the data collection engine wishes to
        pass along.
    :ivar variable_value: The optional variable_value elements define
        the actual value(s) used during data collection of any variable
        referenced by the object (as well as any object referenced via a
        set element). An OVAL Object that includes a variable maybe have
        a different unique set of matching items depending on the value
        assigned to the variable. A tool that is given an OVAL System
        Characteristics file in order to analyze an OVAL Definition
        needs to be able to determine the exact instance of an object to
        use based on the variable values supplied. If a variable
        represents a collection of values, then multiple variable_value
        elements would exist with the same variable_id attribute.
    :ivar reference: The optional reference element links the collected
        item found by the data collection engine and the global OVAL
        Object. A global OVAL Object my have multiple matching items on
        a system. For example a global file object that is a pattern
        match might match 10 different files on a specific system. In
        this case, there would be 10 reference elements, one for each of
        the files found on the system.
    :ivar id:
    :ivar version:
    :ivar variable_instance:
    :ivar comment:
    :ivar flag:
    """
    message: List[MessageType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    variable_value: List[VariableValueType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    reference: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:obj:[1-9][0-9]*",
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    variable_instance: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    flag: Optional[FlagEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CollectedObjectsType:
    """The CollectedObjectsType complex type states all the objects that have
    been collected by the system characteristics file.

    The details of each object are defined by the global OVAL object
    that is identified by the id.
    """
    object: List[ObjectType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class EntityItemRecordType(EntityItemComplexBaseType):
    """The EntityItemRecordType defines an entity that consists of a number of
    named fields.

    This structure is used for representing a record from a database
    query and other similar structures where multiple related fields
    must be collected at once. Note that for all entities of this type,
    the only allowed datatype is 'record'. Note the datatype attribute
    must be set to 'record'. Note that when the mask attribute is set to
    'true', all child field elements must be masked regardless of the
    child field's mask attribute value.
    """
    field_value: List[EntityItemFieldType] = field(
        default_factory=list,
        metadata={
            "name": "field",
            "type": "Element",
        }
    )


@dataclass
class SystemInfoType:
    """The SystemInfoType complex type specifies general information about the
    system that data was collected from, including information that can be used
    to identify the system.

    See the description of the InterfacesType complex type for more
    information. Note that the high level interfaces is required due to
    the inclusion of the xsd:any tag that follows it. The interfaces tag
    can be empty if no single interface is present. Additional system
    information is also allowed although it is not part of the official
    OVAL Schema. Individual organizations can place system information
    that they feel is important and these will be skipped during the
    validation. All OVAL really cares about is that the required system
    information items are there.

    :ivar os_name: The required os_name elements describes the operating
        system of the machine the data was collected on.
    :ivar os_version: The required os_version elements describe the
        operating system version of the machine the data was collected
        on.
    :ivar architecture: The required architecture element describes the
        hardware architecture type of the system data was collected on.
    :ivar primary_host_name: The required primary_host_name element is
        the primary host name of the machine the data was collected on.
    :ivar interfaces: The required interfaces element outlines the
        network interfaces that exist on the system.
    :ivar any_element: The Asset Identification specification
        (http://scap.nist.gov/specifications/ai/) provides a
        standardized way of reporting asset information across different
        organizations. The information contained within an AI computing-
        device element is similar to the information collected by OVAL's
        SystemInfoType. To support greater interoperability, an
        ai:computing-device element describing the system that data was
        collected from may appear at this point in an OVAL System
        Characteristics document.
    """
    os_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    os_version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    architecture: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    primary_host_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    interfaces: Optional[InterfacesType] = field(
        default=None,
        metadata={
            "type": "Element",
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
class Item(ItemType):
    """The abstract item element holds information about a specific item on a
    system.

    An item might be a file, a rpm, a process, etc. This element is
    extended by the different component schemas through substitution
    groups. Each item represents a unique instance of an object as
    specified by an OVAL Object. For example, a single file or a single
    user. Each item may be referenced by more than one object in the
    collected object section. Please refer to the description of
    ItemType for more details about the information stored in items.
    """

    class Meta:
        name = "item"
        namespace = OVAL_SYSTEM_CHARACTERISTICS_5_NAMESPACE


@dataclass
class SystemDataType:
    """The SystemDataType complex type is a container for one or more item
    elements.

    Each item defines a specific piece of data on the system.
    """
    item: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "min_occurs": 1,
        }
    )
    # item: List[Item] = field(
    #     default_factory=list,
    #     metadata={
    #         "type": "Element",
    #         "namespace": OVAL_SYSTEM_CHARACTERISTICS_5_NAMESPACE,
    #         "min_occurs": 1,
    #     }
    # )


@dataclass
class OvalSystemCharacteristics:
    """The system_characteristics element is the root of an OVAL System
    Characteristics Document, and must occur exactly once.

    Its purpose is to bind together the four major sections of a system characteristics file - generator, system_info, collected_objects, and system_data - which are the children of the oval_system_characteristics element.

    :ivar generator: The generator section must be present and provides
        information about when the system characteristics file was
        compiled and under what version.
    :ivar system_info: The required system_info element is used to
        record information about the system being described.
    :ivar collected_objects: The optional collected_objects section is
        used to associated the ids of the OVAL Objects collected with
        the system characteristics items that have been defined. The
        collected_objects section provides a listing of all the objects
        used to generate this system characteristics file.
    :ivar system_data: The optional system_data section defines the
        specific characteristics that have been collected from the
        system.
    :ivar signature: The optional Signature element allows an XML
        Signature as defined by the W3C to be attached to the document.
        This allows authentication and data integrity to be provided to
        the user. Enveloped signatures are supported. More information
        about the official W3C Recommendation regarding XML digital
        signatures can be found at http://www.w3.org/TR/xmldsig-core/.
    """

    class Meta:
        name = "oval_system_characteristics"
        namespace = OVAL_SYSTEM_CHARACTERISTICS_5_NAMESPACE

    generator: Optional[GeneratorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    system_info: Optional[SystemInfoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    collected_objects: Optional[CollectedObjectsType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    system_data: Optional[SystemDataType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )

    @classmethod
    def load(cls, file):
        with open(file, "rb") as fp:
            system_characteristics = scap_parser.parse(fp, cls)
        return system_characteristics

    @classmethod
    def load_json(cls, file):
        with open(file, "rb") as fp:
            system_characteristics = scap_json_parser.parse(fp, cls)
        return system_characteristics

    def dump(self, file):
        with open(file, "w", encoding="utf8") as fp:
            scap_serializer.write(fp, self)

    def dump_json(self, file):
        with open(file, "w", encoding="utf8") as fp:
            scap_json_serializer.write(fp, self)
