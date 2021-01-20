import datetime

from .enums import *


# Text types

class TextType:
    """
    Type for a simple text string with an @override attribute for controlling inheritance.
    """

    def __init__(
            self,
            content: str,
            lang: str = None,
            override: bool = False
    ):
        """

        :param content: The content of the element.
        :param lang:
        :param override: Used to manage inheritance.
        """

        self.content = content
        self.lang = lang
        self.override = override


class HtmlTextType:
    """
    The type for a string with optional XHTML elements and an @xml:lang attribute.
    """

    def __init__(
            self,
            xhtml: list = None,  # TODO: check xhtml content
            lang: str = None,
            override: bool = False
    ):
        """

        :param xhtml: The xhtml content.
        :param lang:
        :param override: Used to manage inheritance.
        """
        if xhtml is None:
            xhtml = []

        self.xhtml = xhtml
        self.lang = lang
        self.override = override


class IdrefType:
    """
    Data type for elements that contain a reference to another XCCDF element
    """

    def __init__(
            self,
            idref: str
    ):
        """

        :param idref: The id value of another XCCDF element
        """
        self.idref = idref


class IdrefListType:
    """
    Data type for elements contain list of references to other XCCDF elements
    """

    def __init__(
            self,
            idref: str
    ):
        """

        :param idref: A space-separated list of id values from other XCCDF elements
        """
        self.idref = idref


class CPE2idrefType:
    """
    Data type for <xccdf:platform> elements that do not need @override attributes. (I.e., <xccdf:platform> elements
    that are in structures that cannot be extended, such as <xccdf:TestResult> and <xccdf:Benchmark> elements.) This
    is used to identify the applicable target platform for its respective parent elements.
    """

    def __init__(
            self,
            idref: str
    ):
        """

        :param idref: Should be a CPE 2.3 Applicability Language identifier using the Formatted String binding or the value of a <cpe:platform-specification> element's @id attribute, the latter acting as a reference to some expression defined using the CPE schema in the <xccdf:Benchmark> element's <cpe:platform-specification> element. The @idref may be a CPE Applicability Language identifier using the URI binding, although this is less preferred.
        """
        self.idref = idref


class OverrideableCPE2idrefType(CPE2idrefType):
    """
    Data type for <xccdf:platform> elements that need @override attributes. (I.e., <xccdf:platform> elements that are
    in structures that can be extended, such as Items and <xccdf:Profile> elements.) This is used to identify the
    applicable target platform for its respective parent elements.
    """

    def __init__(
            self,
            override: bool = False,
            **kwargs
    ):
        """

        :param override: Used to manage inheritance.
        """
        super().__init__(**kwargs)
        self.override = override


class SubType(IdrefType):
    """
    The type used for <xccdf:sub> elements. The <xccdf:sub> element identifies replacement content that should appear
    in place of the <xccdf:sub> element during text substitution. The subType consists of a regular idrefType with an
    additional @use attribute to dictate the behavior of the <xccdf:sub> element under substitution. When the @idref
    is to an <xccdf:Value>, the @use attribute indicates whether the <xccdf:Value> element's title or value should
    replace the <xccdf:sub> element. The @use attribute is ignored when the @idref is to an <xccdf:plain-text>
    element; the body of the <xccdf:plain-text> element is always used to replace the <xccdf:sub> element.
    """

    def __init__(
            self,
            use: SubUseEnumType = SubUseEnumType.value,
            **kwargs
    ):
        """

        :param use: Dictates the nature of the content inserted under text substitution processing.
        """
        super().__init__(**kwargs)
        self.use = use


class HtmlTextWithSubType:
    """
    The type for a string with optional XHTML elements, and an @xml:lang attribute.
    """

    def __init__(
            self,
            sub: list[SubType] = None,
            xhtml: list = None,
            lang: str = None,
            override: bool = False
    ):
        """

        :param sub: Specifies an <xccdf:Value> or <xccdf:plain-text> element to be used for text substitution.
        :param xhtml:  The xhtml content.
        :param lang:
        :param override: Used to manage inheritance.
        """
        if sub is None:
            sub = []
        if xhtml is None:
            xhtml = []

        self.sub = sub
        self.xhtml = xhtml
        self.lang = lang
        self.override = override


