from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional


@dataclass
class AddressLine:
    """Free format address representation.

    An address can have more than one line. The order of the AddressLine
    elements must be preserved.

    :ivar content:
    :ivar type: Defines the type of address line. eg. Street, Address
        Line 1, etc.
    :ivar code: Used by postal services to encode the name of the
        element.
    :ivar other_attributes:
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class BuildingNameType:
    """
    :ivar content:
    :ivar type:
    :ivar type_occurrence: Occurrence of the building name before/after
        the type. eg. EGIS BUILDING where name appears before type
    :ivar code: Used by postal services to encode the name of the
        element.
    :ivar other_attributes:
    """
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    type_occurrence: Optional["BuildingNameType.TypeOccurrence"] = field(
        default=None,
        metadata={
            "name": "TypeOccurrence",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )

    class TypeOccurrence(Enum):
        BEFORE = "Before"
        AFTER = "After"


@dataclass
class CountryName:
    """
    Specification of the name of a country.

    :ivar content:
    :ivar type: Old name, new name, etc
    :ivar code: Used by postal services to encode the name of the
        element.
    :ivar other_attributes:
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class PremiseNumber:
    """Specification of the identifier of the premise (house, building, etc).

    Premises in a street are often uniquely identified by means of
    consecutive identifiers. The identifier can be a number, a letter or
    any combination of the two.

    :ivar content:
    :ivar number_type: Building 12-14 is "Range" and Building 12 is
        "Single"
    :ivar type:
    :ivar indicator: No. in House No.12, # in #12, etc.
    :ivar indicator_occurrence: No. occurs before 12 No.12
    :ivar number_type_occurrence: 12 in BUILDING 12 occurs "after"
        premise type BUILDING
    :ivar code: Used by postal services to encode the name of the
        element.
    :ivar other_attributes:
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    number_type: Optional["PremiseNumber.NumberType"] = field(
        default=None,
        metadata={
            "name": "NumberType",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Indicator",
            "type": "Attribute",
        }
    )
    indicator_occurrence: Optional["PremiseNumber.IndicatorOccurrence"] = field(
        default=None,
        metadata={
            "name": "IndicatorOccurrence",
            "type": "Attribute",
        }
    )
    number_type_occurrence: Optional["PremiseNumber.NumberTypeOccurrence"] = field(
        default=None,
        metadata={
            "name": "NumberTypeOccurrence",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )

    class NumberType(Enum):
        SINGLE = "Single"
        RANGE = "Range"

    class IndicatorOccurrence(Enum):
        BEFORE = "Before"
        AFTER = "After"

    class NumberTypeOccurrence(Enum):
        BEFORE = "Before"
        AFTER = "After"


@dataclass
class PremiseNumberPrefix:
    """
    A in A12.

    :ivar value:
    :ivar number_prefix_separator: A-12 where 12 is number and A is
        prefix and "-" is the separator
    :ivar type:
    :ivar code: Used by postal services to encode the name of the
        element.
    :ivar other_attributes:
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"

    value: Optional[str] = field(
        default=None,
    )
    number_prefix_separator: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumberPrefixSeparator",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class PremiseNumberSuffix:
    """
    A in 12A.

    :ivar content:
    :ivar number_suffix_separator: 12-A where 12 is number and A is
        suffix and "-" is the separator
    :ivar type:
    :ivar code: Used by postal services to encode the name of the
        element.
    :ivar other_attributes:
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    number_suffix_separator: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumberSuffixSeparator",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class ThoroughfareLeadingTypeType:
    """
    :ivar content:
    :ivar type:
    :ivar code: Used by postal services to encode the name of the
        element.
    :ivar other_attributes:
    """
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class ThoroughfareNameType:
    """
    :ivar content:
    :ivar type:
    :ivar code: Used by postal services to encode the name of the
        element.
    :ivar other_attributes:
    """
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class ThoroughfareNumber:
    """Eg.: 23 Archer street or 25/15 Zero Avenue, etc

    :ivar content:
    :ivar number_type: 12 Archer Street is "Single" and 12-14 Archer
        Street is "Range"
    :ivar type:
    :ivar indicator: No. in Street No.12 or "#" in Street # 12, etc.
    :ivar indicator_occurrence: No.12 where "No." is before actual
        street number
    :ivar number_occurrence: 23 Archer St, Archer Street 23, St Archer
        23
    :ivar code: Used by postal services to encode the name of the
        element.
    :ivar other_attributes:
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    number_type: Optional["ThoroughfareNumber.NumberType"] = field(
        default=None,
        metadata={
            "name": "NumberType",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Indicator",
            "type": "Attribute",
        }
    )
    indicator_occurrence: Optional["ThoroughfareNumber.IndicatorOccurrence"] = field(
        default=None,
        metadata={
            "name": "IndicatorOccurrence",
            "type": "Attribute",
        }
    )
    number_occurrence: Optional["ThoroughfareNumber.NumberOccurrence"] = field(
        default=None,
        metadata={
            "name": "NumberOccurrence",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )

    class NumberType(Enum):
        SINGLE = "Single"
        RANGE = "Range"

    class IndicatorOccurrence(Enum):
        BEFORE = "Before"
        AFTER = "After"

    class NumberOccurrence(Enum):
        BEFORE_NAME = "BeforeName"
        AFTER_NAME = "AfterName"
        BEFORE_TYPE = "BeforeType"
        AFTER_TYPE = "AfterType"


@dataclass
class ThoroughfareNumberPrefix:
    """Prefix before the number.

    A in A12 Archer Street

    :ivar content:
    :ivar number_prefix_separator:
    :ivar type:
    :ivar code: Used by postal services to encode the name of the
        element.
    :ivar other_attributes:
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    number_prefix_separator: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumberPrefixSeparator",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class ThoroughfareNumberSuffix:
    """Suffix after the number.

    A in 12A Archer Street

    :ivar content:
    :ivar number_suffix_separator: NEAR, ADJACENT TO, etc 12-A where 12
        is number and A is suffix and "-" is the separator
    :ivar type:
    :ivar code: Used by postal services to encode the name of the
        element.
    :ivar other_attributes:
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    number_suffix_separator: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumberSuffixSeparator",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class ThoroughfarePostDirectionType:
    """
    :ivar content:
    :ivar type:
    :ivar code: Used by postal services to encode the name of the
        element.
    :ivar other_attributes:
    """
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class ThoroughfarePreDirectionType:
    """
    :ivar content:
    :ivar type:
    :ivar code: Used by postal services to encode the name of the
        element.
    :ivar other_attributes:
    """
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class ThoroughfareTrailingTypeType:
    """
    :ivar content:
    :ivar type:
    :ivar code: Used by postal services to encode the name of the
        element.
    :ivar other_attributes:
    """
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class AddressLinesType:
    address_line: List[AddressLine] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
            "min_occurs": 1,
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class MailStopType:
    """
    :ivar address_line:
    :ivar mail_stop_name: Name of the the Mail Stop. eg. MSP, MS, etc
    :ivar mail_stop_number: Number of the Mail stop. eg. 123 in MS 123
    :ivar other_element:
    :ivar type:
    :ivar other_attributes:
    """
    address_line: List[AddressLine] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    mail_stop_name: Optional["MailStopType.MailStopName"] = field(
        default=None,
        metadata={
            "name": "MailStopName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    mail_stop_number: Optional["MailStopType.MailStopNumber"] = field(
        default=None,
        metadata={
            "name": "MailStopNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )

    @dataclass
    class MailStopName:
        """
        :ivar content:
        :ivar type:
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class MailStopNumber:
        """
        :ivar content:
        :ivar name_number_separator: "-" in MS-123
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        name_number_separator: Optional[str] = field(
            default=None,
            metadata={
                "name": "NameNumberSeparator",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )


@dataclass
class PostalCode:
    """PostalCode is the container element for either simple or complex
    (extended) postal codes.

    Type: Area Code, Postcode, etc.

    :ivar address_line:
    :ivar postal_code_number: Specification of a postcode. The postcode
        is formatted according to country-specific rules. Example: SW3
        0A8-1A, 600074, 2067
    :ivar postal_code_number_extension: Examples are: 1234 (USA), 1G
        (UK), etc.
    :ivar post_town: A post town is not the same as a locality. A post
        town can encompass a collection of (small) localities. It can
        also be a subpart of a locality. An actual post town in Norway
        is "Bergen".
    :ivar other_element:
    :ivar type: Area Code, Postcode, Delivery code as in NZ, etc
    :ivar other_attributes:
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"

    address_line: List[AddressLine] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
        }
    )
    postal_code_number: List["PostalCode.PostalCodeNumber"] = field(
        default_factory=list,
        metadata={
            "name": "PostalCodeNumber",
            "type": "Element",
        }
    )
    postal_code_number_extension: List["PostalCode.PostalCodeNumberExtension"] = field(
        default_factory=list,
        metadata={
            "name": "PostalCodeNumberExtension",
            "type": "Element",
        }
    )
    post_town: Optional["PostalCode.PostTown"] = field(
        default=None,
        metadata={
            "name": "PostTown",
            "type": "Element",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )

    @dataclass
    class PostalCodeNumber:
        """
        :ivar content:
        :ivar type: Old Postal Code, new code, etc
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class PostalCodeNumberExtension:
        """
        :ivar content:
        :ivar type: Delivery Point Suffix, New Postal Code, etc..
        :ivar number_extension_separator: The separator between postal
            code number and the extension. Eg. "-"
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        number_extension_separator: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumberExtensionSeparator",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class PostTown:
        """
        :ivar address_line:
        :ivar post_town_name: Name of the post town
        :ivar post_town_suffix: GENERAL PO in MIAMI GENERAL PO
        :ivar type: eg. village, town, suburb, etc
        :ivar other_attributes:
        """
        address_line: List[AddressLine] = field(
            default_factory=list,
            metadata={
                "name": "AddressLine",
                "type": "Element",
            }
        )
        post_town_name: List["PostalCode.PostTown.PostTownName"] = field(
            default_factory=list,
            metadata={
                "name": "PostTownName",
                "type": "Element",
            }
        )
        post_town_suffix: Optional["PostalCode.PostTown.PostTownSuffix"] = field(
            default=None,
            metadata={
                "name": "PostTownSuffix",
                "type": "Element",
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

        @dataclass
        class PostTownName:
            """
            :ivar content:
            :ivar type:
            :ivar code: Used by postal services to encode the name of
                the element.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class PostTownSuffix:
            """
            :ivar content:
            :ivar code: Used by postal services to encode the name of
                the element.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )


@dataclass
class Department:
    """
    Subdivision in the firm: School of Physics at Victoria University (School
    of Physics is the department)

    :ivar address_line:
    :ivar department_name: Specification of the name of a department.
    :ivar mail_stop: A MailStop is where the the mail is delivered to
        within a premise/subpremise/firm or a facility.
    :ivar postal_code:
    :ivar other_element:
    :ivar type: School in Physics School, Division in Radiology division
        of school of physics
    :ivar other_attributes:
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"

    address_line: List[AddressLine] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
        }
    )
    department_name: List["Department.DepartmentName"] = field(
        default_factory=list,
        metadata={
            "name": "DepartmentName",
            "type": "Element",
        }
    )
    mail_stop: Optional[MailStopType] = field(
        default=None,
        metadata={
            "name": "MailStop",
            "type": "Element",
        }
    )
    postal_code: Optional[PostalCode] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )

    @dataclass
    class DepartmentName:
        """
        :ivar content:
        :ivar type:
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )


@dataclass
class FirmType:
    """
    :ivar address_line:
    :ivar firm_name: Name of the firm
    :ivar department:
    :ivar mail_stop: A MailStop is where the the mail is delivered to
        within a premise/subpremise/firm or a facility.
    :ivar postal_code:
    :ivar other_element:
    :ivar type:
    :ivar other_attributes:
    """
    address_line: List[AddressLine] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    firm_name: List["FirmType.FirmName"] = field(
        default_factory=list,
        metadata={
            "name": "FirmName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    department: List[Department] = field(
        default_factory=list,
        metadata={
            "name": "Department",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    mail_stop: Optional[MailStopType] = field(
        default=None,
        metadata={
            "name": "MailStop",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    postal_code: Optional[PostalCode] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )

    @dataclass
    class FirmName:
        """
        :ivar content:
        :ivar type:
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )


@dataclass
class PostBox:
    """Specification of a postbox like mail delivery point.

    Only a single postbox number can be specified. Examples of postboxes
    are POBox, free mail numbers, etc.

    :ivar address_line:
    :ivar post_box_number: Specification of the number of a postbox
    :ivar post_box_number_prefix: Specification of the prefix of the
        post box number. eg. A in POBox:A-123
    :ivar post_box_number_suffix: Specification of the suffix of the
        post box number. eg. A in POBox:123A
    :ivar post_box_number_extension: Some countries like USA have POBox
        as 12345-123
    :ivar firm: Specification of a firm, company, organization, etc. It
        can be specified as part of an address that contains a street or
        a postbox. It is therefore different from  a large mail user
        address, which contains no street.
    :ivar postal_code:
    :ivar other_element:
    :ivar type: Possible values are, not limited to: POBox and Freepost.
    :ivar indicator: LOCKED BAG NO:1234 where the Indicator is NO: and
        Type is LOCKED BAG
    :ivar other_attributes:
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"

    address_line: List[AddressLine] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
        }
    )
    post_box_number: Optional["PostBox.PostBoxNumber"] = field(
        default=None,
        metadata={
            "name": "PostBoxNumber",
            "type": "Element",
            "required": True,
        }
    )
    post_box_number_prefix: Optional["PostBox.PostBoxNumberPrefix"] = field(
        default=None,
        metadata={
            "name": "PostBoxNumberPrefix",
            "type": "Element",
        }
    )
    post_box_number_suffix: Optional["PostBox.PostBoxNumberSuffix"] = field(
        default=None,
        metadata={
            "name": "PostBoxNumberSuffix",
            "type": "Element",
        }
    )
    post_box_number_extension: Optional["PostBox.PostBoxNumberExtension"] = field(
        default=None,
        metadata={
            "name": "PostBoxNumberExtension",
            "type": "Element",
        }
    )
    firm: Optional[FirmType] = field(
        default=None,
        metadata={
            "name": "Firm",
            "type": "Element",
        }
    )
    postal_code: Optional[PostalCode] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Indicator",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )

    @dataclass
    class PostBoxNumber:
        """
        :ivar content:
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class PostBoxNumberPrefix:
        """
        :ivar content:
        :ivar number_prefix_separator: A-12 where 12 is number and A is
            prefix and "-" is the separator
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        number_prefix_separator: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumberPrefixSeparator",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class PostBoxNumberSuffix:
        """
        :ivar content:
        :ivar number_suffix_separator: 12-A where 12 is number and A is
            suffix and "-" is the separator
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        number_suffix_separator: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumberSuffixSeparator",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class PostBoxNumberExtension:
        """
        :ivar content:
        :ivar number_extension_separator: "-" is the
            NumberExtensionSeparator in POBOX:12345-123
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        number_extension_separator: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumberExtensionSeparator",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )


@dataclass
class SubPremiseType:
    """
    :ivar address_line:
    :ivar sub_premise_name: Name of the SubPremise
    :ivar sub_premise_location: Name of the SubPremise Location. eg.
        LOBBY, BASEMENT, GROUND FLOOR, etc...
    :ivar sub_premise_number: Specification of the identifier of a sub-
        premise. Examples of sub-premises are apartments and suites.
        sub-premises in a building are often uniquely identified by
        means of consecutive identifiers. The identifier can be a
        number, a letter or any combination of the two. In the latter
        case, the identifier includes exactly one variable (range) part,
        which is either a  number or a single letter that is surrounded
        by fixed parts at the left (prefix) or the right (postfix).
    :ivar sub_premise_number_prefix: Prefix of the sub premise number.
        eg. A in A-12
    :ivar sub_premise_number_suffix: Suffix of the sub premise number.
        eg. A in 12A
    :ivar building_name: Name of the building
    :ivar firm: Specification of a firm, company, organization, etc. It
        can be specified as part of an address that contains a street or
        a postbox. It is therefore different from a large mail user
        address, which contains no street.
    :ivar mail_stop: A MailStop is where the the mail is delivered to
        within a premise/subpremise/firm or a facility.
    :ivar postal_code:
    :ivar sub_premise: Specification of a single sub-premise. Examples
        of sub-premises are apartments and suites.  Each sub-premise
        should be uniquely identifiable. SubPremiseType: Specification
        of the name of a sub-premise type. Possible values not limited
        to: Suite, Appartment, Floor, Unknown Multiple levels within a
        premise by recursively calling SubPremise Eg. Level 4, Suite 2,
        Block C
    :ivar other_element:
    :ivar type:
    :ivar other_attributes:
    """
    address_line: List[AddressLine] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    sub_premise_name: List["SubPremiseType.SubPremiseName"] = field(
        default_factory=list,
        metadata={
            "name": "SubPremiseName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    sub_premise_location: Optional["SubPremiseType.SubPremiseLocation"] = field(
        default=None,
        metadata={
            "name": "SubPremiseLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    sub_premise_number: List["SubPremiseType.SubPremiseNumber"] = field(
        default_factory=list,
        metadata={
            "name": "SubPremiseNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    sub_premise_number_prefix: List["SubPremiseType.SubPremiseNumberPrefix"] = field(
        default_factory=list,
        metadata={
            "name": "SubPremiseNumberPrefix",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    sub_premise_number_suffix: List["SubPremiseType.SubPremiseNumberSuffix"] = field(
        default_factory=list,
        metadata={
            "name": "SubPremiseNumberSuffix",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    building_name: List[BuildingNameType] = field(
        default_factory=list,
        metadata={
            "name": "BuildingName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    firm: Optional[FirmType] = field(
        default=None,
        metadata={
            "name": "Firm",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    mail_stop: Optional[MailStopType] = field(
        default=None,
        metadata={
            "name": "MailStop",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    postal_code: Optional[PostalCode] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    sub_premise: Optional["SubPremiseType"] = field(
        default=None,
        metadata={
            "name": "SubPremise",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )

    @dataclass
    class SubPremiseName:
        """
        :ivar content:
        :ivar type:
        :ivar type_occurrence: EGIS Building where EGIS occurs before
            Building
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        type_occurrence: Optional["SubPremiseType.SubPremiseName.TypeOccurrence"] = field(
            default=None,
            metadata={
                "name": "TypeOccurrence",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

        class TypeOccurrence(Enum):
            BEFORE = "Before"
            AFTER = "After"

    @dataclass
    class SubPremiseNumberPrefix:
        """
        :ivar content:
        :ivar number_prefix_separator: A-12 where 12 is number and A is
            prefix and "-" is the separator
        :ivar type:
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        number_prefix_separator: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumberPrefixSeparator",
                "type": "Attribute",
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class SubPremiseNumberSuffix:
        """
        :ivar content:
        :ivar number_suffix_separator: 12-A where 12 is number and A is
            suffix and "-" is the separator
        :ivar type:
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        number_suffix_separator: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumberSuffixSeparator",
                "type": "Attribute",
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class SubPremiseLocation:
        """
        :ivar content:
        :ivar code: Used by postal services to encode the name of the
            element.
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )

    @dataclass
    class SubPremiseNumber:
        """
        :ivar content:
        :ivar indicator: "TH" in 12TH which is a floor number, "NO." in
            NO.1, "#" in APT #12, etc.
        :ivar indicator_occurrence: "No." occurs before 1 in No.1, or TH
            occurs after 12 in 12TH
        :ivar number_type_occurrence: 12TH occurs "before" FLOOR (a type
            of subpremise) in 12TH FLOOR
        :ivar premise_number_separator: "/" in 12/14 Archer Street where
            12 is sub-premise number and 14 is premise number
        :ivar type:
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        indicator: Optional[str] = field(
            default=None,
            metadata={
                "name": "Indicator",
                "type": "Attribute",
            }
        )
        indicator_occurrence: Optional["SubPremiseType.SubPremiseNumber.IndicatorOccurrence"] = field(
            default=None,
            metadata={
                "name": "IndicatorOccurrence",
                "type": "Attribute",
            }
        )
        number_type_occurrence: Optional["SubPremiseType.SubPremiseNumber.NumberTypeOccurrence"] = field(
            default=None,
            metadata={
                "name": "NumberTypeOccurrence",
                "type": "Attribute",
            }
        )
        premise_number_separator: Optional[str] = field(
            default=None,
            metadata={
                "name": "PremiseNumberSeparator",
                "type": "Attribute",
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

        class IndicatorOccurrence(Enum):
            BEFORE = "Before"
            AFTER = "After"

        class NumberTypeOccurrence(Enum):
            BEFORE = "Before"
            AFTER = "After"


@dataclass
class PostalRouteType:
    """
    :ivar address_line:
    :ivar postal_route_name: Name of the Postal Route
    :ivar postal_route_number: Number of the Postal Route
    :ivar post_box:
    :ivar other_element:
    :ivar type:
    :ivar other_attributes:
    """
    address_line: List[AddressLine] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    postal_route_name: List["PostalRouteType.PostalRouteName"] = field(
        default_factory=list,
        metadata={
            "name": "PostalRouteName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    postal_route_number: Optional["PostalRouteType.PostalRouteNumber"] = field(
        default=None,
        metadata={
            "name": "PostalRouteNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    post_box: Optional[PostBox] = field(
        default=None,
        metadata={
            "name": "PostBox",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )

    @dataclass
    class PostalRouteName:
        """
        :ivar content:
        :ivar type:
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class PostalRouteNumber:
        """
        :ivar content:
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )


@dataclass
class Premise:
    """Specification of a single premise, for example a house or a building.

    The premise as a whole has a unique premise (house) number or a
    premise name.  There could be more than one premise in a street
    referenced in an address. For example a building address near a
    major shopping centre or raiwlay station

    :ivar address_line:
    :ivar premise_name: Specification of the name of the premise (house,
        building, park, farm, etc). A premise name is specified when the
        premise cannot be addressed using a street name plus premise
        (house) number.
    :ivar premise_location: LOBBY, BASEMENT, GROUND FLOOR, etc...
    :ivar premise_number:
    :ivar premise_number_range: Specification for defining the premise
        number range. Some premises have number as Building C1-C7
    :ivar premise_number_prefix:
    :ivar premise_number_suffix:
    :ivar building_name: Specification of the name of a building.
    :ivar sub_premise: Specification of a single sub-premise. Examples
        of sub-premises are apartments and suites. Each sub-premise
        should be uniquely identifiable.
    :ivar firm: Specification of a firm, company, organization, etc. It
        can be specified as part of an address that contains a street or
        a postbox. It is therefore different from a large mail user
        address, which contains no street.
    :ivar mail_stop: A MailStop is where the the mail is delivered to
        within a premise/subpremise/firm or a facility.
    :ivar postal_code:
    :ivar premise:
    :ivar other_element:
    :ivar type: COMPLEXE in COMPLEX DES JARDINS, A building, station,
        etc
    :ivar premise_dependency: STREET, PREMISE, SUBPREMISE, PARK, FARM,
        etc
    :ivar premise_dependency_type: NEAR, ADJACENT TO, etc
    :ivar premise_thoroughfare_connector: DES, DE, LA, LA, DU in RUE DU
        BOIS. These terms connect a premise/thoroughfare type and
        premise/thoroughfare name. Terms may appear with names AVE DU
        BOIS
    :ivar other_attributes:
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"

    address_line: List[AddressLine] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
        }
    )
    premise_name: List["Premise.PremiseName"] = field(
        default_factory=list,
        metadata={
            "name": "PremiseName",
            "type": "Element",
        }
    )
    premise_location: Optional["Premise.PremiseLocation"] = field(
        default=None,
        metadata={
            "name": "PremiseLocation",
            "type": "Element",
        }
    )
    premise_number: List[PremiseNumber] = field(
        default_factory=list,
        metadata={
            "name": "PremiseNumber",
            "type": "Element",
        }
    )
    premise_number_range: Optional["Premise.PremiseNumberRange"] = field(
        default=None,
        metadata={
            "name": "PremiseNumberRange",
            "type": "Element",
        }
    )
    premise_number_prefix: List[PremiseNumberPrefix] = field(
        default_factory=list,
        metadata={
            "name": "PremiseNumberPrefix",
            "type": "Element",
        }
    )
    premise_number_suffix: List[PremiseNumberSuffix] = field(
        default_factory=list,
        metadata={
            "name": "PremiseNumberSuffix",
            "type": "Element",
        }
    )
    building_name: List[BuildingNameType] = field(
        default_factory=list,
        metadata={
            "name": "BuildingName",
            "type": "Element",
        }
    )
    sub_premise: List[SubPremiseType] = field(
        default_factory=list,
        metadata={
            "name": "SubPremise",
            "type": "Element",
        }
    )
    firm: Optional[FirmType] = field(
        default=None,
        metadata={
            "name": "Firm",
            "type": "Element",
        }
    )
    mail_stop: Optional[MailStopType] = field(
        default=None,
        metadata={
            "name": "MailStop",
            "type": "Element",
        }
    )
    postal_code: Optional[PostalCode] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
        }
    )
    premise: Optional["Premise"] = field(
        default=None,
        metadata={
            "name": "Premise",
            "type": "Element",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    premise_dependency: Optional[str] = field(
        default=None,
        metadata={
            "name": "PremiseDependency",
            "type": "Attribute",
        }
    )
    premise_dependency_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "PremiseDependencyType",
            "type": "Attribute",
        }
    )
    premise_thoroughfare_connector: Optional[str] = field(
        default=None,
        metadata={
            "name": "PremiseThoroughfareConnector",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )

    @dataclass
    class PremiseName:
        """
        :ivar content:
        :ivar type:
        :ivar type_occurrence: EGIS Building where EGIS occurs before
            Building, DES JARDINS occurs after COMPLEXE DES JARDINS
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        type_occurrence: Optional["Premise.PremiseName.TypeOccurrence"] = field(
            default=None,
            metadata={
                "name": "TypeOccurrence",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

        class TypeOccurrence(Enum):
            BEFORE = "Before"
            AFTER = "After"

    @dataclass
    class PremiseLocation:
        """
        :ivar content:
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class PremiseNumberRange:
        """
        :ivar premise_number_range_from: Start number details of the
            premise number range
        :ivar premise_number_range_to: End number details of the premise
            number range
        :ivar range_type: Eg. Odd or even number range
        :ivar indicator: Eg. No. in Building No:C1-C5
        :ivar separator: "-" in 12-14  or "Thru" in 12 Thru 14 etc.
        :ivar type:
        :ivar indicator_occurence: No.12-14 where "No." is before actual
            street number
        :ivar number_range_occurence: Building 23-25 where the number
            occurs after building name
        """
        premise_number_range_from: Optional["Premise.PremiseNumberRange.PremiseNumberRangeFrom"] = field(
            default=None,
            metadata={
                "name": "PremiseNumberRangeFrom",
                "type": "Element",
                "required": True,
            }
        )
        premise_number_range_to: Optional["Premise.PremiseNumberRange.PremiseNumberRangeTo"] = field(
            default=None,
            metadata={
                "name": "PremiseNumberRangeTo",
                "type": "Element",
                "required": True,
            }
        )
        range_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "RangeType",
                "type": "Attribute",
            }
        )
        indicator: Optional[str] = field(
            default=None,
            metadata={
                "name": "Indicator",
                "type": "Attribute",
            }
        )
        separator: Optional[str] = field(
            default=None,
            metadata={
                "name": "Separator",
                "type": "Attribute",
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        indicator_occurence: Optional["Premise.PremiseNumberRange.IndicatorOccurence"] = field(
            default=None,
            metadata={
                "name": "IndicatorOccurence",
                "type": "Attribute",
            }
        )
        number_range_occurence: Optional["Premise.PremiseNumberRange.NumberRangeOccurence"] = field(
            default=None,
            metadata={
                "name": "NumberRangeOccurence",
                "type": "Attribute",
            }
        )

        @dataclass
        class PremiseNumberRangeFrom:
            address_line: List[AddressLine] = field(
                default_factory=list,
                metadata={
                    "name": "AddressLine",
                    "type": "Element",
                }
            )
            premise_number_prefix: List[PremiseNumberPrefix] = field(
                default_factory=list,
                metadata={
                    "name": "PremiseNumberPrefix",
                    "type": "Element",
                }
            )
            premise_number: List[PremiseNumber] = field(
                default_factory=list,
                metadata={
                    "name": "PremiseNumber",
                    "type": "Element",
                    "min_occurs": 1,
                }
            )
            premise_number_suffix: List[PremiseNumberSuffix] = field(
                default_factory=list,
                metadata={
                    "name": "PremiseNumberSuffix",
                    "type": "Element",
                }
            )

        @dataclass
        class PremiseNumberRangeTo:
            address_line: List[AddressLine] = field(
                default_factory=list,
                metadata={
                    "name": "AddressLine",
                    "type": "Element",
                }
            )
            premise_number_prefix: List[PremiseNumberPrefix] = field(
                default_factory=list,
                metadata={
                    "name": "PremiseNumberPrefix",
                    "type": "Element",
                }
            )
            premise_number: List[PremiseNumber] = field(
                default_factory=list,
                metadata={
                    "name": "PremiseNumber",
                    "type": "Element",
                    "min_occurs": 1,
                }
            )
            premise_number_suffix: List[PremiseNumberSuffix] = field(
                default_factory=list,
                metadata={
                    "name": "PremiseNumberSuffix",
                    "type": "Element",
                }
            )

        class IndicatorOccurence(Enum):
            BEFORE = "Before"
            AFTER = "After"

        class NumberRangeOccurence(Enum):
            BEFORE_NAME = "BeforeName"
            AFTER_NAME = "AfterName"
            BEFORE_TYPE = "BeforeType"
            AFTER_TYPE = "AfterType"


@dataclass
class PostOffice:
    """Specification of a post office.

    Examples are a rural post office where post is delivered and a post
    office containing post office boxes.

    :ivar address_line:
    :ivar post_office_name: Specification of the name of the post
        office. This can be a rural postoffice where post is delivered
        or a post office containing post office boxes.
    :ivar post_office_number: Specification of the number of the
        postoffice. Common in rural postoffices
    :ivar postal_route: A Postal van is specific for a route as in
        Is`rael, Rural route
    :ivar post_box:
    :ivar postal_code:
    :ivar other_element:
    :ivar type: Could be a Mobile Postoffice Van as in Isreal
    :ivar indicator: eg. Kottivakkam (P.O) here (P.O) is the Indicator
    :ivar other_attributes:
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"

    address_line: List[AddressLine] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
        }
    )
    post_office_name: List["PostOffice.PostOfficeName"] = field(
        default_factory=list,
        metadata={
            "name": "PostOfficeName",
            "type": "Element",
        }
    )
    post_office_number: Optional["PostOffice.PostOfficeNumber"] = field(
        default=None,
        metadata={
            "name": "PostOfficeNumber",
            "type": "Element",
        }
    )
    postal_route: Optional[PostalRouteType] = field(
        default=None,
        metadata={
            "name": "PostalRoute",
            "type": "Element",
        }
    )
    post_box: Optional[PostBox] = field(
        default=None,
        metadata={
            "name": "PostBox",
            "type": "Element",
        }
    )
    postal_code: Optional[PostalCode] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Indicator",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )

    @dataclass
    class PostOfficeName:
        """
        :ivar content:
        :ivar type:
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class PostOfficeNumber:
        """
        :ivar content:
        :ivar indicator: MS in MS 62, # in MS # 12, etc.
        :ivar indicator_occurrence: MS occurs before 62 in MS 62
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        indicator: Optional[str] = field(
            default=None,
            metadata={
                "name": "Indicator",
                "type": "Attribute",
            }
        )
        indicator_occurrence: Optional["PostOffice.PostOfficeNumber.IndicatorOccurrence"] = field(
            default=None,
            metadata={
                "name": "IndicatorOccurrence",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

        class IndicatorOccurrence(Enum):
            BEFORE = "Before"
            AFTER = "After"


@dataclass
class DependentLocalityType:
    """
    :ivar address_line:
    :ivar dependent_locality_name: Name of the dependent locality
    :ivar dependent_locality_number: Number of the dependent locality.
        Some areas are numbered. Eg. SECTOR 5 in a Suburb as in India or
        SOI SUKUMVIT 10 as in Thailand
    :ivar post_box:
    :ivar large_mail_user: Specification of a large mail user address.
        Examples of large mail users are postal companies, companies in
        France with a cedex number, hospitals and airports with their
        own post code. Large mail user addresses do not have a street
        name with premise name or premise number in countries like
        Netherlands. But they have a POBox and street also in countries
        like France
    :ivar post_office:
    :ivar postal_route: A Postal van is specific for a route as in
        Is`rael, Rural route
    :ivar thoroughfare:
    :ivar premise:
    :ivar dependent_locality: Dependent localities are Districts within
        cities/towns, locality divisions, postal  divisions of cities,
        suburbs, etc. DependentLocality is a recursive element, but no
        nesting deeper than two exists (Locality-DependentLocality-
        DependentLocality).
    :ivar postal_code:
    :ivar other_element:
    :ivar type: City or IndustrialEstate, etc
    :ivar usage_type: Postal or Political - Sometimes locations must be
        distinguished between postal system, and physical locations as
        defined by a political system
    :ivar connector: "VIA" as in Hill Top VIA Parish where Parish is a
        locality and Hill Top is a dependent locality
    :ivar indicator: Eg. Erode (Dist) where (Dist) is the Indicator
    :ivar other_attributes:
    """
    address_line: List[AddressLine] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    dependent_locality_name: List["DependentLocalityType.DependentLocalityName"] = field(
        default_factory=list,
        metadata={
            "name": "DependentLocalityName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    dependent_locality_number: Optional["DependentLocalityType.DependentLocalityNumber"] = field(
        default=None,
        metadata={
            "name": "DependentLocalityNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    post_box: Optional[PostBox] = field(
        default=None,
        metadata={
            "name": "PostBox",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    large_mail_user: Optional["LargeMailUserType"] = field(
        default=None,
        metadata={
            "name": "LargeMailUser",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    post_office: Optional[PostOffice] = field(
        default=None,
        metadata={
            "name": "PostOffice",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    postal_route: Optional[PostalRouteType] = field(
        default=None,
        metadata={
            "name": "PostalRoute",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    thoroughfare: Optional["Thoroughfare"] = field(
        default=None,
        metadata={
            "name": "Thoroughfare",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    premise: Optional[Premise] = field(
        default=None,
        metadata={
            "name": "Premise",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    dependent_locality: Optional["DependentLocalityType"] = field(
        default=None,
        metadata={
            "name": "DependentLocality",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    postal_code: Optional[PostalCode] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    usage_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsageType",
            "type": "Attribute",
        }
    )
    connector: Optional[str] = field(
        default=None,
        metadata={
            "name": "Connector",
            "type": "Attribute",
        }
    )
    indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Indicator",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )

    @dataclass
    class DependentLocalityName:
        """
        :ivar content:
        :ivar type:
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class DependentLocalityNumber:
        """
        :ivar content:
        :ivar name_number_occurrence: Eg. SECTOR occurs before 5 in
            SECTOR 5
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        name_number_occurrence: Optional["DependentLocalityType.DependentLocalityNumber.NameNumberOccurrence"] = field(
            default=None,
            metadata={
                "name": "NameNumberOccurrence",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

        class NameNumberOccurrence(Enum):
            BEFORE = "Before"
            AFTER = "After"


@dataclass
class Thoroughfare:
    """Specification of a thoroughfare.

    A thoroughfare could be a rd, street, canal, river, etc.  Note
    dependentlocality in a street. For example, in some countries, a
    large street will have many subdivisions with numbers. Normally the
    subdivision name is the same as the road name, but with a number to
    identifiy it. Eg. SOI SUKUMVIT 3, SUKUMVIT RD, BANGKOK

    :ivar address_line:
    :ivar thoroughfare_number:
    :ivar thoroughfare_number_range: A container to represent a range of
        numbers (from x thru y)for a thoroughfare. eg. 1-2 Albert Av
    :ivar thoroughfare_number_prefix:
    :ivar thoroughfare_number_suffix:
    :ivar thoroughfare_pre_direction: North Baker Street, where North is
        the pre-direction. The direction appears before the name.
    :ivar thoroughfare_leading_type: Appears before the thoroughfare
        name. Ed. Spanish: Avenida Aurora, where Avenida is the leading
        type / French: Rue Moliere, where Rue is the leading type.
    :ivar thoroughfare_name: Specification of the name of a Thoroughfare
        (also dependant street name): street name, canal name, etc.
    :ivar thoroughfare_trailing_type: Appears after the thoroughfare
        name. Ed. British: Baker Lane, where Lane is the trailing type.
    :ivar thoroughfare_post_direction: 221-bis Baker Street North, where
        North is the post-direction. The post-direction appears after
        the name.
    :ivar dependent_thoroughfare: DependentThroughfare is related to a
        street; occurs in GB, IE, ES, PT
    :ivar dependent_locality: Dependent localities are Districts within
        cities/towns, locality divisions, postal  divisions of cities,
        suburbs, etc. DependentLocality is a recursive element, but no
        nesting deeper than two exists (Locality-DependentLocality-
        DependentLocality).
    :ivar premise:
    :ivar firm: Specification of a firm, company, organization, etc. It
        can be specified as part of an address that contains a street or
        a postbox. It is therefore different from  a large mail user
        address, which contains no street.
    :ivar postal_code:
    :ivar other_element:
    :ivar type:
    :ivar dependent_thoroughfares: Does this thoroughfare have a a
        dependent thoroughfare? Corner of street X, etc
    :ivar dependent_thoroughfares_indicator: Corner of, Intersection of
    :ivar dependent_thoroughfares_connector: Corner of Street1 AND
        Street 2 where AND is the Connector
    :ivar dependent_thoroughfares_type: STS in GEORGE and ADELAIDE STS,
        RDS IN A and B RDS, etc. Use only when both the street types are
        the same
    :ivar other_attributes:
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"

    address_line: List[AddressLine] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
        }
    )
    thoroughfare_number: List[ThoroughfareNumber] = field(
        default_factory=list,
        metadata={
            "name": "ThoroughfareNumber",
            "type": "Element",
            "sequential": True,
        }
    )
    thoroughfare_number_range: List["Thoroughfare.ThoroughfareNumberRange"] = field(
        default_factory=list,
        metadata={
            "name": "ThoroughfareNumberRange",
            "type": "Element",
            "sequential": True,
        }
    )
    thoroughfare_number_prefix: List[ThoroughfareNumberPrefix] = field(
        default_factory=list,
        metadata={
            "name": "ThoroughfareNumberPrefix",
            "type": "Element",
        }
    )
    thoroughfare_number_suffix: List[ThoroughfareNumberSuffix] = field(
        default_factory=list,
        metadata={
            "name": "ThoroughfareNumberSuffix",
            "type": "Element",
        }
    )
    thoroughfare_pre_direction: Optional[ThoroughfarePreDirectionType] = field(
        default=None,
        metadata={
            "name": "ThoroughfarePreDirection",
            "type": "Element",
        }
    )
    thoroughfare_leading_type: Optional[ThoroughfareLeadingTypeType] = field(
        default=None,
        metadata={
            "name": "ThoroughfareLeadingType",
            "type": "Element",
        }
    )
    thoroughfare_name: List[ThoroughfareNameType] = field(
        default_factory=list,
        metadata={
            "name": "ThoroughfareName",
            "type": "Element",
        }
    )
    thoroughfare_trailing_type: Optional[ThoroughfareTrailingTypeType] = field(
        default=None,
        metadata={
            "name": "ThoroughfareTrailingType",
            "type": "Element",
        }
    )
    thoroughfare_post_direction: Optional[ThoroughfarePostDirectionType] = field(
        default=None,
        metadata={
            "name": "ThoroughfarePostDirection",
            "type": "Element",
        }
    )
    dependent_thoroughfare: Optional["Thoroughfare.DependentThoroughfare"] = field(
        default=None,
        metadata={
            "name": "DependentThoroughfare",
            "type": "Element",
        }
    )
    dependent_locality: Optional[DependentLocalityType] = field(
        default=None,
        metadata={
            "name": "DependentLocality",
            "type": "Element",
        }
    )
    premise: Optional[Premise] = field(
        default=None,
        metadata={
            "name": "Premise",
            "type": "Element",
        }
    )
    firm: Optional[FirmType] = field(
        default=None,
        metadata={
            "name": "Firm",
            "type": "Element",
        }
    )
    postal_code: Optional[PostalCode] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    dependent_thoroughfares: Optional["Thoroughfare.DependentThoroughfares"] = field(
        default=None,
        metadata={
            "name": "DependentThoroughfares",
            "type": "Attribute",
        }
    )
    dependent_thoroughfares_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "DependentThoroughfaresIndicator",
            "type": "Attribute",
        }
    )
    dependent_thoroughfares_connector: Optional[str] = field(
        default=None,
        metadata={
            "name": "DependentThoroughfaresConnector",
            "type": "Attribute",
        }
    )
    dependent_thoroughfares_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "DependentThoroughfaresType",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )

    @dataclass
    class DependentThoroughfare:
        """
        :ivar address_line:
        :ivar thoroughfare_pre_direction: North Baker Street, where
            North is the pre-direction. The direction appears before the
            name.
        :ivar thoroughfare_leading_type: Appears before the thoroughfare
            name. Ed. Spanish: Avenida Aurora, where Avenida is the
            leading type / French: Rue Moliere, where Rue is the leading
            type.
        :ivar thoroughfare_name: Specification of the name of a
            Thoroughfare (also dependant street name): street name,
            canal name, etc.
        :ivar thoroughfare_trailing_type: Appears after the thoroughfare
            name. Ed. British: Baker Lane, where Lane is the trailing
            type.
        :ivar thoroughfare_post_direction: 221-bis Baker Street North,
            where North is the post-direction. The post-direction
            appears after the name.
        :ivar other_element:
        :ivar type:
        :ivar other_attributes:
        """
        address_line: List[AddressLine] = field(
            default_factory=list,
            metadata={
                "name": "AddressLine",
                "type": "Element",
            }
        )
        thoroughfare_pre_direction: Optional[ThoroughfarePreDirectionType] = field(
            default=None,
            metadata={
                "name": "ThoroughfarePreDirection",
                "type": "Element",
            }
        )
        thoroughfare_leading_type: Optional[ThoroughfareLeadingTypeType] = field(
            default=None,
            metadata={
                "name": "ThoroughfareLeadingType",
                "type": "Element",
            }
        )
        thoroughfare_name: List[ThoroughfareNameType] = field(
            default_factory=list,
            metadata={
                "name": "ThoroughfareName",
                "type": "Element",
            }
        )
        thoroughfare_trailing_type: Optional[ThoroughfareTrailingTypeType] = field(
            default=None,
            metadata={
                "name": "ThoroughfareTrailingType",
                "type": "Element",
            }
        )
        thoroughfare_post_direction: Optional[ThoroughfarePostDirectionType] = field(
            default=None,
            metadata={
                "name": "ThoroughfarePostDirection",
                "type": "Element",
            }
        )
        other_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class ThoroughfareNumberRange:
        """
        :ivar address_line:
        :ivar thoroughfare_number_from: Starting number in the range
        :ivar thoroughfare_number_to: Ending number in the range
        :ivar range_type: Thoroughfare number ranges are odd or even
        :ivar indicator: "No." No.12-13
        :ivar separator: "-" in 12-14  or "Thru" in 12 Thru 14 etc.
        :ivar indicator_occurrence: No.12-14 where "No." is before
            actual street number
        :ivar number_range_occurrence: 23-25 Archer St, where number
            appears before name
        :ivar type:
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        address_line: List[AddressLine] = field(
            default_factory=list,
            metadata={
                "name": "AddressLine",
                "type": "Element",
            }
        )
        thoroughfare_number_from: Optional["Thoroughfare.ThoroughfareNumberRange.ThoroughfareNumberFrom"] = field(
            default=None,
            metadata={
                "name": "ThoroughfareNumberFrom",
                "type": "Element",
                "required": True,
            }
        )
        thoroughfare_number_to: Optional["Thoroughfare.ThoroughfareNumberRange.ThoroughfareNumberTo"] = field(
            default=None,
            metadata={
                "name": "ThoroughfareNumberTo",
                "type": "Element",
                "required": True,
            }
        )
        range_type: Optional["Thoroughfare.ThoroughfareNumberRange.RangeType"] = field(
            default=None,
            metadata={
                "name": "RangeType",
                "type": "Attribute",
            }
        )
        indicator: Optional[str] = field(
            default=None,
            metadata={
                "name": "Indicator",
                "type": "Attribute",
            }
        )
        separator: Optional[str] = field(
            default=None,
            metadata={
                "name": "Separator",
                "type": "Attribute",
            }
        )
        indicator_occurrence: Optional["Thoroughfare.ThoroughfareNumberRange.IndicatorOccurrence"] = field(
            default=None,
            metadata={
                "name": "IndicatorOccurrence",
                "type": "Attribute",
            }
        )
        number_range_occurrence: Optional["Thoroughfare.ThoroughfareNumberRange.NumberRangeOccurrence"] = field(
            default=None,
            metadata={
                "name": "NumberRangeOccurrence",
                "type": "Attribute",
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

        @dataclass
        class ThoroughfareNumberFrom:
            """
            :ivar content:
            :ivar address_line:
            :ivar thoroughfare_number_prefix:
            :ivar thoroughfare_number:
            :ivar thoroughfare_number_suffix:
            :ivar code: Used by postal services to encode the name of
                the element.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            address_line: List[AddressLine] = field(
                default_factory=list,
                metadata={
                    "name": "AddressLine",
                    "type": "Element",
                }
            )
            thoroughfare_number_prefix: List[ThoroughfareNumberPrefix] = field(
                default_factory=list,
                metadata={
                    "name": "ThoroughfareNumberPrefix",
                    "type": "Element",
                }
            )
            thoroughfare_number: List[ThoroughfareNumber] = field(
                default_factory=list,
                metadata={
                    "name": "ThoroughfareNumber",
                    "type": "Element",
                    "min_occurs": 1,
                }
            )
            thoroughfare_number_suffix: List[ThoroughfareNumberSuffix] = field(
                default_factory=list,
                metadata={
                    "name": "ThoroughfareNumberSuffix",
                    "type": "Element",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class ThoroughfareNumberTo:
            """
            :ivar content:
            :ivar address_line:
            :ivar thoroughfare_number_prefix:
            :ivar thoroughfare_number:
            :ivar thoroughfare_number_suffix:
            :ivar code: Used by postal services to encode the name of
                the element.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            address_line: List[AddressLine] = field(
                default_factory=list,
                metadata={
                    "name": "AddressLine",
                    "type": "Element",
                }
            )
            thoroughfare_number_prefix: List[ThoroughfareNumberPrefix] = field(
                default_factory=list,
                metadata={
                    "name": "ThoroughfareNumberPrefix",
                    "type": "Element",
                }
            )
            thoroughfare_number: List[ThoroughfareNumber] = field(
                default_factory=list,
                metadata={
                    "name": "ThoroughfareNumber",
                    "type": "Element",
                    "min_occurs": 1,
                }
            )
            thoroughfare_number_suffix: List[ThoroughfareNumberSuffix] = field(
                default_factory=list,
                metadata={
                    "name": "ThoroughfareNumberSuffix",
                    "type": "Element",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        class RangeType(Enum):
            ODD = "Odd"
            EVEN = "Even"

        class IndicatorOccurrence(Enum):
            BEFORE = "Before"
            AFTER = "After"

        class NumberRangeOccurrence(Enum):
            BEFORE_NAME = "BeforeName"
            AFTER_NAME = "AfterName"
            BEFORE_TYPE = "BeforeType"
            AFTER_TYPE = "AfterType"

    class DependentThoroughfares(Enum):
        YES = "Yes"
        NO = "No"


@dataclass
class LargeMailUserType:
    """
    :ivar address_line:
    :ivar large_mail_user_name: Name of the large mail user. eg. Smith
        Ford International airport
    :ivar large_mail_user_identifier: Specification of the
        identification number of a large mail user. An example are the
        Cedex codes in France.
    :ivar building_name: Name of the building
    :ivar department:
    :ivar post_box:
    :ivar thoroughfare:
    :ivar postal_code:
    :ivar other_element:
    :ivar type:
    :ivar other_attributes:
    """
    address_line: List[AddressLine] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    large_mail_user_name: List["LargeMailUserType.LargeMailUserName"] = field(
        default_factory=list,
        metadata={
            "name": "LargeMailUserName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    large_mail_user_identifier: Optional["LargeMailUserType.LargeMailUserIdentifier"] = field(
        default=None,
        metadata={
            "name": "LargeMailUserIdentifier",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    building_name: List[BuildingNameType] = field(
        default_factory=list,
        metadata={
            "name": "BuildingName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    department: Optional[Department] = field(
        default=None,
        metadata={
            "name": "Department",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    post_box: Optional[PostBox] = field(
        default=None,
        metadata={
            "name": "PostBox",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    thoroughfare: Optional[Thoroughfare] = field(
        default=None,
        metadata={
            "name": "Thoroughfare",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    postal_code: Optional[PostalCode] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )

    @dataclass
    class LargeMailUserName:
        """
        :ivar content:
        :ivar type: Airport, Hospital, etc
        :ivar code:
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class LargeMailUserIdentifier:
        """
        :ivar content:
        :ivar type: CEDEX Code
        :ivar indicator: eg. Building 429 in which Building is the
            Indicator
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        indicator: Optional[str] = field(
            default=None,
            metadata={
                "name": "Indicator",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )


@dataclass
class Locality:
    """Locality is one level lower than adminisstrative area.

    Eg.: cities, reservations and any other built-up areas.

    :ivar address_line:
    :ivar locality_name: Name of the locality
    :ivar post_box:
    :ivar large_mail_user: Specification of a large mail user address.
        Examples of large mail users are postal companies, companies in
        France with a cedex number, hospitals and airports with their
        own post code. Large mail user addresses do not have a street
        name with premise name or premise number in countries like
        Netherlands. But they have a POBox and street also in countries
        like France
    :ivar post_office:
    :ivar postal_route: A Postal van is specific for a route as in
        Is`rael, Rural route
    :ivar thoroughfare:
    :ivar premise:
    :ivar dependent_locality: Dependent localities are Districts within
        cities/towns, locality divisions, postal  divisions of cities,
        suburbs, etc. DependentLocality is a recursive element, but no
        nesting deeper than two exists (Locality-DependentLocality-
        DependentLocality).
    :ivar postal_code:
    :ivar other_element:
    :ivar type: Possible values not limited to: City, IndustrialEstate,
        etc
    :ivar usage_type: Postal or Political - Sometimes locations must be
        distinguished between postal system, and physical locations as
        defined by a political system
    :ivar indicator: Erode (Dist) where (Dist) is the Indicator
    :ivar other_attributes:
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"

    address_line: List[AddressLine] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
        }
    )
    locality_name: List["Locality.LocalityName"] = field(
        default_factory=list,
        metadata={
            "name": "LocalityName",
            "type": "Element",
        }
    )
    post_box: Optional[PostBox] = field(
        default=None,
        metadata={
            "name": "PostBox",
            "type": "Element",
        }
    )
    large_mail_user: Optional[LargeMailUserType] = field(
        default=None,
        metadata={
            "name": "LargeMailUser",
            "type": "Element",
        }
    )
    post_office: Optional[PostOffice] = field(
        default=None,
        metadata={
            "name": "PostOffice",
            "type": "Element",
        }
    )
    postal_route: Optional[PostalRouteType] = field(
        default=None,
        metadata={
            "name": "PostalRoute",
            "type": "Element",
        }
    )
    thoroughfare: Optional[Thoroughfare] = field(
        default=None,
        metadata={
            "name": "Thoroughfare",
            "type": "Element",
        }
    )
    premise: Optional[Premise] = field(
        default=None,
        metadata={
            "name": "Premise",
            "type": "Element",
        }
    )
    dependent_locality: Optional[DependentLocalityType] = field(
        default=None,
        metadata={
            "name": "DependentLocality",
            "type": "Element",
        }
    )
    postal_code: Optional[PostalCode] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    usage_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsageType",
            "type": "Attribute",
        }
    )
    indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Indicator",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )

    @dataclass
    class LocalityName:
        """
        :ivar content:
        :ivar type:
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )


@dataclass
class AdministrativeArea:
    """
    Examples of administrative areas are provinces counties, special regions
    (such as "Rijnmond"), etc.

    :ivar address_line:
    :ivar administrative_area_name: Name of the administrative area. eg.
        MI in USA, NSW in Australia
    :ivar sub_administrative_area: Specification of a sub-administrative
        area. An example of a sub-administrative areas is a county.
        There are two places where the name of an administrative  area
        can be specified and in this case, one becomes sub-
        administrative area.
    :ivar locality:
    :ivar post_office:
    :ivar postal_code:
    :ivar other_element:
    :ivar type: Province or State or County or Kanton, etc
    :ivar usage_type: Postal or Political - Sometimes locations must be
        distinguished between postal system, and physical locations as
        defined by a political system
    :ivar indicator: Erode (Dist) where (Dist) is the Indicator
    :ivar other_attributes:
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"

    address_line: List[AddressLine] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
        }
    )
    administrative_area_name: List["AdministrativeArea.AdministrativeAreaName"] = field(
        default_factory=list,
        metadata={
            "name": "AdministrativeAreaName",
            "type": "Element",
        }
    )
    sub_administrative_area: Optional["AdministrativeArea.SubAdministrativeArea"] = field(
        default=None,
        metadata={
            "name": "SubAdministrativeArea",
            "type": "Element",
        }
    )
    locality: Optional[Locality] = field(
        default=None,
        metadata={
            "name": "Locality",
            "type": "Element",
        }
    )
    post_office: Optional[PostOffice] = field(
        default=None,
        metadata={
            "name": "PostOffice",
            "type": "Element",
        }
    )
    postal_code: Optional[PostalCode] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    usage_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "UsageType",
            "type": "Attribute",
        }
    )
    indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Indicator",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )

    @dataclass
    class AdministrativeAreaName:
        """
        :ivar content:
        :ivar type:
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class SubAdministrativeArea:
        """
        :ivar address_line:
        :ivar sub_administrative_area_name: Name of the sub-
            administrative area
        :ivar locality:
        :ivar post_office:
        :ivar postal_code:
        :ivar other_element:
        :ivar type: Province or State or County or Kanton, etc
        :ivar usage_type: Postal or Political - Sometimes locations must
            be distinguished between postal system, and physical
            locations as defined by a political system
        :ivar indicator: Erode (Dist) where (Dist) is the Indicator
        :ivar other_attributes:
        """
        address_line: List[AddressLine] = field(
            default_factory=list,
            metadata={
                "name": "AddressLine",
                "type": "Element",
            }
        )
        sub_administrative_area_name: List[
            "AdministrativeArea.SubAdministrativeArea.SubAdministrativeAreaName"] = field(
            default_factory=list,
            metadata={
                "name": "SubAdministrativeAreaName",
                "type": "Element",
            }
        )
        locality: Optional[Locality] = field(
            default=None,
            metadata={
                "name": "Locality",
                "type": "Element",
            }
        )
        post_office: Optional[PostOffice] = field(
            default=None,
            metadata={
                "name": "PostOffice",
                "type": "Element",
            }
        )
        postal_code: Optional[PostalCode] = field(
            default=None,
            metadata={
                "name": "PostalCode",
                "type": "Element",
            }
        )
        other_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        usage_type: Optional[str] = field(
            default=None,
            metadata={
                "name": "UsageType",
                "type": "Attribute",
            }
        )
        indicator: Optional[str] = field(
            default=None,
            metadata={
                "name": "Indicator",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

        @dataclass
        class SubAdministrativeAreaName:
            """
            :ivar content:
            :ivar type:
            :ivar code: Used by postal services to encode the name of
                the element.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )


@dataclass
class AddressDetails:
    """This container defines the details of the address.

    Can define multiple addresses including tracking address history

    :ivar postal_service_elements: Postal authorities use specific
        postal service data to expedient delivery of mail
    :ivar address: Address as one line of free text
    :ivar address_lines: Container for Address lines
    :ivar country: Specification of a country
    :ivar administrative_area:
    :ivar locality:
    :ivar thoroughfare:
    :ivar other_element:
    :ivar address_type: Type of address. Example: Postal,
        residential,business, primary, secondary, etc
    :ivar current_status: Moved, Living, Investment, Deceased, etc..
    :ivar valid_from_date: Start Date of the validity of address
    :ivar valid_to_date: End date of the validity of address
    :ivar usage: Communication, Contact, etc.
    :ivar code: Used by postal services to encode the name of the
        element.
    :ivar address_details_key: Key identifier for the element for not
        reinforced references from other elements. Not required to be
        unique for the document to be valid, but application may get
        confused if not unique. Extend this schema adding unique
        contraint if needed.
    :ivar other_attributes:
    """

    class Meta:
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"

    postal_service_elements: Optional["AddressDetails.PostalServiceElements"] = field(
        default=None,
        metadata={
            "name": "PostalServiceElements",
            "type": "Element",
        }
    )
    address: Optional["AddressDetails.Address"] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
        }
    )
    address_lines: Optional[AddressLinesType] = field(
        default=None,
        metadata={
            "name": "AddressLines",
            "type": "Element",
        }
    )
    country: Optional["AddressDetails.Country"] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
        }
    )
    administrative_area: Optional[AdministrativeArea] = field(
        default=None,
        metadata={
            "name": "AdministrativeArea",
            "type": "Element",
        }
    )
    locality: Optional[Locality] = field(
        default=None,
        metadata={
            "name": "Locality",
            "type": "Element",
        }
    )
    thoroughfare: Optional[Thoroughfare] = field(
        default=None,
        metadata={
            "name": "Thoroughfare",
            "type": "Element",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    address_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddressType",
            "type": "Attribute",
            "required": True,
        }
    )
    current_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrentStatus",
            "type": "Attribute",
            "required": True,
        }
    )
    valid_from_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidFromDate",
            "type": "Attribute",
            "required": True,
        }
    )
    valid_to_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidToDate",
            "type": "Attribute",
            "required": True,
        }
    )
    usage: Optional[str] = field(
        default=None,
        metadata={
            "name": "Usage",
            "type": "Attribute",
            "required": True,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
    address_details_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddressDetailsKey",
            "type": "Attribute",
            "required": True,
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
            "required": True,
        }
    )

    @dataclass
    class PostalServiceElements:
        """
        :ivar address_identifier: A unique identifier of an address
            assigned by postal authorities. Example: DPID in Australia
        :ivar endorsement_line_code: Directly affects postal service
            distribution
        :ivar key_line_code: Required for some postal services
        :ivar barcode: Required for some postal services
        :ivar sorting_code: Used for sorting addresses. Values may for
            example be CEDEX 16 (France)
        :ivar address_latitude: Latitude of delivery address
        :ivar address_latitude_direction: Latitude direction of delivery
            address;N = North and S = South
        :ivar address_longitude: Longtitude of delivery address
        :ivar address_longitude_direction: Longtitude direction of
            delivery address;N=North and S=South
        :ivar supplementary_postal_service_data: any postal service
            elements not covered by the container can be represented
            using this element
        :ivar other_element:
        :ivar type: USPS, ECMA, UN/PROLIST, etc
        :ivar other_attributes:
        """
        address_identifier: List["AddressDetails.PostalServiceElements.AddressIdentifier"] = field(
            default_factory=list,
            metadata={
                "name": "AddressIdentifier",
                "type": "Element",
            }
        )
        endorsement_line_code: Optional["AddressDetails.PostalServiceElements.EndorsementLineCode"] = field(
            default=None,
            metadata={
                "name": "EndorsementLineCode",
                "type": "Element",
            }
        )
        key_line_code: Optional["AddressDetails.PostalServiceElements.KeyLineCode"] = field(
            default=None,
            metadata={
                "name": "KeyLineCode",
                "type": "Element",
            }
        )
        barcode: Optional["AddressDetails.PostalServiceElements.Barcode"] = field(
            default=None,
            metadata={
                "name": "Barcode",
                "type": "Element",
            }
        )
        sorting_code: Optional["AddressDetails.PostalServiceElements.SortingCode"] = field(
            default=None,
            metadata={
                "name": "SortingCode",
                "type": "Element",
            }
        )
        address_latitude: Optional["AddressDetails.PostalServiceElements.AddressLatitude"] = field(
            default=None,
            metadata={
                "name": "AddressLatitude",
                "type": "Element",
            }
        )
        address_latitude_direction: Optional["AddressDetails.PostalServiceElements.AddressLatitudeDirection"] = field(
            default=None,
            metadata={
                "name": "AddressLatitudeDirection",
                "type": "Element",
            }
        )
        address_longitude: Optional["AddressDetails.PostalServiceElements.AddressLongitude"] = field(
            default=None,
            metadata={
                "name": "AddressLongitude",
                "type": "Element",
            }
        )
        address_longitude_direction: Optional["AddressDetails.PostalServiceElements.AddressLongitudeDirection"] = field(
            default=None,
            metadata={
                "name": "AddressLongitudeDirection",
                "type": "Element",
            }
        )
        supplementary_postal_service_data: List[
            "AddressDetails.PostalServiceElements.SupplementaryPostalServiceData"] = field(
            default_factory=list,
            metadata={
                "name": "SupplementaryPostalServiceData",
                "type": "Element",
            }
        )
        other_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

        @dataclass
        class AddressIdentifier:
            """
            :ivar content:
            :ivar identifier_type: Type of identifier. eg. DPID as in
                Australia
            :ivar type:
            :ivar code: Used by postal services to encode the name of
                the element.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            identifier_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IdentifierType",
                    "type": "Attribute",
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class EndorsementLineCode:
            """
            :ivar content:
            :ivar type: Specific to postal service
            :ivar code: Used by postal services to encode the name of
                the element.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class KeyLineCode:
            """
            :ivar content:
            :ivar type: Specific to postal service
            :ivar code: Used by postal services to encode the name of
                the element.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class Barcode:
            """
            :ivar content:
            :ivar type: Specific to postal service
            :ivar code: Used by postal services to encode the name of
                the element.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class SortingCode:
            """
            :ivar type: Specific to postal service
            :ivar code: Used by postal services to encode the name of
                the element.
            """
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )

        @dataclass
        class AddressLatitude:
            """
            :ivar content:
            :ivar type: Specific to postal service
            :ivar code: Used by postal services to encode the name of
                the element.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class AddressLatitudeDirection:
            """
            Specific to postal service.

            :ivar content:
            :ivar type:
            :ivar code: Used by postal services to encode the name of
                the element.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class AddressLongitude:
            """
            :ivar content:
            :ivar type: Specific to postal service
            :ivar code: Used by postal services to encode the name of
                the element.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class AddressLongitudeDirection:
            """
            :ivar content:
            :ivar type: Specific to postal service
            :ivar code: Used by postal services to encode the name of
                the element.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

        @dataclass
        class SupplementaryPostalServiceData:
            """
            :ivar content:
            :ivar type: Specific to postal service
            :ivar code: Used by postal services to encode the name of
                the element.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )

    @dataclass
    class Address:
        """
        :ivar content:
        :ivar type: Postal, residential, corporate, etc
        :ivar code: Used by postal services to encode the name of the
            element.
        :ivar other_attributes:
        """
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

    @dataclass
    class Country:
        """
        :ivar address_line:
        :ivar country_name_code: A country code according to the
            specified scheme
        :ivar country_name:
        :ivar administrative_area:
        :ivar locality:
        :ivar thoroughfare:
        :ivar other_element:
        :ivar other_attributes:
        """
        address_line: List[AddressLine] = field(
            default_factory=list,
            metadata={
                "name": "AddressLine",
                "type": "Element",
            }
        )
        country_name_code: List["AddressDetails.Country.CountryNameCode"] = field(
            default_factory=list,
            metadata={
                "name": "CountryNameCode",
                "type": "Element",
            }
        )
        country_name: List[CountryName] = field(
            default_factory=list,
            metadata={
                "name": "CountryName",
                "type": "Element",
            }
        )
        administrative_area: Optional[AdministrativeArea] = field(
            default=None,
            metadata={
                "name": "AdministrativeArea",
                "type": "Element",
            }
        )
        locality: Optional[Locality] = field(
            default=None,
            metadata={
                "name": "Locality",
                "type": "Element",
            }
        )
        thoroughfare: Optional[Thoroughfare] = field(
            default=None,
            metadata={
                "name": "Thoroughfare",
                "type": "Element",
            }
        )
        other_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
            }
        )
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )

        @dataclass
        class CountryNameCode:
            """
            :ivar content:
            :ivar scheme: Country code scheme possible values, but not
                limited to: iso.3166-2, iso.3166-3 for two and three
                character country codes.
            :ivar code: Used by postal services to encode the name of
                the element.
            :ivar other_attributes:
            """
            content: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "mixed": True,
                }
            )
            scheme: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Scheme",
                    "type": "Attribute",
                }
            )
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                }
            )
            other_attributes: Dict = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                }
            )


@dataclass
class XAl:
    """
    Root element for a list of addresses.

    :ivar address_details:
    :ivar other_element:
    :ivar version: Specific to DTD to specify the version number of DTD
    :ivar other_attributes:
    """

    class Meta:
        name = "xAL"
        namespace = "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"

    address_details: List[AddressDetails] = field(
        default_factory=list,
        metadata={
            "name": "AddressDetails",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
