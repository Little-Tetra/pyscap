from .common import *


# Item element

class ItemType:
    """
    This abstract itemType represents the basic data shared by all <xccdf:Group>, <xccdf:Rule> and <xccdf:Value>
    elements. All elements in an itemType are optional, although each element that builds on the itemType may add its
    own elements, some of which will be required for that element.
    """

    def __init__(
            self,
            status: list[Status] = None,
            dc_status: list[DcStatusType] = None,
            version: VersionType = None,
            title: list[TextWithSubType] = None,
            description: list[HtmlTextWithSubType] = None,
            warning: list[WarningType] = None,
            question: list[TextType] = None,
            reference: list[ReferenceType] = None,
            metadata: list[MetadataType] = None,
            abstract: bool = False,
            cluster_id: str = None,
            extends: str = None,
            hidden: bool = False,
            prohibit_changes: bool = False,
            lang: str = None,
            base: str = None,
            xml_id: str = None
    ):
        """

        :param status: Status of the item and date at which it attained that status. <xccdf:Benchmark> authors may use this element to record the maturity or consensus level for elements in the <xccdf:Benchmark>. If an item does not have an explicit <xccdf:status> given, then its status is that of its parent.
        :param dc_status: Holds additional status information using the Dublin Core format.
        :param version: Version information about this item.
        :param title: Title of the item. Every item should have an <xccdf:title>, because this helps people understand the purpose of the item.
        :param description: Text that describes the item.
        :param warning: A note or caveat about the item intended to convey important cautionary information for the <xccdf:Benchmark> user (e.g., “Complying with this rule will cause the system to reject all IP packets”). If multiple <xccdf:warning> elements appear, benchmark consumers should concatenate them for generating reports or documents. Benchmark consumers may present this information in a special manner in generated documents.
        :param question: Interrogative text to present to the user during tailoring. It may also be included into a generated document. For <xccdf:Rule> and <xccdf:Group> elements, the <xccdf:question> text should be a simple binary (yes/no) question because it is supporting the selection aspect of tailoring. For <xccdf:Value> elements, the <xccdf:question> should solicit the user to provide a specific value. Tools may also display constraints on values and any defaults as specified by the other <xccdf:Value> properties.
        :param reference: References where the user can learn more about the subject of this item.
        :param metadata: XML metadata associated with this item, such as sources, special information, or other details.
        :param abstract: If true, then this item is abstract and exists only to be extended. The use of this attribute for <xccdf:Group> elements is deprecated and should be avoided.
        :param cluster_id: An identifier to be used as a means to identify (refer to) related items. It designates membership in a cluster of items, which are used for controlling items via <xccdf:Profile> elements. All the items with the same cluster identifier belong to the same cluster. A selector in an <xccdf:Profile> may refer to a cluster, thus making it easier for authors to create and maintain <xccdf:Profile> elements in a complex <xccdf:Benchmark>.
        :param extends: The identifier of an item on which to base this item. If present, it must have a value equal to the @id attribute of another item. The use of this attribute for <xccdf:Group> elements is deprecated and should be avoided.
        :param hidden: If this item should be excluded from any generated documents although it may still be used during assessments.
        :param prohibit_changes: If benchmark producers should prohibit changes to this item during tailoring. An author should use this when they do not want to allow end users to change the item.
        :param lang:
        :param base:
        :param xml_id: An identifier used for referencing elements included in an XML signature
        """
        if status is None:
            status = []
        if dc_status is None:
            dc_status = []
        if title is None:
            title = []
        if description is None:
            description = []
        if warning is None:
            warning = []
        if question is None:
            question = []
        if reference is None:
            reference = []
        if metadata is None:
            metadata = []

        self.status = status
        self.dc_status = dc_status
        self.version = version
        self.title = title
        self.description = description
        self.warning = warning
        self.question = question
        self.reference = reference
        self.metadata = metadata
        self.abstract = abstract
        self.cluster_id = cluster_id
        self.extends = extends
        self.hidden = hidden
        self.prohibit_changes = prohibit_changes
        self.lang = lang
        self.base = base
        self.xml_id = xml_id


class Item(ItemType):
    """
    An item is a named constituent of an <xccdf:Benchmark>. There are three types of items: <xccdf:Group>,
    <xccdf:Rule> and <xccdf:Value>. The <xccdf:Item> element type imposes constraints shared by all <xccdf:Group>,
    <xccdf:Rule> and <xccdf:Value> elements. The itemType is abstract, so the element <xccdf:Item> can never appear
    in a valid XCCDF document.
    """


# Selectable item type

class SelectableItemType(ItemType):
    """
    This abstract item type represents the basic data shared by all <xccdf:Group> and <xccdf:Rule> elements.
    """

    def __init__(
            self,
            rationale: list[HtmlTextWithSubType] = None,
            platform: list[OverrideableCPE2idrefType] = None,
            requires: list[IdrefListType] = None,
            conflicts: list[IdrefType] = None,
            selected: bool = True,
            weight: WeightType = WeightType(1.0),
            **kwargs
    ):
        """

        :param rationale: Descriptive text giving rationale or motivations for abiding by this <xccdf:Group>/<xccdf:Rule> (i.e., why it is important to the security of the target platform).
        :param platform: Platforms to which this <xccdf:Group>/<xccdf:Rule> applies.
        :param requires: The identifiers of other <xccdf:Group> or <xccdf:Rule> elements that must be selected for this <xccdf:Group>/<xccdf:Rule> to be evaluated and scored properly. Each <xccdf:requires> element specifies a list of one or more required items by their identifiers. If at least one of the specified <xccdf:Group> or <xccdf:Rule> elements is selected, the requirement is met.
        :param conflicts: The identifier of another <xccdf:Group> or <xccdf:Rule> that must be unselected for this <xccdf:Group>/<xccdf:Rule> to be evaluated and scored properly. Each <xccdf:conflicts> element specifies a single conflicting item using its idref attribute. If the specified <xccdf:Group> or <xccdf:Rule> element is not selected, the requirement is met.
        :param selected: If true, this <xccdf:Group>/<xccdf:Rule> is selected to be processed as part of the <xccdf:Benchmark> when it is applied to a target system. An unselected <xccdf:Group> does not get processed, and its contents are not processed either (i.e., all descendants of an unselected <xccdf:Group> are implicitly unselected). An unselected <xccdf:Rule> is not checked and does not contribute to scoring.
        :param weight: The relative scoring weight of this <xccdf:Group>/<xccdf:Rule>, for computing a score, expressed as a non-negative real number. It denotes the importance of an <xccdf:Group>/<xccdf:Rule>. Under some scoring models, scoring is computed independently for each collection of sibling <xccdf:Group> and <xccdf:Rule> elements, then normalized as part of the overall scoring process.
        """
        super().__init__(**kwargs)

        if rationale is None:
            rationale = []
        if platform is None:
            platform = []
        if requires is None:
            requires = []
        if conflicts is None:
            conflicts = []

        self.rationale = rationale
        self.platform = platform
        self.requires = requires
        self.conflicts = conflicts
        self.selected = selected
        self.weight = weight