class ProfileNoteType:
    """
    Type for an <xccdf:profile-note> within an <xccdf:Rule>. This element contains text that describes special
    aspects of an <xccdf:Rule> relative to one or more <xccdf:Profile> elements. This allows an author to document
    things within <xccdf:Rule> elements that are specific to a given <xccdf:Profile>. This information might then be
    displayed to a reader based on the selection of a particular <xccdf:Profile>. The body text may include XHTML
    mark-up as well as <xccdf:sub> elements.
    """

    def __init__(
            self,
            tag: str,
            sub: list[SubType] = None,
            xhtml: list = None,
            lang: str = None
    ):
        """

        :param tag: The identifier of this note.
        :param sub: Specifies an <xccdf:Value> or <xccdf:plain-text> element to be used for text substitution.
        :param xhtml:  The xhtml content.
        :param lang:
        """
        if sub is None:
            sub = []
        if xhtml is None:
            xhtml = []

        self.tag = tag
        self.sub = sub
        self.xhtml = xhtml
        self.lang = lang


class TextWithSubType:
    """
    Type for a string with embedded <xccdf:Value> substitutions and an @override attribute to help manage inheritance.
    """

    def __init__(
            self,
            sub: list[SubType] = None,
            lang: str = None,
            override: bool = False
    ):
        """

        :param sub: Specifies an <xccdf:Value> or <xccdf:plain-text> element to be used for text substitution.
        :param lang:
        :param override: Used to manage inheritance.
        """
        if sub is None:
            sub = []

        self.sub = sub
        self.lang = lang
        self.override = override


# Benchmark types

class NoticeType:
    """
    Data type for an <xccdf:notice> element. <xccdf:notice> elements are used to include legal notices (licensing
    information, terms of use, etc.), copyright statements, warnings, and other advisory notices about this
    <xccdf:Benchmark> and its use. This information may be expressed using XHTML or may be a simply text expression.
    Each <xccdf:notice> element must have a unique identifier.
    """


class DcStatusType:
    """
    Data type element for the <xccdf:dc-status> element, which holds status information about its parent element
    using the Dublin Core format, expressed as elements of the DCMI Simple DC Element specification.
    """


class PlainTextType:
    """
    The data type for an <xccdf:plain-text> element, which is a reusable text block for reference by the <xccdf:sub>
    element. This allows text to be defined once and then reused multiple times. Each <xccdf:plain-text> element mush
    have a unique id.
    """


class ReferenceType:
    """
    This element provides supplementary descriptive text for a XCCDF elements. When used, it has either a simple
    string value or a value consisting of simple Dublin Core elements. If a bare string appears, then it is taken to
    be the string content for a Dublin Core title element. Multiple <xccdf:reference> elements may appear; a document
    generation processing tool may concatenate them, or put them into a reference list, and may choose to number them.
    """


class SignatureType:
    """
    The type of an <XMLDSig:signature> element, which holds an enveloped digital signature asserting authorship and
    allowing verification of the integrity of associated data (e.g., its parent element, other documents, portions of
    other documents).
    """


class MetadataType:
    """
    Data type that supports inclusion of metadata about a document or element. This is particularly useful for
    facilitating the discovery and retrieval of XCCDF checklists from public repositories. When used, the contents of
    the <xccdf:metadata> element are expressed in XML. The <xccdf:Benchmark> element's metadata should contain
    information formatted using the Dublin Core Metadata Initiative (DCMI) Simple DC Element specification,
    as described in [DCES] and [DCXML]. Benchmark consumers should be prepared to process Dublin Core metadata in the
    <xccdf:metadata> element. Other metadata schemes, including ad-hoc elements, are also allowed, both in the
    <xccdf:Benchmark> and in other elements.
    """


# Global types


class ParamType:
    """
    Type for a parameter used in the <xccdf:model> element, which records scoring model information. The contents of
    this type represent a name-value pair, where the name is recorded in the @name attribute and the value appears in
    the element body. <xccdf:param> elements with equal values for the @name attribute may not appear as children of
    the same <xccdf:model> element.
    """

    def __init__(
            self,
            content: str,
            name: str
    ):
        """

        :param content: The content of the element.
        :param name: The name associated with the contained value.
        """
        self.content = content
        self.name = name


class VersionType:
    """
    Type for most <xccdf:version> elements.
    """

    def __init__(
            self,
            content: str,
            time: datetime.datetime = None,
            update: str = None
    ):
        """

        :param content: The content of the element.
        :param time: The time that this version of the associated element was completed.
        :param update: A URI indicating a location where updates to the associated element may be obtained.
        """
        self.content = content
        self.time = time
        self.update = update


# Global elements


class Status:
    """
    The acceptance status of an element with an optional date attribute, which signifies the date of the status
    change. If an element does not have its own <xccdf:status> element, its status is that of its parent element. If
    there is more than one <xccdf:status> for a single element, then every instance of the <xccdf:status> element
    must have a @date attribute, and the <xccdf:status> element with the latest date is considered the current status.
    """

    def __init__(
            self,
            content: StatusType,
            date: datetime.date = None
    ):
        """

        :param content: The content of the element
        :param date: The date the parent element achieved the indicated status.
        """
        self.content = content
        self.date = date


