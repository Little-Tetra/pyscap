from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

from .common import (
    TextWithSubType,
    HtmlTextWithSubType,
    TextType,
    OverrideableCpe2IdrefType,
    IdrefListType, IdrefType,
    Status,
    VersionType
)
from .components import DcStatusType, WarningType, ReferenceType, MetadataType


# Item type

@dataclass
class ItemType:
    """This abstract itemType represents the basic data shared by all
    <xccdf:Group>, <xccdf:Rule> and <xccdf:Value> elements.

    All elements in an itemType are optional, although each element that
    builds on the itemType may add its own elements, some of which will
    be required for that element.

    :ivar status: Status of the item and date at which it
        attained that status. <xccdf:Benchmark> authors may use
        this element                         to record the maturity or
        consensus level for elements in the
        <xccdf:Benchmark>. If an item does not have an explicit
        <xccdf:status> given, then its status is that of its
        parent.
    :ivar dc_status: Holds additional status information using the
        Dublin Core format.
    :ivar version: Version information about this item.
    :ivar title: Title of the item. Every item should have an
        <xccdf:title>, because this helps people understand the
        purpose of the                         item.
    :ivar description: Text that describes the item.
    :ivar warning: A note or caveat about the item intended to
        convey important cautionary information for the
        <xccdf:Benchmark> user                         (e.g.,
        “Complying with this rule will cause the system to reject all IP
        packets”). If multiple <xccdf:warning> elements appear,
        benchmark                         consumers should concatenate
        them for generating reports or documents.
        Benchmark consumers may present this information in a special
        manner in                         generated documents.
    :ivar question: Interrogative text to present to the user
        during tailoring. It may also be included into a generated
        document. For                         <xccdf:Rule> and
        <xccdf:Group> elements, the
        <xccdf:question> text should be a simple binary (yes/no)
        question                         because it is supporting the
        selection aspect of tailoring. For
        <xccdf:Value> elements, the <xccdf:question> should
        solicit the                         user to provide a specific
        value. Tools may also display constraints on
        values and any defaults as specified by the other
        <xccdf:Value>                         properties.
    :ivar reference: References where the user can learn more about
        the subject of this item.
    :ivar metadata: XML metadata associated with this item, such as
        sources, special information, or other details.
    :ivar abstract: If true, then this item is abstract and exists only
        to be extended. The use of this attribute for
        <xccdf:Group> elements is                     deprecated
        and should be avoided.
    :ivar cluster_id: An identifier to be used as a means to identify
        (refer to) related items. It designates membership in a cluster
        of items, which                     are used for controlling
        items via <xccdf:Profile> elements. All the items
        with the same cluster identifier belong to the same cluster. A
        selector in an                     <xccdf:Profile> may
        refer to a cluster, thus making it easier for authors
        to create and maintain <xccdf:Profile> elements in a
        complex                     <xccdf:Benchmark>.
    :ivar extends: The identifier of an item on which to base this
        item. If present, it must have a value equal to the @id
        attribute of another                     item. The use of this
        attribute for <xccdf:Group> elements is deprecated
        and should be avoided.
    :ivar hidden: If this item should be excluded from any generated
        documents although it may still be used during assessments.
    :ivar prohibit_changes: If benchmark producers should prohibit
        changes to                     this item during tailoring. An
        author should use this when they do not want to
        allow end users to change the item.
    :ivar lang:
    :ivar base:
    :ivar id: An identifier used for referencing elements
        included in an XML signature
    """

    class Meta:
        name = "itemType"

    status: List[Status] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://checklists.nist.gov/xccdf/1.2",
        }
    )
    dc_status: List[DcStatusType] = field(
        default_factory=list,
        metadata={
            "name": "dc-status",
            "type": "Element",
            "namespace": "",
        }
    )
    version: Optional[VersionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    title: List[TextWithSubType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    description: List[HtmlTextWithSubType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    warning: List[WarningType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    question: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    reference: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    metadata: List[MetadataType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    abstract: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    cluster_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "cluster-id",
            "type": "Attribute",
        }
    )
    extends: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    hidden: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    prohibit_changes: bool = field(
        default=False,
        metadata={
            "name": "prohibitChanges",
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class Item(ItemType):
    """An item is a named constituent of an.

    <xccdf:Benchmark>. There are three types of items:
    <xccdf:Group>, <xccdf:Rule> and <xccdf:Value>. The
    <xccdf:Item> element type imposes constraints shared by all
    <xccdf:Group>, <xccdf:Rule> and <xccdf:Value>
    elements. The itemType is abstract, so the element
    <xccdf:Item> can never appear in a valid XCCDF document.
    """

    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"


# Selectable item type

@dataclass
class SelectableItemType(ItemType):
    """
    This abstract item type represents the basic data shared by all
    <xccdf:Group> and <xccdf:Rule> elements.

    :ivar rationale: Descriptive text giving rationale or
        motivations for abiding by this
        <xccdf:Group>/<xccdf:Rule> (i.e., why it is
        important to                                 the security of the
        target platform).
    :ivar platform: Platforms to which this
        <xccdf:Group>/<xccdf:Rule> applies.
    :ivar requires: The identifiers of other
        <xccdf:Group> or <xccdf:Rule> elements that must be
        selected for this <xccdf:Group>/<xccdf:Rule> to be
        evaluated and scored properly. Each <xccdf:requires>
        element                                 specifies a list of one
        or more required items by their identifiers.
        If at least one of the specified <xccdf:Group> or
        <xccdf:Rule> elements is selected, the requirement is met.
    :ivar conflicts: The identifier of another
        <xccdf:Group> or <xccdf:Rule> that must be
        unselected                                 for this
        <xccdf:Group>/<xccdf:Rule> to be evaluated and
        scored properly. Each <xccdf:conflicts> element specifies
        a                                 single conflicting item using
        its idref attribute. If the specified
        <xccdf:Group> or <xccdf:Rule> element is not
        selected,                                 the requirement is
        met.
    :ivar selected: If true, this
        <xccdf:Group>/<xccdf:Rule> is selected to be
        processed as                             part of the
        <xccdf:Benchmark> when it is applied to a target
        system. An unselected <xccdf:Group> does not get
        processed, and                             its contents are not
        processed either (i.e., all descendants of an
        unselected <xccdf:Group> are implicitly unselected). An
        unselected                             <xccdf:Rule> is not
        checked and does not contribute to scoring.
    :ivar weight: The relative scoring weight of this
        <xccdf:Group>/<xccdf:Rule>, for computing a score,
        expressed                             as a non-negative real
        number. It denotes the importance of an
        <xccdf:Group>/<xccdf:Rule>. Under some scoring
        models,                             scoring is computed
        independently for each collection of sibling
        <xccdf:Group> and <xccdf:Rule> elements, then
        normalized as                             part of the overall
        scoring process.
    """

    class Meta:
        name = "selectableItemType"

    rationale: List[HtmlTextWithSubType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    platform: List[OverrideableCpe2IdrefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    requires: List[IdrefListType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    conflicts: List[IdrefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    selected: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    weight: Decimal = field(
        default=Decimal("1.0"),
        metadata={
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "total_digits": 3,
        }
    )
