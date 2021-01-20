import datetime
from enum import Enum


class NoticeType:
    """
    Data type for an <xccdf:notice> element. <xccdf:notice> elements are used to include legal notices (licensing
    information, terms of use, etc.), copyright statements, warnings, and other advisory notices about this
    <xccdf:Benchmark> and its use. This information may be expressed using XHTML or may be a simply text expression.
    Each <xccdf:notice> element must have a unique identifier.
    """

    def __init__(
            self,
            xhtml: list = None,  # TODO: check xhtml content
            id_: str = None,
            base: str = None,
            lang: str = None
    ):
        """

        :param xhtml:
        :param id_: The unique identifier for this <xccdf:notice>.
        :param base:
        :param lang:
        """
        self.xhtml = xhtml
        self.id_ = id_
        self.base = base
        self.lang = lang


class DcStatusType:
    """
    Data type element for the <xccdf:dc-status> element, which holds status information about its parent element
    using the Dublin Core format, expressed as elements of the DCMI Simple DC Element specification.
    """

    def __init__(
            self,
            dc: list  # TODO: check dc content
    ):
        """

        :param dc:
        """
        self.dc = dc


class PlainTextType:
    """
    The data type for an <xccdf:plain-text> element, which is a reusable text block for reference by the <xccdf:sub>
    element. This allows text to be defined once and then reused multiple times. Each <xccdf:plain-text> element mush
    have a unique id.
    """

    def __init__(
            self,
            content: str,
            id_: str
    ):
        """

        :param content:
        :param id_: The unique identifier for this <xccdf:plain-text> element.
        """
        self.content = content
        self.id_ = id_


class ReferenceType:
    """
    This element provides supplementary descriptive text for a XCCDF elements. When used, it has either a simple
    string value or a value consisting of simple Dublin Core elements. If a bare string appears, then it is taken to
    be the string content for a Dublin Core title element. Multiple <xccdf:reference> elements may appear; a document
    generation processing tool may concatenate them, or put them into a reference list, and may choose to number them.
    """

    def __init__(
            self,
            dc: list = None,
            href: str = None,
            override: bool = None,
    ):
        """

        :param dc:
        :param href: A URL pointing to the referenced resource.
        :param override: Used to manage inheritance processing.
        """
        self.dc = dc
        self.href = href
        self.override = override


class SignatureType:
    """
    The type of an <XMLDSig:signature> element, which holds an enveloped digital signature asserting authorship and
    allowing verification of the integrity of associated data (e.g., its parent element, other documents, portions of
    other documents).
    """

    def __init__(
            self,
            xmldsig
    ):
        """

        :param xmldsig:
        """
        self.xmldsig = xmldsig


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

    def __init__(
            self,
            other: list
    ):
        """

        :param other:
        """
        self.other = other


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


class StatusType(Enum):
    """
    The statusType represents the possible levels of maturity or consensus level for its parent element as recorded
    by an <xccdf:status> element.
    """
    accepted = "accepted"  # Released as final
    deprecated = "deprecated"  # No longer needed
    draft = "draft"  # Released in draft state
    incomplete = "incomplete"  # Under initial development
    interim = "interim"  # Revised and in the process of being finalized


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


# Id types

class _IdType:
    _type = None

    def __init__(self, namespace, content):
        """

        :param namespace:
        :type namespace: str
        :param content:
        :type content: str
        """
        self.namespace = namespace
        self.content = content

    def __str__(self):
        if self._type is None:
            raise NotImplementedError
        return f"xccdf_{self.namespace}_{self._type}_{self.content}"


class BenchmarkIdType(_IdType):
    """
    The format required for the @id property of <xccdf:Benchmark> elements. xccdf_N_benchmark_S, where N is a
    reverse-DNS style namespace and S is an NCName-compatible string.
    """
    _type = "benchmark"


class RuleIdType(_IdType):
    """
    The format required for the @id property of <xccdf:Rule> elements. xccdf_N_rule_S, where N is a reverse-DNS style
    namespace and S is an NCName-compatible string.
    """
    _type = "rule"


class GroupIdType(_IdType):
    """
    The format required for the @id property of <xccdf:Group> elements. xccdf_N_group_S, where N is a reverse-DNS
    style namespace and S is an NCName-compatible string.
    """
    _type = "group"


class ValueIdType(_IdType):
    """
    The format required for the @id property of <xccdf:Value> elements. xccdf_N_value_S, where N is a reverse-DNS
    style namespace and S is an NCName-compatible string.
    """
    _type = "value"


class ProfileIdType(_IdType):
    """
    The format required for the @id property of <xccdf:Profile> elements. xccdf_N_profile_S, where N is a reverse-DNS
    style namespace and S is an NCName-compatible string.
    """
    _type = "profile"


class TestResultIdType(_IdType):
    """
    The format required for the @id property of <xccdf:TestResult> elements. xccdf_N_testresult_S, where N is a
    reverse-DNS style namespace and S is an NCName-compatible string.
    """
    _type = "testresult"


class TailoringIdType(_IdType):
    """
    The format required for the @id property of <xccdf:Tailoring> elements. xccdf_N_tailoring_S, where N is a
    reverse-DNS style namespace and S is an NCName-compatible string.
    """
    _type = "tailoring"


# Idref types


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


class SubUseEnumType(Enum):
    """
    This holds the possible values of the @use attribute within an <xccdf:sub> element. The @use attribute is only
    applicable with the subType's @idref attribute holds the value of the @id of an <xccdf:Value> element.
    """
    value = "value"  # Replace with the selected <xccdf:value> or <xccdf:complex-value> of an <xccdf:Value>.
    title = "title"  # Replace with the <xccdf:title> of the <xccdf:Value>.
    legacy = "legacy"  # Use the context-dependent processing of <xccdf:sub> elements outlined in XCCDF 1.1.4.


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


class HtmlTextWithSubType:
    """
    The type for a string with optional XHTML elements, and an @xml:lang attribute.
    """

    def __init__(
            self,
            sub: list[SubType] = None,
            xhtml: list = None,  # TODO: check xhtml content
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
            xhtml: list = None,  # TODO: check xhtml content
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
