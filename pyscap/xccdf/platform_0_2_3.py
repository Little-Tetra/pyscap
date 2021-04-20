from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://www.cisecurity.org/xccdf/platform/0.2.3"


class LogicalOperatorOperator(Enum):
    AND_VALUE = "and"
    OR_VALUE = "or"


@dataclass
class Product:
    class Meta:
        name = "product"
        namespace = "http://www.cisecurity.org/xccdf/platform/0.2.3"

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TextType:
    """Type for a string with an xml:lang attribute.

    (Note: changed this to allow any xml: attribute
    because xml:lang is a bit narrow, and also would
    require the validation processor to download the
    XML namespace schema every time.  We cannot count
    on XCCDF or other benchmark users have a live
    Internet connection at all times.)
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


class VersionOperatorType(Enum):
    """Allowed operators for version elements.

    These are valid only for quasi-numeric version numbers, but the
    schema doesn't enforce it.
    """
    EQUALS = "equals"
    NOT_EQUAL = "not equal"


@dataclass
class LogicalOperator:
    class Meta:
        name = "logical-operator"
        namespace = "http://www.cisecurity.org/xccdf/platform/0.2.3"

    product: List[Product] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    logical_operator: List["LogicalOperator"] = field(
        default_factory=list,
        metadata={
            "name": "logical-operator",
            "type": "Element",
        }
    )
    operator: Optional[LogicalOperatorOperator] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Platform:
    """
    A listing of all supported platforms.
    """
    class Meta:
        name = "platform"
        namespace = "http://www.cisecurity.org/xccdf/platform/0.2.3"

    remark: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ProductType:
    """An individual product or component that makes up the overall platform.

    For more information see the subtypes below. A product consists of:
    a name, a version designator, zero or more named properties, and
    zero or more remarks.

    :ivar title:
    :ivar remark:
    :ivar vendor: The organization  responsible for development and
        maintenance of the product
    :ivar family: The product family the software or device belongs to.
        This will be used along with the optional model and  level
        elements to determine version-range comparisons. Example:
        "Windows", "routers", "portal server".
    :ivar model: The product's model which will differentiate major
        versions  of software.  This may be useful when defining that
        all  versions of software of a specific model are acceptable.
    :ivar level: The product's level which will differentiate functional
        capabilities across the same software version. Example:
        "enterprise", "home"
    :ivar version: The version designation for a platform component.
        This is the type for the version element: the element content is
        a version name or number, and the operator attribute specifies
        how that version applies.  For example, to say 'IOS 12.1 or
        later', the content would be "12.1" and the operator attribute
        would be  "greater than or equal to".
    :ivar version_range:
    """
    class Meta:
        name = "productType"

    title: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.cisecurity.org/xccdf/platform/0.2.3",
            "required": True,
        }
    )
    remark: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.cisecurity.org/xccdf/platform/0.2.3",
        }
    )
    vendor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.cisecurity.org/xccdf/platform/0.2.3",
            "required": True,
        }
    )
    family: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.cisecurity.org/xccdf/platform/0.2.3",
            "required": True,
        }
    )
    model: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.cisecurity.org/xccdf/platform/0.2.3",
        }
    )
    level: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.cisecurity.org/xccdf/platform/0.2.3",
        }
    )
    version: Optional["ProductType.Version"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.cisecurity.org/xccdf/platform/0.2.3",
        }
    )
    version_range: Optional["ProductType.VersionRange"] = field(
        default=None,
        metadata={
            "name": "version-range",
            "type": "Element",
            "namespace": "http://www.cisecurity.org/xccdf/platform/0.2.3",
        }
    )

    @dataclass
    class Version:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        operator: VersionOperatorType = field(
            default=VersionOperatorType.EQUALS,
            metadata={
                "type": "Attribute",
            }
        )

    @dataclass
    class VersionRange:
        min_inclusive: Optional[str] = field(
            default=None,
            metadata={
                "name": "min-inclusive",
                "type": "Element",
                "namespace": "http://www.cisecurity.org/xccdf/platform/0.2.3",
            }
        )
        min_exclusive: Optional[str] = field(
            default=None,
            metadata={
                "name": "min-exclusive",
                "type": "Element",
                "namespace": "http://www.cisecurity.org/xccdf/platform/0.2.3",
            }
        )
        max_inclusive: Optional[str] = field(
            default=None,
            metadata={
                "name": "max-inclusive",
                "type": "Element",
                "namespace": "http://www.cisecurity.org/xccdf/platform/0.2.3",
            }
        )
        max_exclusive: Optional[str] = field(
            default=None,
            metadata={
                "name": "max-exclusive",
                "type": "Element",
                "namespace": "http://www.cisecurity.org/xccdf/platform/0.2.3",
            }
        )


@dataclass
class Application(ProductType):
    """An application or user-level program component product, part of a
    platform.

    Examples: Microsoft Word, Mozilla
    """
    class Meta:
        name = "application"
        namespace = "http://www.cisecurity.org/xccdf/platform/0.2.3"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"app-[a-zA-Z0-9\-]+",
        }
    )


@dataclass
class Hardware(ProductType):
    """A hardware chassis or designation that is part of the specification of a
    benchmark platform.

    Examples: Cisco C3725, Juniper M7.
    """
    class Meta:
        name = "hardware"
        namespace = "http://www.cisecurity.org/xccdf/platform/0.2.3"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"hwr-[a-zA-Z0-9\-]+",
        }
    )


@dataclass
class Os(ProductType):
    """The operating system for a benchmark platform.

    Examples: Microsoft Windows XP, Sun Solaris, Cisco IOS.
    """
    class Meta:
        name = "os"
        namespace = "http://www.cisecurity.org/xccdf/platform/0.2.3"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"os-[a-zA-Z0-9\-]+",
        }
    )


@dataclass
class Service(ProductType):
    """A system or network service that is a component of a benchmark platform.

    Examples: Apache HTTPD,
    Microsoft Exchange, IBM MQSeries Message Server
    """
    class Meta:
        name = "service"
        namespace = "http://www.cisecurity.org/xccdf/platform/0.2.3"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"srv-[a-zA-Z0-9\-]+",
        }
    )


@dataclass
class PlatformDefinitions:
    """
    This element contains the individual application, service, os and hardware
    definitions which will be used in an a-la-cart fashion to define specific
    platform support rulesets.
    """
    class Meta:
        name = "platform-definitions"
        namespace = "http://www.cisecurity.org/xccdf/platform/0.2.3"

    application: List[Application] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    service: List[Service] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    os: List[Os] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    hardware: List[Hardware] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    platform_definition: List["PlatformDefinitions.PlatformDefinition"] = field(
        default_factory=list,
        metadata={
            "name": "platform-definition",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )

    @dataclass
    class PlatformDefinition:
        title: Optional[TextType] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        remark: List[TextType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            }
        )
        product: Optional[Product] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        logical_operator: Optional[LogicalOperator] = field(
            default=None,
            metadata={
                "name": "logical-operator",
                "type": "Element",
            }
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
