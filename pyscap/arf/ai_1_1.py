from dataclasses import dataclass, field
from decimal import Decimal
from typing import Dict, List, Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from .reporting_core_1_1 import RelationshipsContainerType
from .x_al import (
    AddressLine,
    AddressLinesType,
    AdministrativeArea,
    CountryName,
    Locality,
    Thoroughfare,
)
from .x_nl import (
    OrganisationNameDetails,
    PersonName,
)

AI_1_1_NAMESPACE = "http://scap.nist.gov/schema/asset-identification/1.1"


@dataclass
class Cpe:
    """
    A Common Platform Enumeration (CPE) name (CPE 2.2 URI or CPE 2.3 Formatted
    String).
    """

    class Meta:
        name = "cpe"
        namespace = AI_1_1_NAMESPACE

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"[cC][pP][eE]:/[AHOaho]?(:[A-Za-z0-9\._\-~%]*){0,6}",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": AI_1_1_NAMESPACE,
        }
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": AI_1_1_NAMESPACE,
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
class EmailAddress:
    """
    An email address.
    """

    class Meta:
        name = "email-address"
        namespace = AI_1_1_NAMESPACE

    value: Optional[str] = field(
        default=None,
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": AI_1_1_NAMESPACE,
        }
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": AI_1_1_NAMESPACE,
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
class Fqdn:
    """
    The fully qualified domain name for the object.
    """

    class Meta:
        name = "fqdn"
        namespace = AI_1_1_NAMESPACE

    value: Optional[str] = field(
        default=None,
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": AI_1_1_NAMESPACE,
        }
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": AI_1_1_NAMESPACE,
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
class IpAddressType:
    class Meta:
        name = "ip-address-type"

    ip_v4: Optional["IpAddressType.IpV4"] = field(
        default=None,
        metadata={
            "name": "ip-v4",
            "type": "Element",
        }
    )
    ip_v6: Optional["IpAddressType.IpV6"] = field(
        default=None,
        metadata={
            "name": "ip-v6",
            "type": "Element",
        }
    )

    @dataclass
    class IpV4:
        value: Optional[str] = field(
            default=None,
            metadata={
                "pattern": r"([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))",
            }
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
    class IpV6:
        value: Optional[str] = field(
            default=None,
            metadata={
                "pattern": r"([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}",
            }
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
class Location:
    class Meta:
        name = "location"
        namespace = AI_1_1_NAMESPACE

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class LocationPoint:
    """
    The geographic point where an asset is located.

    :ivar latitude: The latitude of the asset, defined between -90 (90
        degrees South, inclusive) and                         90 (90
        degrees North, inclusive).
    :ivar longitude: The longitude of the asset, defined between -180
        (180 degrees West, exclusive) and                         180
        (180 degrees East, inclusive).
    :ivar elevation: The elevation of the asset, specified in meters
        from sea level.
    :ivar radius: The radius of a horizontal circle centered on the
        point within which the asset                         resides.
    :ivar source:
    :ivar timestamp:
    :ivar other_attributes:
    """

    class Meta:
        name = "location-point"
        namespace = AI_1_1_NAMESPACE

    latitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": Decimal("-90"),
            "max_inclusive": Decimal("90"),
        }
    )
    longitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": Decimal("-180"),
            "max_inclusive": Decimal("180"),
        }
    )
    elevation: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    radius: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": Decimal("0"),
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": AI_1_1_NAMESPACE,
        }
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": AI_1_1_NAMESPACE,
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
class LocationRegion:
    """
    The region where an asset is located.
    """

    class Meta:
        name = "location-region"
        namespace = AI_1_1_NAMESPACE

    value: Optional[str] = field(
        default=None,
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": AI_1_1_NAMESPACE,
        }
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": AI_1_1_NAMESPACE,
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
class SyntheticId:
    """
    Holds the synthetic ID for the asset.

    :ivar resource: The namespace governing this synthetic ID.
    :ivar id: The ID of the asset within the resource namespace.
    """

    class Meta:
        name = "synthetic-id"
        namespace = AI_1_1_NAMESPACE

    resource: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
