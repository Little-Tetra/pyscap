from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional


@dataclass
class DelegatePublic:
    class Meta:
        name = "delegatePublic"
        namespace = "urn:oasis:names:tc:entity:xmlns:xml:catalog"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
    public_id_start_string: Optional[str] = field(
        default=None,
        metadata={
            "name": "publicIdStartString",
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z0-9\-'\(\)+,./:=?;!*#@$_%]*",
        }
    )
    catalog: Optional[str] = field(
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
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
            "required": True,
        }
    )


@dataclass
class DelegateSystem:
    class Meta:
        name = "delegateSystem"
        namespace = "urn:oasis:names:tc:entity:xmlns:xml:catalog"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
    system_id_start_string: Optional[str] = field(
        default=None,
        metadata={
            "name": "systemIdStartString",
            "type": "Attribute",
            "required": True,
        }
    )
    catalog: Optional[str] = field(
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
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
            "required": True,
        }
    )


@dataclass
class DelegateUri:
    class Meta:
        name = "delegateURI"
        namespace = "urn:oasis:names:tc:entity:xmlns:xml:catalog"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
    uri_start_string: Optional[str] = field(
        default=None,
        metadata={
            "name": "uriStartString",
            "type": "Attribute",
            "required": True,
        }
    )
    catalog: Optional[str] = field(
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
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
            "required": True,
        }
    )


@dataclass
class NextCatalog:
    class Meta:
        name = "nextCatalog"
        namespace = "urn:oasis:names:tc:entity:xmlns:xml:catalog"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
    catalog: Optional[str] = field(
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
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
            "required": True,
        }
    )


@dataclass
class Public:
    class Meta:
        name = "public"
        namespace = "urn:oasis:names:tc:entity:xmlns:xml:catalog"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
    public_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "publicId",
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z0-9\-'\(\)+,./:=?;!*#@$_%]*",
        }
    )
    uri: Optional[str] = field(
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
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
            "required": True,
        }
    )


@dataclass
class RewriteSystem:
    class Meta:
        name = "rewriteSystem"
        namespace = "urn:oasis:names:tc:entity:xmlns:xml:catalog"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
    system_id_start_string: Optional[str] = field(
        default=None,
        metadata={
            "name": "systemIdStartString",
            "type": "Attribute",
            "required": True,
        }
    )
    rewrite_prefix: Optional[str] = field(
        default=None,
        metadata={
            "name": "rewritePrefix",
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
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
            "required": True,
        }
    )


@dataclass
class RewriteUri:
    class Meta:
        name = "rewriteURI"
        namespace = "urn:oasis:names:tc:entity:xmlns:xml:catalog"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
    uri_start_string: Optional[str] = field(
        default=None,
        metadata={
            "name": "uriStartString",
            "type": "Attribute",
            "required": True,
        }
    )
    rewrite_prefix: Optional[str] = field(
        default=None,
        metadata={
            "name": "rewritePrefix",
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
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
            "required": True,
        }
    )


@dataclass
class System:
    class Meta:
        name = "system"
        namespace = "urn:oasis:names:tc:entity:xmlns:xml:catalog"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
    system_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "systemId",
            "type": "Attribute",
            "required": True,
        }
    )
    uri: Optional[str] = field(
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
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
            "required": True,
        }
    )


class SystemOrPublic(Enum):
    SYSTEM = "system"
    PUBLIC = "public"


@dataclass
class SystemSuffix:
    class Meta:
        name = "systemSuffix"
        namespace = "urn:oasis:names:tc:entity:xmlns:xml:catalog"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
    system_id_suffix: Optional[str] = field(
        default=None,
        metadata={
            "name": "systemIdSuffix",
            "type": "Attribute",
            "required": True,
        }
    )
    uri: Optional[str] = field(
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
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
            "required": True,
        }
    )


@dataclass
class Uri:
    class Meta:
        name = "uri"
        namespace = "urn:oasis:names:tc:entity:xmlns:xml:catalog"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    uri: Optional[str] = field(
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
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
            "required": True,
        }
    )


@dataclass
class UriSuffix:
    class Meta:
        name = "uriSuffix"
        namespace = "urn:oasis:names:tc:entity:xmlns:xml:catalog"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
    uri_suffix: Optional[str] = field(
        default=None,
        metadata={
            "name": "uriSuffix",
            "type": "Attribute",
            "required": True,
        }
    )
    uri: Optional[str] = field(
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
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
            "required": True,
        }
    )


@dataclass
class Group:
    class Meta:
        name = "group"
        namespace = "urn:oasis:names:tc:entity:xmlns:xml:catalog"

    public: List[Public] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    system: List[System] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    uri: List[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    rewrite_system: List[RewriteSystem] = field(
        default_factory=list,
        metadata={
            "name": "rewriteSystem",
            "type": "Element",
        }
    )
    rewrite_uri: List[RewriteUri] = field(
        default_factory=list,
        metadata={
            "name": "rewriteURI",
            "type": "Element",
        }
    )
    uri_suffix: List[UriSuffix] = field(
        default_factory=list,
        metadata={
            "name": "uriSuffix",
            "type": "Element",
        }
    )
    system_suffix: List[SystemSuffix] = field(
        default_factory=list,
        metadata={
            "name": "systemSuffix",
            "type": "Element",
        }
    )
    delegate_public: List[DelegatePublic] = field(
        default_factory=list,
        metadata={
            "name": "delegatePublic",
            "type": "Element",
        }
    )
    delegate_system: List[DelegateSystem] = field(
        default_factory=list,
        metadata={
            "name": "delegateSystem",
            "type": "Element",
        }
    )
    delegate_uri: List[DelegateUri] = field(
        default_factory=list,
        metadata={
            "name": "delegateURI",
            "type": "Element",
        }
    )
    next_catalog: List[NextCatalog] = field(
        default_factory=list,
        metadata={
            "name": "nextCatalog",
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
    prefer: Optional[SystemOrPublic] = field(
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
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
            "required": True,
        }
    )


@dataclass
class Catalog:
    class Meta:
        name = "catalog"
        namespace = "urn:oasis:names:tc:entity:xmlns:xml:catalog"

    public: List[Public] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    system: List[System] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    uri: List[Uri] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    rewrite_system: List[RewriteSystem] = field(
        default_factory=list,
        metadata={
            "name": "rewriteSystem",
            "type": "Element",
        }
    )
    rewrite_uri: List[RewriteUri] = field(
        default_factory=list,
        metadata={
            "name": "rewriteURI",
            "type": "Element",
        }
    )
    uri_suffix: List[UriSuffix] = field(
        default_factory=list,
        metadata={
            "name": "uriSuffix",
            "type": "Element",
        }
    )
    system_suffix: List[SystemSuffix] = field(
        default_factory=list,
        metadata={
            "name": "systemSuffix",
            "type": "Element",
        }
    )
    delegate_public: List[DelegatePublic] = field(
        default_factory=list,
        metadata={
            "name": "delegatePublic",
            "type": "Element",
        }
    )
    delegate_system: List[DelegateSystem] = field(
        default_factory=list,
        metadata={
            "name": "delegateSystem",
            "type": "Element",
        }
    )
    delegate_uri: List[DelegateUri] = field(
        default_factory=list,
        metadata={
            "name": "delegateURI",
            "type": "Element",
        }
    )
    next_catalog: List[NextCatalog] = field(
        default_factory=list,
        metadata={
            "name": "nextCatalog",
            "type": "Element",
        }
    )
    group: List[Group] = field(
        default_factory=list,
        metadata={
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    prefer: Optional[SystemOrPublic] = field(
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
            "required": True,
        }
    )
