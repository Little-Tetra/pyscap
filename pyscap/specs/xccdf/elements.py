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


# Base elements

class ItemType:
    """
    This abstract itemType represents the basic data shared by all <xccdf:Group>, <xccdf:Rule> and <xccdf:Value>
    elements. All elements in an itemType are optional, although each element that builds on the itemType may add its
    own elements, some of which will be required for that element.
    """


class Item(ItemType):
    """
    An item is a named constituent of an <xccdf:Benchmark>. There are three types of items: <xccdf:Group>,
    <xccdf:Rule> and <xccdf:Value>. The <xccdf:Item> element type imposes constraints shared by all <xccdf:Group>,
    <xccdf:Rule> and <xccdf:Value> elements. The itemType is abstract, so the element <xccdf:Item> can never appear
    in a valid XCCDF document.
    """


class SelectableItemType(ItemType):
    """
    This abstract item type represents the basic data shared by all <xccdf:Group> and <xccdf:Rule> elements.
    """


# Main elements

class GroupType(SelectableItemType):
    """
    Data type for the <xccdf:Group> element. A <xccdf:Group> element contains descriptive information about a portion
    of an <xccdf:Benchmark>, as well as <xccdf:Rule>, <xccdf:Value>, and/or other <xccdf:Group> elements
    """


class Group(GroupType):
    """
    An item that can hold other items. It allows an author to collect related items into a common structure and
    provide descriptive text and references about them.
    """


class RuleType(SelectableItemType):
    """
    Data type for the <xccdf:Rule> element that represents a specific <xccdf:Benchmark> test.
    """


class Rule(RuleType):
    """
    The <xccdf:Rule> element contains the description for a single item of guidance or constraint. <xccdf:Rule>
    elements form the basis for testing a target platform for compliance with an <xccdf:Benchmark>, for scoring,
    and for conveying descriptive prose, identifiers, references, and remediation information.
    """


class ValueType(ItemType):
    """
    Data type for the <xccdf:Value> element, which is a named parameter that can be substituted into properties of
    other elements within the <xccdf:Benchmark>, including the interior of structured check specifications and fix
    scripts.
    """


class Value(ValueType):
    """
    The <xccdf:Value> element is a named parameter that can be substituted into properties of other elements within
    the <xccdf:Benchmark>, including the interior of structured check specifications and fix scripts.
    """


class ProfileType:
    """
    Data type for the <xccdf:Profile> element, which holds a specific tailoring of the <xccdf:Benchmark>. The main
    part of an <xccdf:Profile> is the selectors: <xccdf:select>, <xccdf:set-value>, <xccdf:set-complex-value>,
    <xccdf:refine-rule>, and <xccdf:refine-value>. An <xccdf:Profile> may also be signed with an XML-Signature.
    """


class Profile(ProfileType):
    """
    The <xccdf:Profile> element is a named tailoring for an <xccdf:Benchmark>. While an <xccdf:Benchmark> can be
    tailored in place by setting properties of various elements, <xccdf:Profile> elements allow one <xccdf:Benchmark>
    document to hold several independent tailorings.
    """


class TestResultType:
    """
    Data type for the <xccdf:TestResult> element, which holds the results of one application of the
    <xccdf:Benchmark>. The <xccdf:TestResult> element normally appears as the child of the <xccdf:Benchmark> element,
    although it may also appear as the top-level element of an XCCDF results document. XCCDF is not intended to be a
    database format for detailed results; the <xccdf:TestResult> element offers a way to store the results of
    individual tests in modest detail, with the ability to reference lower-level testing data. Although several of
    the child elements of this type technically support the @override attribute, the <xccdf:TestResult> element
    cannot be extended. Therefore, @override has no meaning within an <xccdf:TestResult> element and its children,
    and should not be used for them.
    """


class TestResult(TestResultType):
    """
    The <xccdf:TestResult> element encapsulates the results of a single application of an <xccdf:Benchmark> to a
    single target platform. The <xccdf:TestResult> element normally appears as the child of the <xccdf:Benchmark>
    element, although it may also appear as the top-level element of an XCCDF results document. XCCDF is not intended
    to be a database format for detailed results; the <xccdf:TestResult> element offers a way to store the results of
    individual tests in modest detail, with the ability to reference lower-level testing data.
    """


class TailoringType:
    """
    Data type for the <xccdf:Tailoring> element. The <xccdf:Tailoring> element allows named tailorings (i.e.,
    <xccdf:Profile> elements) of an <xccdf:Benchmark> to be defined separately from the <xccdf:Benchmark> itself. The
    <xccdf:Profile> elements in an <xccdf:Tailoring> element can be used in two ways: First, an organization might
    wish to pre-define a set of tailoring actions to be applied on top of or instead of the tailoring performed by an
    <xccdf:Benchmark> element's <xccdf:Profile> elements. Second, an <xccdf:Tailoring> element can be used to record
    manual tailoring actions performed during the course of an assessment.
    """


class Tailoring(TailoringType):
    """
    The <xccdf:Tailoring> element holds one or more <xccdf:Profile> elements. These <xccdf:Profile> elements record
    additional tailoring activities that apply to a given <xccdf:Benchmark>. <xccdf:Tailoring> elements are separate
    from <xccdf:Benchmark> documents, but each <xccdf:Tailoring> element is associated with a specific
    <xccdf:Benchmark> document. By defining these tailoring actions separately from the <xccdf:Benchmark> document to
    which they apply, these actions can be recorded without affecting the integrity of the source itself.
    """


# Root element

class Benchmark:
    """
    This is the root element of the XCCDF document; it must appear exactly once. It encloses the entire benchmark,
    and contains both descriptive information and structural information. Note that the order of <xccdf:Group> and
    <xccdf:Rule> child elements may matter for the appearance of a generated document. <xccdf:Group> and <xccdf:Rule>
    children may be freely intermingled, but they must appear after any <xccdf:Value> children. All the other
    children must appear in the order shown.
    """