class Model:
    """
    A suggested scoring model for an <xccdf:Benchmark>, also encapsulating any parameters needed by the model. Every
    model is designated with a URI, which appears here as the system attribute. See the XCCDF specification for a
    list of standard scoring models and their associated URIs. Vendors may define their own scoring models and
    provide additional URIs to designate them. Some models may need additional parameters; to support such a model,
    zero or more <xccdf:param> elements may appear as children of the <xccdf:model> element.
    """

    def __init__(
            self,
            system: str,
            param: list[ParamType] = None
    ):
        """

        :param system: A URI designating a scoring model.
        :param param: Parameters provided as input to the designated scoring model.
        """
        if param is None:
            param = []

        self.system = system
        self.param = param


# Base types

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
            version=None,
            title=None,
            description=None,
            warning=None,
            question=None,
            reference=None,
            metadata=None,
            abstract=False,
            cluster_id=None,
            extends=None,
            hidden=False,
            prohibit_changes=False,
            lang=None,
            base=None,
            xml_id=None
    ):
        """

        :param status: Status of the item and date at which it attained that status. <xccdf:Benchmark> authors may use this element to record the maturity or consensus level for elements in the <xccdf:Benchmark>. If an item does not have an explicit <xccdf:status> given, then its status is that of its parent.
        :param dc_status: Holds additional status information using the Dublin Core format.
        :param version: Version information about this item.
        :type version: VersionType
        :param title: Title of the item. Every item should have an <xccdf:title>, because this helps people understand the purpose of the item.
        :type title: list[TextWithSubType]
        :param description: Text that describes the item.
        :type description: list[HtmlTextWithSubType]
        :param warning: A note or caveat about the item intended to convey important cautionary information for the <xccdf:Benchmark> user (e.g., “Complying with this rule will cause the system to reject all IP packets”). If multiple <xccdf:warning> elements appear, benchmark consumers should concatenate them for generating reports or documents. Benchmark consumers may present this information in a special manner in generated documents.
        :type warning: list[WarningType]
        :param question: Interrogative text to present to the user during tailoring. It may also be included into a generated document. For <xccdf:Rule> and <xccdf:Group> elements, the <xccdf:question> text should be a simple binary (yes/no) question because it is supporting the selection aspect of tailoring. For <xccdf:Value> elements, the <xccdf:question> should solicit the user to provide a specific value. Tools may also display constraints on values and any defaults as specified by the other <xccdf:Value> properties.
        :type question: list[TextType]
        :param reference: References where the user can learn more about the subject of this item.
        :type reference: list[ReferenceType]
        :param metadata: XML metadata associated with this item, such as sources, special information, or other details.
        :type metadata: list[MetadataType]
        :param abstract: If true, then this item is abstract and exists only to be extended. The use of this attribute for <xccdf:Group> elements is deprecated and should be avoided.
        :type abstract: bool
        :param cluster_id: An identifier to be used as a means to identify (refer to) related items. It designates membership in a cluster of items, which are used for controlling items via <xccdf:Profile> elements. All the items with the same cluster identifier belong to the same cluster. A selector in an <xccdf:Profile> may refer to a cluster, thus making it easier for authors to create and maintain <xccdf:Profile> elements in a complex <xccdf:Benchmark>.
        :type cluster_id: str
        :param extends: The identifier of an item on which to base this item. If present, it must have a value equal to the @id attribute of another item. The use of this attribute for <xccdf:Group> elements is deprecated and should be avoided.
        :type extends: str
        :param hidden: If this item should be excluded from any generated documents although it may still be used during assessments.
        :type hidden: bool
        :param prohibit_changes: If benchmark producers should prohibit changes to this item during tailoring. An author should use this when they do not want to allow end users to change the item.
        :type prohibit_changes: bool
        :param lang:
        :type lang: str
        :param base:
        :type base: str
        :param xml_id: An identifier used for referencing elements included in an XML signature
        :type xml_id: str
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


class SelectableItemType(ItemType):
    """
    This abstract item type represents the basic data shared by all <xccdf:Group> and <xccdf:Rule> elements.
    """


# Base elements

class Item(ItemType):
    """
    An item is a named constituent of an <xccdf:Benchmark>. There are three types of items: <xccdf:Group>,
    <xccdf:Rule> and <xccdf:Value>. The <xccdf:Item> element type imposes constraints shared by all <xccdf:Group>,
    <xccdf:Rule> and <xccdf:Value> elements. The itemType is abstract, so the element <xccdf:Item> can never appear
    in a valid XCCDF document.
    """