class TelephoneNumber:
    """The telephone number.

    For a North American number, the number must be valid and the format
    must be XXX-XXX-XXXX where X is a digit. For an international
    number, the number must begin with a '+' symbol, followed by 7 to 15
    digits. A space may be used between digits, as appropriate. For
    example: +88 888 888 8 (this is following the ITU-T E.123 notation).
    """

    class Meta:
        name = "telephone-number"
        namespace = AI_1_1_NAMESPACE

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"(([2-9][0-8]\d-[2-9]\d{2}-[0-9]{4})|(\+([0-9] ?){6,14}[0-9]))",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": AI_1_1_NAMESPACE,
        }
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": AI_1_1_NAMESPACE,
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
class WebsiteUrl:
    """
    The URL to the website.
    """

    class Meta:
        name = "website-url"
        namespace = AI_1_1_NAMESPACE

    value: Optional[str] = field(
        default=None,
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": AI_1_1_NAMESPACE,
        }
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": AI_1_1_NAMESPACE,
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
class IpAddress(IpAddressType):
    """
    An IP address.
    """

    class Meta:
        name = "ip-address"
        namespace = AI_1_1_NAMESPACE


@dataclass
class LocationAddress:
    """
    The address where an asset is located.

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
        name = "location-address"
        namespace = AI_1_1_NAMESPACE

    postal_service_elements: Optional["LocationAddress.PostalServiceElements"] = field(
        default=None,
        metadata={
            "name": "PostalServiceElements",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    address: Optional["LocationAddress.Address"] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    address_lines: Optional[AddressLinesType] = field(
        default=None,
        metadata={
            "name": "AddressLines",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    country: Optional["LocationAddress.Country"] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    administrative_area: Optional[AdministrativeArea] = field(
        default=None,
        metadata={
            "name": "AdministrativeArea",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
        }
    )
    locality: Optional[Locality] = field(
        default=None,
        metadata={
            "name": "Locality",
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
        address_identifier: List["LocationAddress.PostalServiceElements.AddressIdentifier"] = field(
            default_factory=list,
            metadata={
                "name": "AddressIdentifier",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
            }
        )
        endorsement_line_code: Optional["LocationAddress.PostalServiceElements.EndorsementLineCode"] = field(
            default=None,
            metadata={
                "name": "EndorsementLineCode",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
            }
        )
        key_line_code: Optional["LocationAddress.PostalServiceElements.KeyLineCode"] = field(
            default=None,
            metadata={
                "name": "KeyLineCode",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
            }
        )
        barcode: Optional["LocationAddress.PostalServiceElements.Barcode"] = field(
            default=None,
            metadata={
                "name": "Barcode",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
            }
        )
        sorting_code: Optional["LocationAddress.PostalServiceElements.SortingCode"] = field(
            default=None,
            metadata={
                "name": "SortingCode",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
            }
        )
        address_latitude: Optional["LocationAddress.PostalServiceElements.AddressLatitude"] = field(
            default=None,
            metadata={
                "name": "AddressLatitude",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
            }
        )
        address_latitude_direction: Optional["LocationAddress.PostalServiceElements.AddressLatitudeDirection"] = field(
            default=None,
            metadata={
                "name": "AddressLatitudeDirection",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
            }
        )
        address_longitude: Optional["LocationAddress.PostalServiceElements.AddressLongitude"] = field(
            default=None,
            metadata={
                "name": "AddressLongitude",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
            }
        )
        address_longitude_direction: Optional[
            "LocationAddress.PostalServiceElements.AddressLongitudeDirection"] = field(
            default=None,
            metadata={
                "name": "AddressLongitudeDirection",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
            }
        )
        supplementary_postal_service_data: List[
            "LocationAddress.PostalServiceElements.SupplementaryPostalServiceData"] = field(
            default_factory=list,
            metadata={
                "name": "SupplementaryPostalServiceData",
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
                "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
            }
        )
        country_name_code: List["LocationAddress.Country.CountryNameCode"] = field(
            default_factory=list,
            metadata={
                "name": "CountryNameCode",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
            }
        )
        country_name: List[CountryName] = field(
            default_factory=list,
            metadata={
                "name": "CountryName",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
            }
        )
        administrative_area: Optional[AdministrativeArea] = field(
            default=None,
            metadata={
                "name": "AdministrativeArea",
                "type": "Element",
                "namespace": "urn:oasis:names:tc:ciq:xsdschema:xAL:2.0",
            }
        )
        locality: Optional[Locality] = field(
            default=None,
            metadata={
                "name": "Locality",
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
class Locations:
    """
    One or more locations where this asset resides.

    :ivar location_region:
    :ivar location_point:
    :ivar location_address:
    :ivar location: The base for a subtitution group for elements that
        contain location                             information.
    """

    class Meta:
        name = "locations"
        namespace = AI_1_1_NAMESPACE

    location_region: List[LocationRegion] = field(
        default_factory=list,
        metadata={
            "name": "location-region",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    location_point: List[LocationPoint] = field(
        default_factory=list,
        metadata={
            "name": "location-point",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    location_address: List[LocationAddress] = field(
        default_factory=list,
        metadata={
            "name": "location-address",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    location: List[Location] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class NetworkInterfaceType:
    """
    :ivar ip_address: The IP address for this network interface.
    :ivar mac_address: The MAC address associated with this network
        interface.
    :ivar url: A URL in a relevant DNS server for this IP address.
    :ivar subnet_mask: The subnet mask address for this network
        interface.
    :ivar default_route: The IP address for the default gateway of this
        connection.
    """

    class Meta:
        name = "network-interface-type"

    ip_address: Optional[IpAddress] = field(
        default=None,
        metadata={
            "name": "ip-address",
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
        }
    )
    mac_address: Optional["NetworkInterfaceType.MacAddress"] = field(
        default=None,
        metadata={
            "name": "mac-address",
            "type": "Element",
        }
    )
    url: List["NetworkInterfaceType.Url"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    subnet_mask: Optional[IpAddressType] = field(
        default=None,
        metadata={
            "name": "subnet-mask",
            "type": "Element",
        }
    )
    default_route: Optional[IpAddressType] = field(
        default=None,
        metadata={
            "name": "default-route",
            "type": "Element",
        }
    )

    @dataclass
    class MacAddress:
        value: Optional[str] = field(
            default=None,
            metadata={
                "pattern": r"([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}",
            }
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
    class Url:
        value: Optional[str] = field(
            default=None,
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
class AssetType:
    """
    :ivar synthetic_id:
    :ivar locations:
    :ivar extended_information: This is a container to hold any
        addtional identifying information for an asset, as
        specified by the content creator.
    :ivar timestamp:
    """

    class Meta:
        name = "asset-type"

    synthetic_id: List[SyntheticId] = field(
        default_factory=list,
        metadata={
            "name": "synthetic-id",
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
        }
    )
    locations: Optional[Locations] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
        }
    )
    extended_information: Optional["AssetType.ExtendedInformation"] = field(
        default=None,
        metadata={
            "name": "extended-information",
            "type": "Element",
        }
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": AI_1_1_NAMESPACE,
        }
    )

    @dataclass
    class ExtendedInformation:
        other_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##other",
                "min_occurs": 1,
            }
        )


@dataclass
class Asset(AssetType):
    """
    Holds identifying attributes that are common to all assets.
    """

    class Meta:
        name = "asset"
        namespace = AI_1_1_NAMESPACE


@dataclass
class DataType(AssetType):
    class Meta:
        name = "data-type"


@dataclass
class ItAssetType(AssetType):
    class Meta:
        name = "it-asset-type"


@dataclass
class OrganizationType(AssetType):
    class Meta:
        name = "organization-type"

    organisation_name_details: List[OrganisationNameDetails] = field(
        default_factory=list,
        metadata={
            "name": "OrganisationNameDetails",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xNL:2.0",
        }
    )
    email_address: List[EmailAddress] = field(
        default_factory=list,
        metadata={
            "name": "email-address",
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
        }
    )
    telephone_number: List[TelephoneNumber] = field(
        default_factory=list,
        metadata={
            "name": "telephone-number",
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
        }
    )
    website_url: List[WebsiteUrl] = field(
        default_factory=list,
        metadata={
            "name": "website-url",
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
        }
    )


@dataclass
class PersonType(AssetType):
    """
    :ivar person_name:
    :ivar email_address:
    :ivar telephone_number:
    :ivar birthdate: The birthdate of the person.
    """

    class Meta:
        name = "person-type"

    person_name: Optional[PersonName] = field(
        default=None,
        metadata={
            "name": "PersonName",
            "type": "Element",
            "namespace": "urn:oasis:names:tc:ciq:xsdschema:xNL:2.0",
        }
    )
    email_address: List[EmailAddress] = field(
        default_factory=list,
        metadata={
            "name": "email-address",
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
        }
    )
    telephone_number: List[TelephoneNumber] = field(
        default_factory=list,
        metadata={
            "name": "telephone-number",
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
        }
    )
    birthdate: Optional["PersonType.Birthdate"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )

    @dataclass
    class Birthdate:
        value: Optional[XmlDate] = field(
            default=None,
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
class CircuitType(ItAssetType):
    """
    :ivar circuit_name: The common name for the circult.
    """

    class Meta:
        name = "circuit-type"

    circuit_name: Optional["CircuitType.CircuitName"] = field(
        default=None,
        metadata={
            "name": "circuit-name",
            "type": "Element",
        }
    )

    @dataclass
    class CircuitName:
        value: Optional[str] = field(
            default=None,
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
class ComputingDeviceType(ItAssetType):
    """
    :ivar distinguished_name: The full X.500 distinguished name for the
        device.
    :ivar cpe: The hardware CPE name for the device (CPE 2.2 URI or CPE
        2.3 Formatted String).
    :ivar connections: The IP network interface connections that exist
        for the device (regardless                                 of if
        the network interface is connected to a network or not).
    :ivar fqdn:
    :ivar hostname: The hostname of the computing device.
    :ivar motherboard_guid: The motherboard globally unique identifier
        of the computing                                 device.
    """

    class Meta:
        name = "computing-device-type"

    distinguished_name: Optional["ComputingDeviceType.DistinguishedName"] = field(
        default=None,
        metadata={
            "name": "distinguished-name",
            "type": "Element",
        }
    )
    cpe: List[Cpe] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
        }
    )
    connections: Optional["ComputingDeviceType.Connections"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fqdn: Optional[Fqdn] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
        }
    )
    hostname: Optional["ComputingDeviceType.Hostname"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    motherboard_guid: Optional["ComputingDeviceType.MotherboardGuid"] = field(
        default=None,
        metadata={
            "name": "motherboard-guid",
            "type": "Element",
        }
    )

    @dataclass
    class DistinguishedName:
        value: Optional[str] = field(
            default=None,
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
    class Connections:
        """
        :ivar connection: An IP network interface connection.
        """
        connection: List[NetworkInterfaceType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Hostname:
        value: Optional[str] = field(
            default=None,
            metadata={
                "pattern": r"[\w\-]+(\.[\w\-]+){0,}",
            }
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
    class MotherboardGuid:
        value: Optional[str] = field(
            default=None,
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
class Data(DataType):
    """A stub element to represent the identification of data.

    This element can be extended in the future for specific types of
    data.
    """

    class Meta:
        name = "data"
        namespace = AI_1_1_NAMESPACE


@dataclass
class DatabaseType(ItAssetType):
    """
    :ivar instance_name: The name of the database instance being
        identified.
    """

    class Meta:
        name = "database-type"

    instance_name: Optional["DatabaseType.InstanceName"] = field(
        default=None,
        metadata={
            "name": "instance-name",
            "type": "Element",
        }
    )

    @dataclass
    class InstanceName:
        value: Optional[str] = field(
            default=None,
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
class ItAsset(ItAssetType):
    """
    Holds identifying attributes that are common to all IT assets.
    """

    class Meta:
        name = "it-asset"
        namespace = AI_1_1_NAMESPACE


@dataclass
class NetworkType(ItAssetType):
    """
    :ivar network_name: The name of the network as commonly referred to.
    :ivar ip_net_range: The start and end IP addresses to indicate the
        range of IP addresses
        covered by this network.
    :ivar cidr: The classless inter-domain routing notation for the
        network.
    """

    class Meta:
        name = "network-type"

    network_name: Optional["NetworkType.NetworkName"] = field(
        default=None,
        metadata={
            "name": "network-name",
            "type": "Element",
        }
    )
    ip_net_range: Optional["NetworkType.IpNetRange"] = field(
        default=None,
        metadata={
            "name": "ip-net-range",
            "type": "Element",
        }
    )
    cidr: Optional["NetworkType.Cidr"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )

    @dataclass
    class NetworkName:
        value: Optional[str] = field(
            default=None,
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
    class IpNetRange:
        """
        :ivar ip_net_range_start: The starting IP address in the
            network.
        :ivar ip_net_range_end: The ending IP address in the network.
        """
        ip_net_range_start: Optional[IpAddressType] = field(
            default=None,
            metadata={
                "name": "ip-net-range-start",
                "type": "Element",
                "required": True,
            }
        )
        ip_net_range_end: Optional[IpAddressType] = field(
            default=None,
            metadata={
                "name": "ip-net-range-end",
                "type": "Element",
                "required": True,
            }
        )

    @dataclass
    class Cidr:
        value: Optional[str] = field(
            default=None,
            metadata={
                "pattern": r"([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))/([0-9]|[1-2][0-9]|3[0-2])",
            }
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
class Organization(OrganizationType):
    """
    Holds identifying attributes for an organization.
    """

    class Meta:
        name = "organization"
        namespace = AI_1_1_NAMESPACE


@dataclass
class Person(PersonType):
    """
    Holds identifying attributes for a person.
    """

    class Meta:
        name = "person"
        namespace = AI_1_1_NAMESPACE


@dataclass
class ServiceType(ItAssetType):
    """
    :ivar host: The hostname or IP address where the service is hosted.
    :ivar port: The port to which the service is bound.
    :ivar port_range: The inclusive port range to which the service is
        bound.
    :ivar protocol: The protocol used to interact with the service.
    """

    class Meta:
        name = "service-type"

    host: Optional["ServiceType.Host"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    port: List["ServiceType.Port"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    port_range: List["ServiceType.PortRange"] = field(
        default_factory=list,
        metadata={
            "name": "port-range",
            "type": "Element",
        }
    )
    protocol: Optional["ServiceType.Protocol"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )

    @dataclass
    class Host:
        fqdn: Optional[Fqdn] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        ip_address: Optional[IpAddress] = field(
            default=None,
            metadata={
                "name": "ip-address",
                "type": "Element",
                "namespace": AI_1_1_NAMESPACE,
            }
        )

    @dataclass
    class Port:
        value: Optional[int] = field(
            default=None,
            metadata={
                "min_inclusive": 0,
                "max_inclusive": 65535,
            }
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
    class PortRange:
        lower_bound: Optional[int] = field(
            default=None,
            metadata={
                "name": "lower-bound",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0,
                "max_inclusive": 65535,
            }
        )
        upper_bound: Optional[int] = field(
            default=None,
            metadata={
                "name": "upper-bound",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0,
                "max_inclusive": 65535,
            }
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
    class Protocol:
        value: Optional[str] = field(
            default=None,
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
class SoftwareType(ItAssetType):
    """
    :ivar installation_id: Any identifier for the software instance
        (installation)
    :ivar cpe: The CPE name for the software (CPE 2.2 URI or CPE 2.3
        Formatted String).
    :ivar license: The license key for the software.
    """

    class Meta:
        name = "software-type"

    installation_id: Optional["SoftwareType.InstallationId"] = field(
        default=None,
        metadata={
            "name": "installation-id",
            "type": "Element",
        }
    )
    cpe: Optional[Cpe] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
        }
    )
    license: List["SoftwareType.License"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )

    @dataclass
    class InstallationId:
        value: Optional[str] = field(
            default=None,
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
    class License:
        value: Optional[str] = field(
            default=None,
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
class SystemType(ItAssetType):
    """
    :ivar system_name: The name of the system. It is possible that a
        system have multiple names,                                 or
        even abbreviated names. Each one of those names may be captured
        here.
    :ivar version: The version of the system.
    """

    class Meta:
        name = "system-type"

    system_name: List["SystemType.SystemName"] = field(
        default_factory=list,
        metadata={
            "name": "system-name",
            "type": "Element",
        }
    )
    version: Optional["SystemType.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )

    @dataclass
    class SystemName:
        value: Optional[str] = field(
            default=None,
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
    class Version:
        value: Optional[str] = field(
            default=None,
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
class WebsiteType(ItAssetType):
    """
    :ivar document_root: The absolute path to the document root location
        of the website on the                                 host.
    :ivar locale: The locale of the website represented as an RFC 5646
        language, and optionally, region code.
    """

    class Meta:
        name = "website-type"

    document_root: Optional["WebsiteType.DocumentRoot"] = field(
        default=None,
        metadata={
            "name": "document-root",
            "type": "Element",
        }
    )
    locale: Optional["WebsiteType.Locale"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )

    @dataclass
    class DocumentRoot:
        value: Optional[str] = field(
            default=None,
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
    class Locale:
        value: Optional[str] = field(
            default=None,
            metadata={
                "pattern": r"[a-zA-Z]{2,3}(-([a-zA-Z]{2}|[0-9]{3}))?",
            }
        )
        source: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
            }
        )
        timestamp: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": AI_1_1_NAMESPACE,
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
class Circuit(CircuitType):
    """
    Holds identifying attributes for a circuit.
    """

    class Meta:
        name = "circuit"
        namespace = AI_1_1_NAMESPACE


@dataclass
class ComputingDevice(ComputingDeviceType):
    """
    Holds identifying attributes for a computing device.
    """

    class Meta:
        name = "computing-device"
        namespace = AI_1_1_NAMESPACE


@dataclass
class Database(DatabaseType):
    """
    Holds identifying attributes for a database.
    """

    class Meta:
        name = "database"
        namespace = AI_1_1_NAMESPACE


@dataclass
class Network(NetworkType):
    """
    Holds identifying attributes for a network.
    """

    class Meta:
        name = "network"
        namespace = AI_1_1_NAMESPACE


@dataclass
class ServedBy(ServiceType):
    """
    The service that is serving up the asset.
    """

    class Meta:
        name = "served-by"
        namespace = AI_1_1_NAMESPACE


@dataclass
class Service(ServiceType):
    """
    Holds identifying attributes for a service.
    """

    class Meta:
        name = "service"
        namespace = AI_1_1_NAMESPACE


@dataclass
class Software(SoftwareType):
    """
    Holds identifying attributes for a software installation.
    """

    class Meta:
        name = "software"
        namespace = AI_1_1_NAMESPACE


@dataclass
class System(SystemType):
    """
    Holds identifying attributes for a system.
    """

    class Meta:
        name = "system"
        namespace = AI_1_1_NAMESPACE


@dataclass
class Website(WebsiteType):
    """
    Holds identifying attributes for a website.
    """

    class Meta:
        name = "website"
        namespace = AI_1_1_NAMESPACE


@dataclass
class AssetsType(RelationshipsContainerType):
    class Meta:
        name = "assets-type"

    person: List[Person] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
            "min_occurs": 1,
        }
    )
    organization: List[Organization] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
            "min_occurs": 1,
        }
    )
    data: List[Data] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
            "min_occurs": 1,
        }
    )
    website: List[Website] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
            "min_occurs": 1,
        }
    )
    system: List[System] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
            "min_occurs": 1,
        }
    )
    software: List[Software] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
            "min_occurs": 1,
        }
    )
    service: List[Service] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
            "min_occurs": 1,
        }
    )
    network: List[Network] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
            "min_occurs": 1,
        }
    )
    database: List[Database] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
            "min_occurs": 1,
        }
    )
    computing_device: List[ComputingDevice] = field(
        default_factory=list,
        metadata={
            "name": "computing-device",
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
            "min_occurs": 1,
        }
    )
    circuit: List[Circuit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
            "min_occurs": 1,
        }
    )
    it_asset: List[ItAsset] = field(
        default_factory=list,
        metadata={
            "name": "it-asset",
            "type": "Element",
            "namespace": AI_1_1_NAMESPACE,
            "min_occurs": 1,
        }
    )
    asset: List["AssetsType.Asset"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Asset:
        """
        :ivar person:
        :ivar organization:
        :ivar data:
        :ivar website:
        :ivar system:
        :ivar software:
        :ivar service:
        :ivar network:
        :ivar database:
        :ivar computing_device:
        :ivar circuit:
        :ivar it_asset:
        :ivar asset:
        :ivar id: An internal ID to identify this asset.
        :ivar other_attributes: A placeholder so that content creators
            can add attributes as
            desired.
        """
        person: Optional[Person] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": AI_1_1_NAMESPACE,
                "required": True,
            }
        )
        organization: Optional[Organization] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": AI_1_1_NAMESPACE,
                "required": True,
            }
        )
        data: Optional[Data] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": AI_1_1_NAMESPACE,
                "required": True,
            }
        )
        website: Optional[Website] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": AI_1_1_NAMESPACE,
                "required": True,
            }
        )
        system: Optional[System] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": AI_1_1_NAMESPACE,
                "required": True,
            }
        )
        software: Optional[Software] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": AI_1_1_NAMESPACE,
                "required": True,
            }
        )
        service: Optional[Service] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": AI_1_1_NAMESPACE,
                "required": True,
            }
        )
        network: Optional[Network] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": AI_1_1_NAMESPACE,
                "required": True,
            }
        )
        database: Optional[Database] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": AI_1_1_NAMESPACE,
                "required": True,
            }
        )
        computing_device: Optional[ComputingDevice] = field(
            default=None,
            metadata={
                "name": "computing-device",
                "type": "Element",
                "namespace": AI_1_1_NAMESPACE,
                "required": True,
            }
        )
        circuit: Optional[Circuit] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": AI_1_1_NAMESPACE,
                "required": True,
            }
        )
        it_asset: Optional[ItAsset] = field(
            default=None,
            metadata={
                "name": "it-asset",
                "type": "Element",
                "namespace": AI_1_1_NAMESPACE,
                "required": True,
            }
        )
        asset: Optional[Asset] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": AI_1_1_NAMESPACE,
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
        other_attributes: Dict = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )


@dataclass
class AssetIdentificationType(AssetsType):
    class Meta:
        name = "asset-identification-type"

    asset_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "asset-ref",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Assets(AssetsType):
    class Meta:
        name = "assets"
        namespace = AI_1_1_NAMESPACE


@dataclass
class AssetRelated(AssetIdentificationType):
    class Meta:
        name = "asset-related"
        namespace = AI_1_1_NAMESPACE
