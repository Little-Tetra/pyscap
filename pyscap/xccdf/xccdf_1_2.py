from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional

from xsdata.models.datatype import XmlDate, XmlDateTime

from ..common.utils import ParsableElement
from ..cpe import PlatformSpecification

XCCDF_1_2_NAMESPACE = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class Cpe2Idref:
    """

    Data type for <xccdf:platform> elements that do not need @override attributes. (I.e., <xccdf:platform> elements
    that are in structures that cannot be extended, such as <xccdf:TestResult> and <xccdf:Benchmark> elements.) This
    is used to identify the applicable target platform for its respective parent elements.

    :ivar idref: Should be a CPE 2.3 Applicability Language identifier using the Formatted String binding or the value of a <cpe:platform-specification> element's @id attribute, the latter acting as a reference to some expression defined using the CPE schema in the <xccdf:Benchmark> element's <cpe:platform-specification> element. The @idref may be a CPE Applicability Language identifier using the URI binding, although this is less preferred.
    """

    class Meta:
        name = "CPE2idref"

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class BenchmarkReference:
    """

    Type for a reference to the <xccdf:Benchmark> document.

    :ivar href: The URI of the <xccdf:Benchmark> document.
    :ivar id: The value of that <xccdf:Benchmark> element's @id attribute.
    """

    class Meta:
        name = "benchmarkReference"

    href: Optional[str] = field(
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
        }
    )


class ComplexCheckOperator(Enum):
    """

    The type for the allowed @operator names for the <xccdf:complex-check> operator attribute. Only AND and OR
    operators are supported. (The <xccdf:complex-check> has a separate mechanism for negation.)

    :cvar OR: The logical OR of the component terms
    :cvar AND: The logical AND of the component terms
    """
    OR = "OR"
    AND = "AND"


@dataclass
class CheckContentRef:
    """

    Data type for the <xccdf:check-content-ref> element, which points to the code for a detached check in another
    file. This element has no body, just a couple of attributes: @href and @name. The @name is optional, if it does
    not appear then this reference is to the entire document.

    :ivar href: Identifies the referenced document containing checking instructions.
    :ivar name: Identifies a particular part or element of the referenced check document.
    """

    class Meta:
        name = "checkContentRef"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class CheckContent:
    """

    Data type for the <xccdf:check-content> element. The body of this element holds the actual code of a check,
    in the language or system specified by the <xccdf:check> element’s @system attribute. The body of this element
    may be any XML, but cannot contain any XCCDF elements. XCCDF tools do not process its content directly but
    instead pass the content directly to checking engines.
    """

    class Meta:
        name = "checkContent"

    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "mixed": True,
        }
    )


@dataclass
class CheckExport:
    """

    Data type for the <xccdf:check-export> element, which specifies a mapping from an <xccdf:Value> element to a
    checking system variable (i.e., external name or id for use by the checking system). This supports export of
    tailoring <xccdf:Value> elements from the XCCDF processing environment to the checking system. The interface
    between the XCCDF benchmark consumer and the checking system should support, at a minimum, passing the
    <xccdf:value> property of the <xccdf:Value> element, but may also support passing the <xccdf:Value>
    element's@type and @operator properties.

    :ivar value_id: The id of the <xccdf:Value> element to export.
    :ivar export_name: An identifier indicating some structure in the checking system into which the identified <xccdf:Value> element's properties will be mapped.
    """

    class Meta:
        name = "checkExport"

    value_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "value-id",
            "type": "Attribute",
            "required": True,
        }
    )
    export_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "export-name",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CheckImport:
    """

    Data type for the <xccdf:check-import> element, which specifies a value that the <xccdf:Benchmark> author wishes
    to retrieve from the checking system during testing of a target system. The @import-name attribute identifies
    some structure in the checking system that is then retrieved. The mapping from the values of this attribute to
    specific checking system structures is beyond the scope of the XCCDF specification. When the <xccdf:check-import>
    element appears in the context of an <xccdf:Rule>, then it should be empty and any content must be ignored. When
    the <xccdf:check-import> element appears in the context of an <xccdf:rule-result>, then its body holds the
    imported value.

    :ivar any_element:
    :ivar import_name: An identifier indicating some structure in the checking system to be collected.
    :ivar import_xpath: An XPath that is used to select specific values or structures from the imported structure. This allows further refinement of the collected data if the imported value takes the form of XML structures.
    """

    class Meta:
        name = "checkImport"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    import_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "import-name",
            "type": "Attribute",
            "required": True,
        }
    )
    import_xpath: Optional[str] = field(
        default=None,
        metadata={
            "name": "import-xpath",
            "type": "Attribute",
        }
    )


@dataclass
class ComplexValue:
    """

    Data type that supports values that are lists of simple types. Each element in the list is represented by an
    instance of the <xccdf:item> child element. If there are no <xccdf:item> child elements then this represents an
    empty list.

    :ivar item: A single item in the list of values.
    """

    class Meta:
        name = "complexValue"

    item: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class DcStatus:
    """

    Data type element for the <xccdf:dc-status> element, which holds status information about its parent element
    using the Dublin Core format, expressed as elements of the DCMI Simple DC Element specification.
    """

    class Meta:
        name = "dc-status"

    purl_org_dc_elements_1_1_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "min_occurs": 1,
        }
    )


class FixStrategy(Enum):
    """

    Allowed @strategy keyword values for an <xccdf:Rule> element's <xccdf:fix> or <xccdf:fixtext> elements. The
    values indicate the method or approach for fixing non-compliance with a particular <xccdf:Rule>.

    :cvar UNKNOWN: Strategy not defined (default)
    :cvar CONFIGURE: Adjust target configuration/settings
    :cvar COMBINATION: Combination of two or more approaches
    :cvar DISABLE: Turn off or uninstall a target component
    :cvar ENABLE: Turn on or install a target component
    :cvar PATCH: Apply a patch, hotfix, update, etc.
    :cvar POLICY: Remediation requires out-of-band adjustments to policies or procedures
    :cvar RESTRICT: Adjust permissions, access rights, filters, or other access restrictions
    :cvar UPDATE: Install, upgrade or update the system
    """
    UNKNOWN = "unknown"
    CONFIGURE = "configure"
    COMBINATION = "combination"
    DISABLE = "disable"
    ENABLE = "enable"
    PATCH = "patch"
    POLICY = "policy"
    RESTRICT = "restrict"
    UPDATE = "update"


@dataclass
class HtmlText:
    """

    The type for a string with optional XHTML elements and an @xml:lang attribute.

    :ivar w3_org_1999_xhtml_element:
    :ivar lang:
    :ivar override: Used to manage inheritance.
    """

    class Meta:
        name = "htmlText"

    w3_org_1999_xhtml_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/1999/xhtml",
            "mixed": True,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    override: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Ident:
    """

    Data type for the <xccdf:ident> element, a globally meaningful identifier for an <xccdf:Rule>. The body of
    <xccdf:ident> element is the name or identifier of a security configuration issue or vulnerability that the
    <xccdf:Rule> addresses. It has an associated URI that denotes the organization or naming scheme that assigned the
    name. By setting an <xccdf:ident> element on an <xccdf:Rule>, the <xccdf:Benchmark> author effectively declares
    that the <xccdf:Rule> instantiates, implements, or remediates the issue for which the name was assigned.

    :ivar value:
    :ivar system: Denotes the organization or naming scheme that assigned the identifier.
    :ivar other_attributes: May also have other attributes from other namespaces in order to provide additional metadata for the given identifier.
    """

    class Meta:
        name = "ident"

    value: Optional[str] = field(
        default=None,
    )
    system: Optional[str] = field(
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
class Identity:
    """

    Type for an <xccdf:identity> element in an <xccdf:TestResult>. It contains information about the system identity
    or user employed during application of the <xccdf:Benchmark>. If used, shall specify the name of the
    authenticated identity.

    :ivar value:
    :ivar authenticated: Whether the identity was authenticated with the target system during the application of the <xccdf:Benchmark>.
    :ivar privileged: Whether the identity was granted administrative or other special privileges beyond those of a normal user.
    """

    class Meta:
        name = "identity"

    value: Optional[str] = field(
        default=None,
    )
    authenticated: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    privileged: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class IdrefList:
    """

    Data type for elements contain list of references to other XCCDF elements.

    :ivar idref: A space-separated list of id values from other XCCDF elements
    """

    class Meta:
        name = "idrefList"

    idref: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "required": True,
            "tokens": True,
        }
    )


@dataclass
class Idref:
    """

    Data type for elements that contain a reference to another XCCDF element.

    :ivar idref: The id value of another XCCDF element
    """

    class Meta:
        name = "idref"

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class InstanceFix:
    """

    Type for an <xccdf:instance> element which may appear in an <xccdf:fix> element. The <xccdf:instance> element
    inside an <xccdf:fix> element designates a spot where the name of the instance should be substituted into the fix
    template to generate the final fix data.

    :ivar context: Describes the scope or significance of the instance content. The context attribute is intended to be informative and does not affect basic processing.
    """

    class Meta:
        name = "instanceFix"

    context: str = field(
        default="undefined",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class InstanceResult:
    """

    Type for an <xccdf:instance> element in an <xccdf:rule-result>. The content is a string, but the element may also
    have two attributes: @context and @parentContext. Both attributes are intended to provide hints as to the nature
    of the substituted content. This body of this type records the details of the target system instance for multiply
    instantiated <xccdf:Rule> elements.

    :ivar value:
    :ivar context: Describes the scope or significance of the instance content.
    :ivar parent_context: Used to express nested structure in instance context structures.
    """

    class Meta:
        name = "instanceResult"

    value: Optional[str] = field(
        default=None,
    )
    context: str = field(
        default="undefined",
        metadata={
            "type": "Attribute",
        }
    )
    parent_context: Optional[str] = field(
        default=None,
        metadata={
            "name": "parentContext",
            "type": "Attribute",
        }
    )


class InterfaceHint(Enum):
    """

    Allowed interface hint values. <xccdf:Value> elements may contain a hint or recommendation to a benchmark
    consumer or producer about how the user might select or adjust the <xccdf:Value>. This type enumerates the
    possible values of this hint.

    :cvar CHOICE: Multiple choice
    :cvar TEXTLINE: Multiple lines of text
    :cvar TEXT: Single line of text
    :cvar DATE: Date
    :cvar DATETIME: Date and time
    """
    CHOICE = "choice"
    TEXTLINE = "textline"
    TEXT = "text"
    DATE = "date"
    DATETIME = "datetime"


@dataclass
class Metadata:
    """

    Data type that supports inclusion of metadata about a document or element. This is particularly useful for
    facilitating the discovery and retrieval of XCCDF checklists from public repositories. When used, the contents of
    the <xccdf:metadata> element are expressed in XML. The <xccdf:Benchmark> element's metadata should contain
    information formatted using the Dublin Core Metadata Initiative (DCMI) Simple DC Element specification,
    as described in [DCES] and [DCXML]. Benchmark consumers should be prepared to process Dublin Core metadata in the
    <xccdf:metadata> element. Other metadata schemes, including ad-hoc elements, are also allowed, both in the
    <xccdf:Benchmark> and in other elements.
    """

    class Meta:
        name = "metadata"

    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "min_occurs": 1,
        }
    )


class MessageSeverity(Enum):
    """

    Allowed values to indicate the severity of messages from the checking engine. These values don't affect scoring
    themselves but are present merely to convey diagnostic information from the checking engine. Benchmark consumers
    may choose to log these messages or display them to the user.

    :cvar ERROR: Denotes a serious problem identified; test did not run.
    :cvar WARNING: Denotes a possible issue; test may not have run.
    :cvar INFO: Denotes important information about the tests.
    """
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclass
class Notice:
    """

    Data type for an <xccdf:notice> element. <xccdf:notice> elements are used to include legal notices (licensing
    information, terms of use, etc.), copyright statements, warnings, and other advisory notices about this
    <xccdf:Benchmark> and its use. This information may be expressed using XHTML or may be a simply text expression.
    Each <xccdf:notice> element must have a unique identifier.

    :ivar w3_org_1999_xhtml_element:
    :ivar id: The unique identifier for this <xccdf:notice>.
    :ivar base:
    :ivar lang:
    """

    class Meta:
        name = "notice"

    w3_org_1999_xhtml_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/1999/xhtml",
            "mixed": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Param:
    """

    Type for a parameter used in the <xccdf:model> element, which records scoring model information. The contents of
    this type represent a name-value pair, where the name is recorded in the @name attribute and the value appears in
    the element body. <xccdf:param> elements with equal values for the @name attribute may not appear as children of
    the same <xccdf:model> element.

    :ivar value:
    :ivar name: The name associated with the contained value.
    """

    class Meta:
        name = "param"

    value: Optional[str] = field(
        default=None,
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PlainText:
    """

    The data type for an <xccdf:plain-text> element, which is a reusable text block for reference by the <xccdf:sub>
    element. This allows text to be defined once and then reused multiple times. Each <xccdf:plain-text> element mush
    have a unique id.

    :ivar value:
    :ivar id: The unique identifier for this <xccdf:plain-text> element.
    """

    class Meta:
        name = "plainText"

    value: Optional[str] = field(
        default=None,
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ProfileSetValue:
    """

    Type for the <xccdf:set-value> element in an <xccdf:Profile>. This element upports the direct specification of
    simple value types such as numbers, strings, and boolean values. This overrides the <xccdf:value> and
    <xccdf:complex-value> element(s) of an <xccdf:Value> element.

    :ivar value:
    :ivar idref: The @id value of an <xccdf:Value> or the @cluster-id value of one or more <xccdf:Value> elements
    """

    class Meta:
        name = "profileSetValue"

    value: Optional[str] = field(
        default=None,
    )
    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class Rating(Enum):
    """

    This type enumerates allowed rating values the disruption and complexity properties of an <xccdf:Rule> element's
    <xccdf:fix> or <xccdf:fixtext> elements.

    :cvar UNKNOWN: Rating unknown or impossible to estimate (default)
    :cvar LOW: Little or no potential for disruption, very modest complexity
    :cvar MEDIUM: Some chance of minor disruption, substantial complexity
    :cvar HIGH: Likely to cause serious disruption, very complex
    """
    UNKNOWN = "unknown"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class Reference:
    """

    This element provides supplementary descriptive text for a XCCDF elements. When used, it has either a simple
    string value or a value consisting of simple Dublin Core elements. If a bare string appears, then it is taken to
    be the string content for a Dublin Core title element. Multiple <xccdf:reference> elements may appear; a document
    generation processing tool may concatenate them, or put them into a reference list, and may choose to number them.

    :ivar purl_org_dc_elements_1_1_element:
    :ivar href: A URL pointing to the referenced resource.
    :ivar override: Used to manage inheritance processing.
    """

    class Meta:
        name = "reference"

    purl_org_dc_elements_1_1_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "mixed": True,
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    override: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class Result(Enum):
    """

    Allowed result indicators for a test.

    :cvar PASS: The target system or system component satisfied all the conditions of the <xccdf:Rule>.
    :cvar FAIL: The target system or system component did not satisfy all the conditions of the <xccdf:Rule>.
    :cvar ERROR: The checking engine could not complete the evaluation; therefore the status of the target’s compliance with the <xccdf:Rule> is not certain. This could happen, for example, if a testing tool was run with insufficient privileges and could not gather all of the necessary information.
    :cvar UNKNOWN: The testing tool encountered some problem and the result is unknown. For example, a result of ‘unknown’ might be given if the testing tool was unable to interpret the output of the checking engine (the output has no meaning to the testing tool).
    :cvar NOT_APPLICABLE: The <xccdf:Rule> was not applicable to the target of the test. For example, the <xccdf:Rule> might have been specific to a different version of the target OS, or it might have been a test against a platform feature that was not installed.
    :cvar NOT_CHECKED: The <xccdf:Rule> was not evaluated by the checking engine. This status is designed for <xccdf:Rule> elements that have no check. It may also correspond to a status returned by a checking engine if the checking engine does not support the indicated check code.
    :cvar NOT_SELECTED: The <xccdf:Rule> was not selected in the <xccdf:Benchmark>.
    :cvar INFORMATIONAL: The <xccdf:Rule> was checked, but the output from the checking engine is simply information for auditors or administrators; it is not a compliance category. This status value is designed for <xccdf:Rule> elements whose main purpose is to extract information from the target rather than test the target.
    :cvar FIXED: The <xccdf:Rule> had failed, but was then fixed (possibly by a tool that can automatically apply remediation, or possibly by the human auditor).
    """
    PASS = "pass"
    FAIL = "fail"
    ERROR = "error"
    UNKNOWN = "unknown"
    NOT_APPLICABLE = "notapplicable"
    NOT_CHECKED = "notchecked"
    NOT_SELECTED = "notselected"
    INFORMATIONAL = "informational"
    FIXED = "fixed"


class Role(Enum):
    """

    Allowed checking and scoring roles for an <xccdf:Rule>.

    :cvar FULL: If the <xccdf:Rule> is selected, then check it and let the result contribute to the score and appear in reports (default).
    :cvar UNSCORED: If the <xccdf:Rule> is selected, then check it and include it in the test report, but give the result a status of informational and do not use the result in score computations.
    :cvar UNCHECKED: Do not check the <xccdf:Rule>; just force the result status to notchecked.
    """
    FULL = "full"
    UNSCORED = "unscored"
    UNCHECKED = "unchecked"


@dataclass
class Score:
    """

    Type for a score value in an <xccdf:TestResult>.

    :ivar value:
    :ivar system: A URI indicating the scoring model used to create this score.
    :ivar maximum: The maximum possible score value that could have been achieved under the named scoring system.
    """

    class Meta:
        name = "score"

    value: Optional[Decimal] = field(
        default=None,
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    maximum: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SelNum:
    """

    This type is for an element that has numeric content and a @selector attribute for use during tailoring.

    :ivar value:
    :ivar selector: This may be referenced from <xccdf:Profile> selection elements or used during manual tailoring to refine the application of this property. If no selectors are specified for a given property by <xccdf:Profile> elements or manual tailoring, properties with empty or non-existent @selector attributes are activated. If a selector is applied that does not match the @selector attribute of any of a given type of property, then no property of that type considered activated.
    """

    class Meta:
        name = "selNum"

    value: Optional[Decimal] = field(
        default=None,
    )
    selector: str = field(
        default="",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SelString:
    """

    This type is for an element that has string content and a @selector attribute for use in tailoring.

    :ivar value:
    :ivar selector: This may be referenced from <xccdf:Profile> selection elements or used during manual tailoring to refine the application of this property. If no selectors are specified for a given property by <xccdf:Profile> elements or manual tailoring, properties with empty or non-existent @selector attributes are activated. If a selector is applied that does not match the @selector attribute of any of a given type of property, then no property of that type is considered activated. The only exception is the <xccdf:value> and <xccdf:complex-value> properties of an <xccdf:Value> element - if there is no <xccdf:value> or <xccdf:complex-value> property with a matching @selector value then the <xccdf:value>/<xccdf:complex-value> property with an empty or absent @selector attribute becomes active. If there is no such <xccdf:value> or <xccdf:complex-value>, then the first <xccdf:value> or <xccdf:complex-value> listed in the XML becomes active. This reflects the fact that all <xccdf:Value> elements require an active value property at all times.
    """

    class Meta:
        name = "selString"

    value: Optional[str] = field(
        default=None,
    )
    selector: str = field(
        default="",
        metadata={
            "type": "Attribute",
        }
    )


class Severity(Enum):
    """

    Allowed severity values for the @severity attribute of an <xccdf:Rule>. The value of this attribute provides an
    indication of the importance of the <xccdf:Rule> element's recommendation. This information is informative only
    and does not affect scoring.

    :cvar UNKNOWN: Severity not defined (default).
    :cvar INFO: <xccdf:Rule> is informational and failure does not represent a problem.
    :cvar LOW: Not a serious problem.
    :cvar MEDIUM: Fairly serious problem.
    :cvar HIGH: A grave or critical problem.
    """
    UNKNOWN = "unknown"
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class Signature:
    """

    The type of an <XMLDSig:signature> element, which holds an enveloped digital signature asserting authorship and
    allowing verification of the integrity of associated data (e.g., its parent element, other documents, portions of
    other documents).
    """

    class Meta:
        name = "signature"

    w3_org_2000_09_xmldsig_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


class StatusValue(Enum):
    """

    The statusValue represents the possible levels of maturity or consensus level for its parent element as recorded
    by an <xccdf:status> element.

    :cvar ACCEPTED: Released as final
    :cvar DEPRECATED: No longer needed
    :cvar DRAFT: Released in draft state
    :cvar INCOMPLETE: Under initial development
    :cvar INTERIM: Revised and in the process of being finalized
    """
    ACCEPTED = "accepted"
    DEPRECATED = "deprecated"
    DRAFT = "draft"
    INCOMPLETE = "incomplete"
    INTERIM = "interim"


class SubUse(Enum):
    """

    This holds the possible values of the @use attribute within an <xccdf:sub> element. The @use attribute is only
    applicable with the subType's @idref attribute holds the value of the @id of an <xccdf:Value> element.

    :cvar VALUE: Replace with the selected <xccdf:value> or <xccdf:complex-value> of an <xccdf:Value>.
    :cvar TITLE: Replace with the <xccdf:title> of the <xccdf:Value>.
    :cvar LEGACY: Use the context-dependent processing of <xccdf:sub> elements outlined in XCCDF 1.1.4.
    """
    VALUE = "value"
    TITLE = "title"
    LEGACY = "legacy"


@dataclass
class TailoringReference:
    """

    Type for the <xccdf:tailoring> element within an <xccdf:TestResult>. This element is used to indicate the
    identity and location of an <xccdf:Tailoring> file that was used to create the assessment results.

    :ivar href: The URI of the <xccdf:Tailoring> file's location.
    :ivar id: The <xccdf:Tailoring> element's @id value.
    :ivar version: The value of the <xccdf:Tailoring> element's <xccdf:version> property.
    :ivar time: The value of the @time attribute in the <xccdf:Tailoring> element's <xccdf:version> property.
    """

    class Meta:
        name = "tailoringReference"

    href: Optional[str] = field(
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
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TailoringVersion:
    """

    Type for version information about an <xccdf:Tailoring> element.

    :ivar value:
    :ivar time: The time when this version of the <xccdf:Tailoring> document was completed.
    """

    class Meta:
        name = "tailoringVersion"

    value: Optional[str] = field(
        default=None,
    )
    time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TargetIdRef:
    """

    Type for an <xccdf:target-id-ref> element in an <xccdf:TestResult> element. This element contains references to
    external structures with identifying information about the target of an assessment.

    :ivar system: Indicates the language in which this identifying information is expressed. If the identifying language uses XML namespaces, then the @system attribute for the language should be its namespace.
    :ivar href: Points to the external resource (e.g., a file) that contains the identifying information.
    :ivar name: Identifies a specific structure within the referenced file. If the @name attribute is absent, the reference is to the entire resource indicated in the @href attribute.
    """

    class Meta:
        name = "targetIdRef"

    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Text:
    """

    Type for a simple text string with an @override attribute for controlling inheritance.

    :ivar value:
    :ivar lang:
    :ivar override: Used to manage inheritance.
    """

    class Meta:
        name = "text"

    value: Optional[str] = field(
        default=None,
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    override: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class UriRef:
    """

    Data type for elements that have no content and a single @uri attribute.

    :ivar uri: A URI.
    """

    class Meta:
        name = "uriRef"

    uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class ValueOperator(Enum):
    """

    This type enumerates allowed values of the @operator property of <xccdf:Value> elements. The specific
    interpretation of these operators depends on the checking system used.
    """
    EQUALS = "equals"
    NOT_EQUAL = "not equal"
    GREATER_THAN = "greater than"
    LESS_THAN = "less than"
    GREATER_THAN_OR_EQUAL = "greater than or equal"
    LESS_THAN_OR_EQUAL = "less than or equal"
    PATTERN_MATCH = "pattern match"


class ValueType(Enum):
    """

    Allowed data types for <xccdf:Value> elements, string, numeric, and boolean. A tool may choose any convenient
    form to store an <xccdf:Value> element’s <xccdf:value> element, but the @type conveys how the value should be
    treated for user input validation purposes during tailoring processing. The @type may also be used to give
    additional guidance to the user or to validate the user’s input. For example, if an <xccdf:value> element’s @type
    attribute is “number”, then a tool might choose to reject user tailoring input that is not composed of digits. In
    the case of a list of values, the @type applies to all elements of the list individually. Note that checking
    systems may have their own understanding of data types that may not be identical to the typing indicated in XCCDF

    :cvar NUMBER: A numeric value. This may be decimal or integer.
    :cvar STRING: Any character data
    :cvar BOOLEAN: True/false
    """
    NUMBER = "number"
    STRING = "string"
    BOOLEAN = "boolean"


@dataclass
class Version:
    """

    Type for most <xccdf:version> elements.

    :ivar value:
    :ivar time: The time that this version of the associated element was completed.
    :ivar update: A URI indicating a location where updates to the associated element may be obtained.
    """

    class Meta:
        name = "version"

    value: Optional[str] = field(
        default=None,
    )
    time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    update: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class WarningCategory(Enum):
    """

    Allowed warning category keywords for the <xccdf:warning> element used in <xccdf:Rule> elements.

    :cvar GENERAL: Broad or general-purpose warning (default)
    :cvar FUNCTIONALITY: Warning about possible impacts to functionality or operational features
    :cvar PERFORMANCE: Warning about changes to target system performance or throughput
    :cvar HARDWARE: Warning about hardware restrictions or possible impacts to hardware
    :cvar LEGAL: Warning about legal implications
    :cvar REGULATORY: Warning about regulatory obligations or compliance implications
    :cvar MANAGEMENT: Warning about impacts to the management or administration of the target system
    :cvar AUDIT: Warning about impacts to audit or logging
    :cvar DEPENDENCY: Warning about dependencies between this element and other parts of the target system, or version dependencies
    """
    GENERAL = "general"
    FUNCTIONALITY = "functionality"
    PERFORMANCE = "performance"
    HARDWARE = "hardware"
    LEGAL = "legal"
    REGULATORY = "regulatory"
    MANAGEMENT = "management"
    AUDIT = "audit"
    DEPENDENCY = "dependency"


@dataclass
class Check:
    """

    Data type for the <xccdf:check> element. The <xccdf:check> element identifies instructions for tests to determine
    compliance with the <xccdf:Rule> as well as parameters controlling the reporting of those test results. The
    <xccdf:check> element must have at least one child element.

    :ivar check_import: Identifies a value to be retrieved from the checking system during testing of a target system. This element's body must be empty within an <xccdf:check>. After the associated check results have been collected, the result structure returned by the checking engine is processed to collect the named information. This information is then recorded in the check-import element in the corresponding <xccdf:rule-result>.
    :ivar check_export: A mapping from an <xccdf:Value> element to a checking system variable (i.e., external name or id for use by the checking system). This supports export of tailoring values from the XCCDF processing environment to the checking system.
    :ivar check_content_ref: Points to code for a detached check in another location that uses the language or system specified by the <xccdf:check> element’s @system attribute. If multiple <xccdf:check-content-ref> elements appear, they represent alternative locations from which a benchmark consumer may obtain the check content. Benchmark consumers should process the alternatives in the order in which they appear in the XML. The first <xccdf:check-content-ref> from which content can be successfully retrieved should be used.
    :ivar check_content: Holds the actual code of a check, in the language or system specified by the <xccdf:check> element’s @system attribute. If both <xccdf:check-content-ref> and <xccdf:check-content> elements appear in a single <xccdf:check> element, benchmark consumers should use the <xccdf:check-content> element only if none of the references can be resolved to provide content.
    :ivar system: The URI for a checking system. If the checking system uses XML namespaces, then the system attribute for the system should be its namespace.
    :ivar negate: If set to true, the final result of the <xccdf:check> is negated according to the truth table given below.
    :ivar id: Unique identifier for this element. Optional, but must be globally unique if present.
    :ivar selector: This may be referenced from <xccdf:Profile> selection elements or used during manual tailoring to refine the application of the <xccdf:Rule>. If no selector values are specified for a given <xccdf:Rule> by <xccdf:Profile> elements or manual tailoring, all <xccdf:check> elements with non-empty @selector attributes are ignored. If an <xccdf:Rule> has multiple <xccdf:check> elements with the same @selector attribute, each must employ a different checking system, as identified by the @system attribute of the <xccdf:check> element.
    :ivar multi_check: Applicable in cases where multiple checks are executed to determine compliance with a single <xccdf:Rule>. This situation can arise when an <xccdf:check> includes an <xccdf:check-content-ref> element that does not include a @name attribute. The default behavior of a nameless <xccdf:check-content-ref> is to execute all checks in the referenced check content location and AND their results together into a single <xccdf:rule-result> using the AND truth table below. This corresponds to a @multi-check attribute value of “false”. If, however, the @multi-check attribute is set to "true" and a nameless <xccdf:check-content-ref> is used, the <xccdf:Rule> produces a separate <xccdf:rule-result> for each check.
    :ivar base:
    """

    class Meta:
        name = "check"

    check_import: List[CheckImport] = field(
        default_factory=list,
        metadata={
            "name": "check-import",
            "type": "Element",
        }
    )
    check_export: List[CheckExport] = field(
        default_factory=list,
        metadata={
            "name": "check-export",
            "type": "Element",
        }
    )
    check_content_ref: List[CheckContentRef] = field(
        default_factory=list,
        metadata={
            "name": "check-content-ref",
            "type": "Element",
        }
    )
    check_content: Optional[CheckContent] = field(
        default=None,
        metadata={
            "name": "check-content",
            "type": "Element",
        }
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    negate: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    selector: str = field(
        default="",
        metadata={
            "type": "Attribute",
        }
    )
    multi_check: bool = field(
        default=False,
        metadata={
            "name": "multi-check",
            "type": "Attribute",
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
class Fact:
    """

    Data type for an <xccdf:fact> element, which holds information about a target system: a name-value pair with a
    type. The content of the element is the value, and the @name attribute indicates the name. The @name is in the
    form of a URI that indicates the nature of the fact. A table of defined fact URIs appears in section 6.6.3 of the
    XCCDF specification. Additional URIs may be defined by authors to indicate additional kinds of facts.

    :ivar value:
    :ivar name: A URI that indicates the name of the fact.
    :ivar type: The data type of the fact value.
    """

    class Meta:
        name = "fact"

    value: Optional[str] = field(
        default=None,
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type: ValueType = field(
        default=ValueType.BOOLEAN,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Message:
    """

    Type for a message generated by the checking engine or XCCDF tool during <xccdf:Benchmark> testing. The message
    is contained in string format in the body of the element.

    :ivar value:
    :ivar severity: Denotes the seriousness of the message.
    """

    class Meta:
        name = "message"

    value: Optional[str] = field(
        default=None,
    )
    severity: Optional[MessageSeverity] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Model:
    """

    A suggested scoring model for an <xccdf:Benchmark>, also encapsulating any parameters needed by the model. Every
    model is designated with a URI, which appears here as the system attribute. See the XCCDF specification for a
    list of standard scoring models and their associated URIs. Vendors may define their own scoring models and
    provide additional URIs to designate them. Some models may need additional parameters; to support such a model,
    zero or more <xccdf:param> elements may appear as children of the <xccdf:model> element.

    :ivar param: Parameters provided as input to the designated scoring model.
    :ivar system: A URI designating a scoring model.
    """

    class Meta:
        name = "model"
        namespace = XCCDF_1_2_NAMESPACE

    param: List[Param] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Override:
    """

    Type for an <xccdf:override> element in an <xccdf:rule-result>. This element is used to record manual
    modification or annotation of a particular <xccdf:rule-result>. All attributes and child elements are required.
    It will not always be the case that the <xccdf:new-result> value will differ from the <xccdf:old-result> value.
    They might match if an authority wished to make a remark on the result without changing it. If <xccdf:new-result>
    and <xccdf:old-result> differ, the <xccdf:result> element of the enclosing <xccdf:rule-result> must match the
    <xccdf:new-result> value.

    :ivar old_result: The <xccdf:rule-result> status before this override.
    :ivar new_result: The new, override <xccdf:rule-result> status.
    :ivar remark: Rationale or explanation text for why or how the override was applied.
    :ivar time: When the override was applied.
    :ivar authority: Name or other identification for the human principal authorizing the override.
    """

    class Meta:
        name = "override"

    old_result: Optional[Result] = field(
        default=None,
        metadata={
            "name": "old-result",
            "type": "Element",
            "required": True,
        }
    )
    new_result: Optional[Result] = field(
        default=None,
        metadata={
            "name": "new-result",
            "type": "Element",
            "required": True,
        }
    )
    remark: Optional[Text] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    authority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class OverrideableCpe2Idref(Cpe2Idref):
    """

    Data type for <xccdf:platform> elements that need @override attributes. (I.e., <xccdf:platform> elements that are
    in structures that can be extended, such as Items and <xccdf:Profile> elements.) This is used to identify the
    applicable target platform for its respective parent elements.

    :ivar override: Used to manage inheritance.
    """

    class Meta:
        name = "overrideableCPE2idref"

    override: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ProfileRefineRule:
    """

    Type for the <xccdf:refine-rule> element in an <xccdf:Profile>. A <xccdf:refine-rule> element allows the author
    to select <xccdf:check> statements and override the @weight, @severity, and @role of an <xccdf:Rule>,
    <xccdf:Group>, or cluster of <xccdf:Rule> and <xccdf:Group> elements. Despite the name, this selector does apply
    for <xccdf:Group> elements and for clusters that include <xccdf:Group> elements, but it only affects their
    @weight attribute.

    :ivar remark: Explanatory material or other prose.
    :ivar idref: The @id value of an <xccdf:Rule> or <xccdf:Group>, or the @cluster-id value of one or more <xccdf:Rule> or <xccdf:Group> elements.
    :ivar weight: The new value for the identified element's @weight property.
    :ivar selector: Holds a selector value corresponding to the value of a @selector property in an <xccdf:Rule> element's <xccdf:check> element. If the selector specified does not match any of the @selector attributes specified on any of the <xccdf:check> children of an <xccdf:Rule>, then the <xccdf:check> child element without a @selector attribute is used. If there is no child without a @selector attribute, then that Rule would have no effective <xccdf:check> element.
    :ivar severity: The new value for the identified <xccdf:Rule> element's @severity property.
    :ivar role: The new value for the identified <xccdf:Rule> element's @role property.
    """

    class Meta:
        name = "profileRefineRule"

    remark: List[Text] = field(
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
    weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "total_digits": 3,
        }
    )
    selector: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    severity: Optional[Severity] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    role: Optional[Role] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ProfileRefineValue:
    """

    Type for the <xccdf:refine-value> element in an <xccdf:Profile>. This element designates the <xccdf:Value>
    constraints to be applied during tailoring for an <xccdf:Value> element or the <xccdf:Value> members of a cluster.

    :ivar remark: Explanatory material or other prose.
    :ivar idref: The @id value of an <xccdf:Value> or the @cluster-id value of one or more <xccdf:Value> elements
    :ivar selector: Holds a selector value corresponding to the value of a @selector property in an <xccdf:Value> element's child properties. Properties with a matching @selector are considered active and all other properties are inactive. This may mean that, after selector application, some classes of <xccdf:Value> properties will be completely inactive because none of those properties had a matching @selector. The only exception is the <xccdf:value> and <xccdf:complex-value> properties of an <xccdf:Value> element - if there is no <xccdf:value> or <xccdf:complex-value> property with a matching @selector value then the <xccdf:value>/<xccdf:complex-value> property with an empty or absent @selector attribute becomes active. If there is no such <xccdf:value> or <xccdf:complex-value>, then the first <xccdf:value> or <xccdf:complex-value> listed in the XML becomes active. This reflects the fact that all <xccdf:Value> elements require an active value property at all times.
    :ivar operator: The new value for the identified <xccdf:Value> element's @operator property.
    """

    class Meta:
        name = "profileRefineValue"

    remark: List[Text] = field(
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
    selector: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    operator: Optional[ValueOperator] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ProfileSelect:
    """

    Type for the <xccdf:select> element in an <xccdf:Profile>. This element designates an <xccdf:Rule>,
    <xccdf:Group>, or cluster of <xccdf:Rule> and <xccdf:Group> elements and overrides the @selected attribute on the
    designated items, providing a means for including or excluding <xccdf:Rule> elements from an assessment.

    :ivar remark: Explanatory material or other prose.
    :ivar idref: The @id value of an <xccdf:Rule> or <xccdf:Group>, or the @cluster-id value of one or more <xccdf:Rule> or <xccdf:Group> elements.
    :ivar selected: The new value for the indicated item's @selected property.
    """

    class Meta:
        name = "profileSelect"

    remark: List[Text] = field(
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
    selected: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ProfileSetComplexValue(ComplexValue):
    """

    Type for the <xccdf:set-complex-value> element in an <xccdf:Profile>. This element supports the direct
    specification of complex value types such as lists. Zero or more <xccdf:item> elements may appear as children of
    this element; if no child elements are present, this element represents an empty list. This overrides the
    <xccdf:value> and <xccdf:complex-value> element(s) of an <xccdf:Value> element.

    :ivar idref: The @id value of an <xccdf:Value> or the @cluster-id value of one or more <xccdf:Value> elements
    """

    class Meta:
        name = "profileSetComplexValue"

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SelChoices:
    """

    The type of the <xccdf:choice> element, which specifies a list of legal or suggested choices for an <xccdf:Value> object.

    :ivar choice: A single choice holding a simple type. (I.e.,  number, string, or boolean.)
    :ivar complex_choice: A single choice holding a list of simple types.
    :ivar must_match: True if the listed choices are the only permissible settings for the given <xccdf:Value>. False if choices not specified in this <xccdf:choices> element are acceptable settings for this <xccdf:Value>.
    :ivar selector: This may be referenced from <xccdf:Profile>  selection elements or used during manual tailoring to refine the application of the <xccdf:Rule>. If no selectors are specified for a given <xccdf:Value> by <xccdf:Profile> elements or manual tailoring, an <xccdf:choice> element with an empty or non-existent @selector attribute is activated. If a selector is applied that does not match the  @selector attribute of any <xccdf:choices> element, then no <xccdf:choices>  element is considered activated.
    """

    class Meta:
        name = "selChoices"

    choice: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    complex_choice: List[ComplexValue] = field(
        default_factory=list,
        metadata={
            "name": "complex-choice",
            "type": "Element",
        }
    )
    must_match: Optional[bool] = field(
        default=None,
        metadata={
            "name": "mustMatch",
            "type": "Attribute",
        }
    )
    selector: str = field(
        default="",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SelComplexValue(ComplexValue):
    """

    Data type that supports values that are lists of simple types with an associated @selector attribute used in tailoring.

    :ivar selector: This may be referenced from <xccdf:Profile> selection elements or used during manual tailoring to refine the application of this property. If no selectors are specified for a given item by <xccdf:Profile> elements or manual tailoring, properties with empty or non-existent @selector attributes are activated. If a selector is applied that does not match the  @selector attribute of any of a given type of property, then nxccdf:choices> element is considered activated. The only exception is the <xccdf:value> and <xccdf:complex-  value> properties of an <xccdf:Value> element - if there is no <xccdf:value> or <xccdf:complex-value> property with a matching @selector value then the <xccdf:value>/<xccdf:complex-value> property with an empty or absent @selector attribute becomes active. If there is no such <xccdf:value> or <xccdf:complex-value>, then the first <xccdf:value> or <xccdf:complex-value> listed becomes active. This reflects the fact that all <xccdf:Value>  elements require an active value property at all times.
    """

    class Meta:
        name = "selComplexValue"

    selector: str = field(
        default="",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Status:
    """

    The acceptance status of an element with an optional date attribute, which signifies the date of the status
    change. If an element does not have its own <xccdf:status> element, its status is that of its parent element. If
    there is more than one <xccdf:status> for a single element, then every instance of the <xccdf:status> element
    must have a @date attribute, and the <xccdf:status> element with the latest date is considered the current status.

    :ivar value:
    :ivar date: The date the parent element achieved the indicated status.
    """

    class Meta:
        name = "status"
        namespace = XCCDF_1_2_NAMESPACE

    value: Optional[StatusValue] = field(
        default=None,
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Sub(Idref):
    """

    The type used for <xccdf:sub> elements. The <xccdf:sub> element identifies replacement content that should appear
    in place of the <xccdf:sub> element during text substitution. The subType consists of a regular idrefType with an
    additional @use attribute to dictate the behavior of the <xccdf:sub> element under substitution. When the @idref
    is to an <xccdf:Value>, the @use attribute indicates whether the <xccdf:Value> element's title or value should
    replace the <xccdf:sub> element. The @use attribute is ignored when the @idref is to an <xccdf:plain-text>
    element; the body of the <xccdf:plain-text> element is always used to replace the <xccdf:sub> element.

    :ivar use: Dictates the nature of the content inserted under text substitution processing.
    """

    class Meta:
        name = "sub"

    use: SubUse = field(
        default=SubUse.VALUE,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TailoringBenchmarkReference(BenchmarkReference):
    """

    Identifies the <xccdf:Benchmark> to which an <xccdf:Tailoring> element applies.

    :ivar version: Identifies the version of the referenced <xccdf:Benchmark>.
    """

    class Meta:
        name = "tailoringBenchmarkReference"

    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ComplexCheck:
    """

    The type for an element that contains a boolean combination of <xccdf:checks>. This element can have only
    <xccdf:complex-check> and <xccdf:check> elements as children. Child elements may appear in any order but at least
    one child element must be present. It has two attributes, @operator and @negate, which dictate how <xccdf:check>
    or <xccdf:complex-check> child elements are to be combined. Truth tables for these operations appear below.

    :ivar check: Instructions for a single test.
    :ivar complex_check: A child <xccdf:complex-check>, allowing another level of logic in combining component checks.
    :ivar operator: Indicates whether the child <xccdf:check> and/or <xccdf:complex-check> elements of this <xccdf:complex-check> should be combined using an AND or OR operation
    :ivar negate: If true, negate the final result of this <xccdf:complex-check> after the child elements are combined using the identified operator.
    """

    class Meta:
        name = "complexCheck"

    check: List[Check] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    complex_check: List["ComplexCheck"] = field(
        default_factory=list,
        metadata={
            "name": "complex-check",
            "type": "Element",
        }
    )
    operator: Optional[ComplexCheckOperator] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    negate: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Fix:
    """

    Data type for the <xccdf:fix> element. The body of this element contains a command string, script,
    or other system modification statement that, if executed on the target system, can bring it into full,
    or at least better, compliance with this <xccdf:Rule>.

    :ivar content:
    :ivar sub: Specifies an <xccdf:Value> or <xccdf:plain-text> element to be used for text substitution
    :ivar instance: Designates a spot where the name of the instance should be substituted into the fix template to generate the final fix data. If the @context attribute is omitted, the value of the @context defaults to “undefined”.
    :ivar id: A local identifier for the element. It is optional for the @id to be unique; multiple <xccdf:fix> elements may have the same @id but different values for their other attributes. It is used primarily to allow <xccdf:fixtext> elements to be associated with one or more <xccdf:fix> elements
    :ivar reboot: True if a reboot is known to be required and false otherwise.
    :ivar strategy: The method or approach for making the described fix.
    :ivar disruption: An estimate of the potential for disruption or operational degradation that the application of this fix will impose on the target.
    :ivar complexity: The estimated complexity or difficulty of applying the fix to the target.
    :ivar system: A URI that identifies the scheme, language, engine, or process for which the fix contents are written. Table 17 in the XCCDF specification defines several general-purpose URNs that may be used for this, and tool vendors and system providers may define and use target- specific URNs.
    :ivar platform: In case different fix scripts or procedures are required for different target platform types (e.g., different patches for Windows Vista and Windows 7), this attribute allows a CPE name or CPE applicability language expression to be associated with an <xccdf:fix> element. This should appear on an <xccdf:fix> when the content applies to only one platform out of several to which the <xccdf:Rule> could apply.
    """

    class Meta:
        name = "fix"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    sub: List[Sub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    instance: List[InstanceFix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    reboot: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    strategy: FixStrategy = field(
        default=FixStrategy.UNKNOWN,
        metadata={
            "type": "Attribute",
        }
    )
    disruption: Rating = field(
        default=Rating.UNKNOWN,
        metadata={
            "type": "Attribute",
        }
    )
    complexity: Rating = field(
        default=Rating.UNKNOWN,
        metadata={
            "type": "Attribute",
        }
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    platform: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class HtmlTextWithSub:
    """

    The type for a string with optional XHTML elements, and an @xml:lang attribute.

    :ivar sub: Specifies an <xccdf:Value> or <xccdf:plain-text> element to be used for text substitution
    :ivar w3_org_1999_xhtml_element:
    :ivar lang:
    :ivar override: Used to manage inheritance.
    """

    class Meta:
        name = "htmlTextWithSub"

    sub: List[Sub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    w3_org_1999_xhtml_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/1999/xhtml",
            "mixed": True,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    override: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ProfileNote:
    """

    Type for an <xccdf:profile-note> within an <xccdf:Rule>. This element contains text that describes special
    aspects of an <xccdf:Rule> relative to one or more <xccdf:Profile> elements. This allows an author to document
    things within <xccdf:Rule> elements that are specific to a given <xccdf:Profile>. This information might then be
    displayed to a reader based on the selection of a particular <xccdf:Profile>. The body text may include XHTML
    mark-up as well as <xccdf:sub> elements.

    :ivar sub: Specifies an <xccdf:Value> or <xccdf:plain-text> element to be used for text substitution
    :ivar w3_org_1999_xhtml_element:
    :ivar lang:
    :ivar tag: The identifier of this note.
    """

    class Meta:
        name = "profileNote"

    sub: List[Sub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    w3_org_1999_xhtml_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/1999/xhtml",
            "mixed": True,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    tag: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TargetFacts:
    """

    Data type for the <xccdf:target-facts> elements in <xccdf:TestResult> elements. A <xccdf:target-facts> element
    holds a list of named facts about the target system or platform. Each fact is an element of type factType. Each
    <xccdf:fact> must have a name, but duplicate names are allowed. (For example, if you had a fact about MAC
    addresses, and the target system had three NICs, then you'd need three instances of the
    "urn:xccdf:fact:ethernet:MAC" fact.)

    :ivar fact: A named fact about the target system or platform.
    """

    class Meta:
        name = "targetFacts"

    fact: List[Fact] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class TextWithSub:
    """

    Type for a string with embedded <xccdf:Value> substitutions and an @override attribute to help manage inheritance.

    :ivar content:
    :ivar sub: Specifies an <xccdf:Value> or <xccdf:plain-text> element to be used for text substitution.
    :ivar lang:
    :ivar override: Used to manage inheritance.
    """

    class Meta:
        name = "textWithSub"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    sub: List[Sub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    override: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class FixText(HtmlTextWithSub):
    """

    Data type for the <xccdf:fixtext> element, which contains data that describes how to bring a target system into
    compliance with an <xccdf:Rule>. Each <xccdf:fixtext> element may be associated with one or more <xccdf:fix>
    elements through the @fixref attribute. The body holds explanatory text about the fix procedures.

    :ivar content:
    :ivar fixref: A reference to the @id of an <xccdf:fix> element.
    :ivar reboot: True if a reboot is known to be required and false otherwise.
    :ivar strategy: The method or approach for making the described fix.
    :ivar disruption: An estimate of the potential for disruption or operational degradation that the application of this fix will impose on the target.
    :ivar complexity: The estimated complexity or difficulty of applying the fix to the target.
    """

    class Meta:
        name = "fixtext"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    fixref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    reboot: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    strategy: FixStrategy = field(
        default=FixStrategy.UNKNOWN,
        metadata={
            "type": "Attribute",
        }
    )
    disruption: Rating = field(
        default=Rating.UNKNOWN,
        metadata={
            "type": "Attribute",
        }
    )
    complexity: Rating = field(
        default=Rating.UNKNOWN,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class RuleResult:
    """

    Type for the <xccdf:rule-result> element within an <xccdf:TestResult>. An <xccdf:rule-result> holds the result of
    applying an <xccdf:Rule> from the <xccdf:Benchmark> to a target system or component of a target system.

    :ivar result: Result of applying the referenced <xccdf:Rule> to a target or target component. (E.g., Pass, Fail, etc.)
    :ivar override: An XML block explaining how and why an auditor chose to override the result.
    :ivar ident: A long-term globally meaningful identifier for the issue, vulnerability, platform, etc. copied from the referenced <xccdf:Rule>.
    :ivar metadata: XML metadata associated with this <xccdf:rule-result>.
    :ivar message: Diagnostic messages from the checking engine. These elements do not affect scoring; they are present merely to convey diagnostic information from the checking engine.
    :ivar instance: Name of the target subsystem or component to which this result applies, for a multiply instantiated <xccdf:Rule>. The element is important for an <xccdf:Rule> that applies to components of the target system, especially when a target might have several such components, and where the @multiple attribute of the <xccdf:Rule> is set to true.
    :ivar fix: Fix script for this target platform, if available (would normally appear only for result values of “fail”). It is assumed to have been ‘instantiated’ by the testing tool and any substitutions or platform selections already made.
    :ivar check: Encapsulated or referenced results to detailed testing output from the checking engine (if any).
    :ivar complex_check: A copy of the <xccdf:Rule> element’s <xccdf:complex-check> element where each component <xccdf:check> element of the <xccdf:complex-check> element is an encapsulated or referenced results to detailed testing output from the checking engine (if any) as described in the <xccdf:rule-result> <xccdf:check> property.
    :ivar idref: The value of the @id property of an <xccdf:Rule>. This <xccdf:rule-result> reflects the result of applying this <xccdf:Rule> to a target or target component.
    :ivar role: The value of the @role property of the referenced <xccdf:Rule>.
    :ivar severity: The value of the @severity property of the referenced <xccdf:Rule>.
    :ivar time: Time when application of this instance of the referenced <xccdf:Rule> was completed.
    :ivar version: The value of the @version property of the referenced <xccdf:Rule>.
    :ivar weight: The value of the @weight property of the referenced <xccdf:Rule>.
    """

    class Meta:
        name = "ruleResult"

    result: Optional[Result] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    override: List[Override] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ident: List[Ident] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    metadata: List[Metadata] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    message: List[Message] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    instance: List[InstanceResult] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fix: List[Fix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    check: List[Check] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    complex_check: Optional[ComplexCheck] = field(
        default=None,
        metadata={
            "name": "complex-check",
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
    role: Optional[Role] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    severity: Optional[Severity] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": Decimal("0.0"),
            "total_digits": 3,
        }
    )


@dataclass
class WarningType(HtmlTextWithSub):
    """

    Data type for the <xccdf:warning> element under the <xccdf:Rule> element. This element holds a note or caveat
    about the item intended to convey important cautionary information for the <xccdf:Benchmark> user.

    :ivar content:
    :ivar category: A hint as to the nature of the warning.
    """

    class Meta:
        name = "warning"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    category: WarningCategory = field(
        default=WarningCategory.GENERAL,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Profile:
    """

    The <xccdf:Profile> element is a named tailoring for an <xccdf:Benchmark>. While an <xccdf:Benchmark> can be
    tailored in place by setting properties of various elements, <xccdf:Profile> elements allow one <xccdf:Benchmark>
    document to hold several independent tailorings.

    :ivar status: Status of the <xccdf:Profile> and date at which it attained that status. Authors may use this element to record the maturity or consensus level of an <xccdf:Profile>. If the <xccdf:status> is not given explicitly, then the <xccdf:Profile> is taken to have the same status as its parent <xccdf:Benchmark>.
    :ivar dc_status: Holds additional status information using the Dublin Core format.
    :ivar version: Version information about this <xccdf:Profile>.
    :ivar title: Title of the <xccdf:Profile>.
    :ivar description: Text that describes the <xccdf:Profile>.
    :ivar reference: A reference where the user can learn more about the subject of this <xccdf:Profile>.
    :ivar platform: A target platform for this <xccdf:Profile>.
    :ivar select: Select or deselect <xccdf:Group> and <xccdf:Rule> elements.
    :ivar set_complex_value: Set the value of an <xccdf:Value> to a list.
    :ivar set_value: Set the value of an <xccdf:Value> to a simple data value.
    :ivar refine_value: Customize the properties of an <xccdf:Value>.
    :ivar refine_rule: Customize the properties of an <xccdf:Rule> or <xccdf:Group>.
    :ivar metadata: Metadata associated with this <xccdf:Profile>.
    :ivar signature: A digital signature asserting authorship and allowing verification of the integrity of the <xccdf:Profile>.
    :ivar id: Unique identifier for this <xccdf:Profile>.
    :ivar prohibit_changes: Whether or not products should prohibit changes to this <xccdf:Profile>.
    :ivar abstract: If true, then this <xccdf:Profile> exists solely to be extended by other <xccdf:Profile> elements.
    :ivar note_tag: Tag identifier to specify which <xccdf:profile-note> element from an <xccdf:Rule> should be associated with this <xccdf:Profile>.
    :ivar extends: The id of an <xccdf:Profile> on which to base this <xccdf:Profile>.
    :ivar base:
    :ivar id_attribute: An identifier used for referencing elements included in an XML signature.
    """

    class Meta:
        namespace = XCCDF_1_2_NAMESPACE

    status: List[Status] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": XCCDF_1_2_NAMESPACE,
        }
    )
    dc_status: List[DcStatus] = field(
        default_factory=list,
        metadata={
            "name": "dc-status",
            "type": "Element",
        }
    )
    version: Optional[Version] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: List[TextWithSub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    description: List[HtmlTextWithSub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    platform: List[OverrideableCpe2Idref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    select: List[ProfileSelect] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    set_complex_value: List[ProfileSetComplexValue] = field(
        default_factory=list,
        metadata={
            "name": "set-complex-value",
            "type": "Element",
            "sequential": True,
        }
    )
    set_value: List[ProfileSetValue] = field(
        default_factory=list,
        metadata={
            "name": "set-value",
            "type": "Element",
            "sequential": True,
        }
    )
    refine_value: List[ProfileRefineValue] = field(
        default_factory=list,
        metadata={
            "name": "refine-value",
            "type": "Element",
            "sequential": True,
        }
    )
    refine_rule: List[ProfileRefineRule] = field(
        default_factory=list,
        metadata={
            "name": "refine-rule",
            "type": "Element",
            "sequential": True,
        }
    )
    metadata: List[Metadata] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"xccdf_[^_]+_profile_.+",
        }
    )
    prohibit_changes: bool = field(
        default=False,
        metadata={
            "name": "prohibitChanges",
            "type": "Attribute",
        }
    )
    abstract: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    note_tag: Optional[str] = field(
        default=None,
        metadata={
            "name": "note-tag",
            "type": "Attribute",
        }
    )
    extends: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    id_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class Item:
    """

    An item is a named constituent of an <xccdf:Benchmark>. There are three types of items: <xccdf:Group>,
    <xccdf:Rule> and <xccdf:Value>. The <xccdf:Item> element type imposes constraints shared by all <xccdf:Group>,
    <xccdf:Rule> and <xccdf:Value> elements. The itemType is abstract, so the element <xccdf:Item> can never appear
    in a valid XCCDF document.

    :ivar status: Status of the item and date at which it attained that status. <xccdf:Benchmark> authors may use this element to record the maturity or consensus level for elements in the <xccdf:Benchmark>. If an item does not have an explicit <xccdf:status> given, then its status is that of its parent.
    :ivar dc_status: Holds additional status information using the Dublin Core format.
    :ivar version: Version information about this item.
    :ivar title: Title of the item. Every item should have an <xccdf:title>, because this helps people understand the purpose of the item.
    :ivar description: Text that describes the item.
    :ivar warning: A note or caveat about the item intended to convey important cautionary information for the <xccdf:Benchmark> user (e.g., “Complying with this rule will cause the system to reject all IP packets”). If multiple <xccdf:warning> elements appear, benchmark consumers should concatenate them for generating reports or documents. Benchmark consumers may present this information in a special manner in generated documents.
    :ivar question: Interrogative text to present to the user during tailoring. It may also be included into a generated document. For <xccdf:Rule> and <xccdf:Group> elements, the <xccdf:question> text should be a simple binary (yes/no) question because it is supporting the selection aspect of tailoring. For <xccdf:Value> elements, the <xccdf:question> should solicit the user to provide a specific value. Tools may also display constraints on values and any defaults as specified by the other <xccdf:Value> properties.
    :ivar reference: References where the user can learn more about the subject of this item.
    :ivar metadata: XML metadata associated with this item, such as sources, special information, or other details.
    :ivar abstract: If true, then this item is abstract and exists only to be extended. The use of this attribute for <xccdf:Group> elements is deprecated and should be avoided.
    :ivar cluster_id: An identifier to be used as a means to identify (refer to) related items. It designates membership in a cluster of items, which are used for controlling items via <xccdf:Profile> elements. All the items with the same cluster identifier belong to the same cluster. A selector in an <xccdf:Profile> may refer to a cluster, thus making it easier for authors to create and maintain <xccdf:Profile> elements in a complex <xccdf:Benchmark>.
    :ivar extends: The identifier of an item on which to base this item. If present, it must have a value equal to the @id attribute of another item. The use of this attribute for <xccdf:Group> elements is deprecated and should be avoided.
    :ivar hidden: If this item should be excluded from any generated documents although it may still be used during assessments.
    :ivar prohibit_changes: If benchmark producers should prohibit changes to this item during tailoring. An author should use this when they do not want to allow end users to change the item.
    :ivar lang:
    :ivar base:
    :ivar id: An identifier used for referencing elements included in an XML signature
    """

    class Meta:
        namespace = XCCDF_1_2_NAMESPACE

    status: List[Status] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": XCCDF_1_2_NAMESPACE,
        }
    )
    dc_status: List[DcStatus] = field(
        default_factory=list,
        metadata={
            "name": "dc-status",
            "type": "Element",
        }
    )
    version: Optional[Version] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    title: List[TextWithSub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    description: List[HtmlTextWithSub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    warning: List[WarningType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    question: List[Text] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    metadata: List[Metadata] = field(
        default_factory=list,
        metadata={
            "type": "Element",
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
class TestResult:
    """

    The <xccdf:TestResult> element encapsulates the results of a single application of an <xccdf:Benchmark> to a
    single target platform. The <xccdf:TestResult> element normally appears as the child of the <xccdf:Benchmark>
    element, although it may also appear as the top-level element of an XCCDF results document. XCCDF is not intended
    to be a database format for detailed results; the <xccdf:TestResult> element offers a way to store the results of
    individual tests in modest detail, with the ability to reference lower-level testing data.

    :ivar benchmark: Reference to the <xccdf:Benchmark> for which the <xccdf:TestResult> records results. This property is required if this <xccdf:TestResult> element is the top-level element and optional otherwise.
    :ivar tailoring_file: The tailoring file element contains attributes used to identify an <xccdf:Tailoring> element used to guide the assessment reported on in this <xccdf:TestResult>. The tailoring element is required in an <xccdf:TestResult> if and only if an <xccdf:Tailoring> element guided the assessment recorded in the <xccdf:TestResult> or if the <xccdf:Tailoring> element records manual tailoring actions applied to this assessment.
    :ivar title: Title of the test.
    :ivar remark: A remark about the test, possibly supplied by the person administering the <xccdf:Benchmark> assessment
    :ivar organization: The name of the organization or other entity responsible for applying this <xccdf:Benchmark> and generating this result. When multiple <xccdf:organization> elements are used to indicate multiple organization names in a hierarchical organization, the highest-level organization should appear first.
    :ivar identity: Information about the system identity or user employed during application of the <xccdf:Benchmark>. If used, specifies the name of the authenticated identity.
    :ivar profile: The <xccdf:profile> element holds the value of the @id attribute value of the <xccdf:Profile> selected to be used in the assessment reported on by this <xccdf:TestResult>. This <xccdf:Profile> might be from the <xccdf:Benchmark> or from an <xccdf:Tailoring> file, if used. This element should appear if and only if an <xccdf:Profile> was selected to guide the assessment.
    :ivar target: Name or description of the target system whose test results are recorded in the <xccdf:TestResult> element (the system to which an <xccdf:Benchmark> test was applied). Each appearance of the element supplies a name by which the target host or device was identified at the time the test was run. The name may be any string, but applications should include the fully qualified DNS name whenever possible.
    :ivar target_address: Network address of the target system to which an <xccdf:Benchmark> test was applied. Typical forms for the address include IP version 4 (IPv4), IP version 6 (IPv6), and Ethernet media access control (MAC).
    :ivar target_facts: A list of named facts about the target system or platform.
    :ivar target_id_ref: References to external structures with identifying information about the target of this assessment.
    :ivar other_element: Identifying information expressed in other XML formats can be included here.
    :ivar platform: A platform on the target system. There should be one instance of this property for every platform that the target system was found to meet.
    :ivar set_value: Specific setting for a single <xccdf:Value> element used during the test.
    :ivar set_complex_value: Specific setting for a single <xccdf:Value> element used during the test when the given value is set to a complex type, such as a list.
    :ivar rule_result: The result of a single instance of an <xccdf:Rule> application against the target. The <xccdf:TestResult> must include at least one <xccdf:rule-result> record for each <xccdf:Rule> that was selected in the resolved <xccdf:Benchmark>.
    :ivar score: An overall score for this <xccdf:Benchmark> test.
    :ivar metadata: XML metadata associated with this <xccdf:TestResult>.
    :ivar signature: A digital signature asserting authorship and allowing verification of the integrity of the <xccdf:TestResult>.
    :ivar id: Unique identifier for this element.
    :ivar start_time: Time when testing began.
    :ivar end_time: Time when testing was completed and the results recorded.
    :ivar test_system: Name of the benchmark consumer program that generated this <xccdf:TestResult> element; should be either a CPE name or a CPE applicability language expression.
    :ivar version: The version number string copied from the <xccdf:Benchmark> used to direct this assessment.
    :ivar id_attribute: An identifier used for referencing elements included in an XML signature.
    """

    class Meta:
        namespace = XCCDF_1_2_NAMESPACE

    benchmark: Optional[BenchmarkReference] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tailoring_file: Optional[TailoringReference] = field(
        default=None,
        metadata={
            "name": "tailoring-file",
            "type": "Element",
        }
    )
    title: List[Text] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    remark: List[Text] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    organization: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    identity: Optional[Identity] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    profile: Optional[Idref] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    target: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    target_address: List[str] = field(
        default_factory=list,
        metadata={
            "name": "target-address",
            "type": "Element",
        }
    )
    target_facts: Optional[TargetFacts] = field(
        default=None,
        metadata={
            "name": "target-facts",
            "type": "Element",
        }
    )
    target_id_ref: List[TargetIdRef] = field(
        default_factory=list,
        metadata={
            "name": "target-id-ref",
            "type": "Element",
            "sequential": True,
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "sequential": True,
        }
    )
    platform: List[Cpe2Idref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    set_value: List[ProfileSetValue] = field(
        default_factory=list,
        metadata={
            "name": "set-value",
            "type": "Element",
            "sequential": True,
        }
    )
    set_complex_value: List[ProfileSetComplexValue] = field(
        default_factory=list,
        metadata={
            "name": "set-complex-value",
            "type": "Element",
            "sequential": True,
        }
    )
    rule_result: List[RuleResult] = field(
        default_factory=list,
        metadata={
            "name": "rule-result",
            "type": "Element",
        }
    )
    score: List[Score] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    metadata: List[Metadata] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"xccdf_[^_]+_testresult_.+",
        }
    )
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "start-time",
            "type": "Attribute",
        }
    )
    end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "end-time",
            "type": "Attribute",
            "required": True,
        }
    )
    test_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "test-system",
            "type": "Attribute",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class SelectableItem(Item):
    """

    This abstract item type represents the basic data shared by all <xccdf:Group> and <xccdf:Rule> elements.

    :ivar rationale: Descriptive text giving rationale or motivations for abiding by this <xccdf:Group>/<xccdf:Rule> (i.e., why it is important to the security of the target platform).
    :ivar platform: Platforms to which this <xccdf:Group>/<xccdf:Rule> applies.
    :ivar requires: The identifiers of other <xccdf:Group> or <xccdf:Rule> elements that must be selected for this <xccdf:Group>/<xccdf:Rule> to be evaluated and scored properly. Each <xccdf:requires> element specifies a list of one or more required items by their identifiers. If at least one of the specified <xccdf:Group> or <xccdf:Rule> elements is selected, the requirement is met.
    :ivar conflicts: The identifier of another <xccdf:Group> or <xccdf:Rule> that must be unselected for this <xccdf:Group>/<xccdf:Rule> to be evaluated and scored properly. Each <xccdf:conflicts> element specifies a single conflicting item using its idref attribute. If the specified <xccdf:Group> or <xccdf:Rule> element is not selected, the requirement is met.
    :ivar selected: If true, this <xccdf:Group>/<xccdf:Rule> is selected to be processed as part of the <xccdf:Benchmark> when it is applied to a target system. An unselected <xccdf:Group> does not get processed, and its contents are not processed either (i.e., all descendants of an unselected <xccdf:Group> are implicitly unselected). An unselected <xccdf:Rule> is not checked and does not contribute to scoring.
    :ivar weight: The relative scoring weight of this <xccdf:Group>/<xccdf:Rule>, for computing a score, expressed as a non-negative real number. It denotes the importance of an <xccdf:Group>/<xccdf:Rule>. Under some scoring models, scoring is computed independently for each collection of sibling <xccdf:Group> and <xccdf:Rule> elements, then normalized as part of the overall scoring process.
    """

    class Meta:
        name = "selectableItem"

    rationale: List[HtmlTextWithSub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    platform: List[OverrideableCpe2Idref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    requires: List[IdrefList] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    conflicts: List[Idref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
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


@dataclass
class Tailoring:
    """

    The <xccdf:Tailoring> element holds one or more <xccdf:Profile> elements. These <xccdf:Profile> elements record
    additional tailoring activities that apply to a given <xccdf:Benchmark>. <xccdf:Tailoring> elements are separate
    from <xccdf:Benchmark> documents, but each <xccdf:Tailoring> element is associated with a specific
    <xccdf:Benchmark> document. By defining these tailoring actions separately from the <xccdf:Benchmark> document to
    which they apply, these actions can be recorded without affecting the integrity of the source itself.

    :ivar benchmark: Identifies the <xccdf:Benchmark> to which this tailoring applies. A <xccdf:Tailoring> document is only applicable to a single <xccdf:Benchmark>. Note, however, that this is a purely informative field.
    :ivar status: Status of the tailoring and date at which it attained that status. Authors may use this element to record the maturity or consensus level of an <xccdf:Tailoring> element.
    :ivar dc_status: Holds additional status information using the Dublin Core format.
    :ivar version: The version of this <xccdf:Tailoring> element, with a required @time attribute that records when the <xccdf:Tailoring> element was created. This timestamp is necessary because, under some circumstances, a copy of an <xccdf:Tailoring> document might be automatically generated. Without the version and timestamp, tracking of these automatically created <xccdf:Tailoring> documents could become problematic.
    :ivar metadata: XML metadata for the <xccdf:Tailoring> element.
    :ivar profile: <xccdf:Profile> elements that reference and customize sets of items in an <xccdf:Benchmark>.
    :ivar signature: A digital signature asserting authorship and allowing verification of the integrity of the <xccdf:Tailoring>.
    :ivar id: Unique identifier for this element.
    :ivar id_attribute: An identifier used for referencing elements included in an XML signature.
    """

    class Meta:
        namespace = XCCDF_1_2_NAMESPACE

    benchmark: Optional[TailoringBenchmarkReference] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    status: List[Status] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": XCCDF_1_2_NAMESPACE,
        }
    )
    dc_status: List[DcStatus] = field(
        default_factory=list,
        metadata={
            "name": "dc-status",
            "type": "Element",
        }
    )
    version: Optional[TailoringVersion] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    metadata: List[Metadata] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    profile: List[Profile] = field(
        default_factory=list,
        metadata={
            "name": "Profile",
            "type": "Element",
            "namespace": XCCDF_1_2_NAMESPACE,
            "min_occurs": 1,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"xccdf_[^_]+_tailoring_.+",
        }
    )
    id_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )


@dataclass
class Value(Item):
    """

    The <xccdf:Value> element is a named parameter that can be substituted into properties of other elements within
    the <xccdf:Benchmark>, including the interior of structured check specifications and fix scripts.

    :ivar value: A simple (number, string, or boolean) value associated with this <xccdf:Value>. At any time an <xccdf:Value> has one active (simple or complex) value. If a selector value has been provided under <xccdf:Profile> selection or tailoring then the active <xccdf:value>/<xccdf:complex-value> is the one with a matching @selector. If there is no provided selector or if the provided selector does not match the @selector attribute of any <xccdf:value> or <xccdf:complex-value>, the active <xccdf:value>/<xccdf:complex-value> is the one with an empty or absent @selector or, failing that, the first <xccdf:value> or <xccdf:complex-value> in the XML. When an <xccdf:Value> is exported or used in text substitution, it is the currently active <xccdf:value> or <xccdf:complex-value> that is actually used. If there are multiple <xccdf:value> and/or <xccdf:complex-value> elements, only one may omit a @selector attribute and no two may have the same @selector value.
    :ivar complex_value: A complex (list) value associated with this <xccdf:Value>. See the description of the <xccdf:value> property for <xccdf:Rule> elements regarding activation of an <xccdf:complex-value>.
    :ivar default: The default value displayed to the user as a suggestion by benchmark producers during tailoring of this <xccdf:Value> element. (This is not the default value of an <xccdf:Value>; it is just the default display.) If there are multiple <xccdf:default> and/or <xccdf:complex-default> elements, only one may omit a @selector attribute and no two may have the same @selector value.
    :ivar complex_default: The default <xccdf:complex-value> displayed to the user as a suggestion by benchmark producers during tailoring of this <xccdf:Value> element. (This is not the default value of an <xccdf:Value>; it is just the default display.) If there are multiple <xccdf:default> and <xccdf:complex-default> elements, only one may omit a @selector attribute and no two may have the same @selector value.
    :ivar match: A Perl Compatible Regular Expression that a benchmark producer may apply during tailoring to validate a user’s input for the <xccdf:Value>. It uses implicit anchoring. It applies only when the @type property is “string” or “number” or a list of strings and/or numbers.
    :ivar lower_bound: Minimum legal value for this <xccdf:Value>. It is used to constrain value input during tailoring, when the @type property is “number”. Values supplied by the user for tailoring the <xccdf:Benchmark> must be equal to or greater than this number.
    :ivar upper_bound: Maximum legal value for this <xccdf:Value>. It is used to constrain value input during tailoring, when the @type is “number”. Values supplied by the user for tailoring the <xccdf:Benchmark> must be less than or equal to than this number.
    :ivar choices: A list of legal or suggested choices (values) for an <xccdf:Value> element, to be used during tailoring and document generation.
    :ivar source: URI indicating where the tool may acquire values, value bounds, or value choices for this <xccdf:Value> element. XCCDF does not attach any meaning to the URI; it may be an arbitrary community or tool-specific value, or a pointer directly to a resource. If several instances of the <xccdf:source> property appear, then they represent alternative means or locations for obtaining the value in descending order of preference (i.e., most preferred first).
    :ivar signature: A digital signature asserting authorship and allowing verification of the integrity of the <xccdf:Value>.
    :ivar id: The unique identifier for this element.
    :ivar type: The data type of the <xccdf:Value>. A tool may choose any convenient form to store an <xccdf:Value> element’s <xccdf:value> element, but the @type attribute conveys how the <xccdf:Value> should be treated for user input validation purposes during tailoring processing. The @type attribute may also be used to give additional guidance to the user or to validate the user’s input. In the case of a list of values, the @type attribute, if present, applies to all elements of the list individually.
    :ivar operator: The operator to be used for comparing this <xccdf:Value> to some part of the test system’s configuration during <xccdf:Rule> checking.
    :ivar interactive: Whether tailoring for this <xccdf:Value> should be performed during <xccdf:Benchmark> application. The benchmark consumer may ignore the attribute if asking the user is not feasible or not supported.
    :ivar interface_hint: A hint or recommendation to a benchmark consumer or producer about how the user might select or adjust the <xccdf:Value>.
    """

    class Meta:
        namespace = XCCDF_1_2_NAMESPACE

    value: List[SelString] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    complex_value: List[SelComplexValue] = field(
        default_factory=list,
        metadata={
            "name": "complex-value",
            "type": "Element",
            "sequential": True,
        }
    )
    default: List[SelString] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    complex_default: List[SelComplexValue] = field(
        default_factory=list,
        metadata={
            "name": "complex-default",
            "type": "Element",
            "sequential": True,
        }
    )
    match: List[SelString] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    lower_bound: List[SelNum] = field(
        default_factory=list,
        metadata={
            "name": "lower-bound",
            "type": "Element",
        }
    )
    upper_bound: List[SelNum] = field(
        default_factory=list,
        metadata={
            "name": "upper-bound",
            "type": "Element",
        }
    )
    choices: List[SelChoices] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    source: List[UriRef] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"xccdf_[^_]+_value_.+",
        }
    )
    type: ValueType = field(
        default=ValueType.STRING,
        metadata={
            "type": "Attribute",
        }
    )
    operator: ValueOperator = field(
        default=ValueOperator.EQUALS,
        metadata={
            "type": "Attribute",
        }
    )
    interactive: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    interface_hint: Optional[InterfaceHint] = field(
        default=None,
        metadata={
            "name": "interfaceHint",
            "type": "Attribute",
        }
    )


@dataclass
class Rule(SelectableItem):
    """

    The <xccdf:Rule> element contains the description for a single item of guidance or constraint. <xccdf:Rule>
    elements form the basis for testing a target platform for compliance with an <xccdf:Benchmark>, for scoring,
    and for conveying descriptive prose, identifiers, references, and remediation information.

    :ivar ident: A globally meaningful identifier for this <xccdf:Rule>. This may be the name or identifier of a security configuration issue or vulnerability that the <xccdf:Rule> assesses.
    :ivar impact_metric: The potential impact of failure to conform to the <xccdf:Rule>, expressed as a CVSS 2.0 base vector.
    :ivar profile_note: Text that describes special aspects of the <xccdf:Rule> related to one or more <xccdf:Profile> elements. This allows an author to document things within <xccdf:Rule> elements that are specific to a given <xccdf:Profile>, and then select the appropriate text based on the selected <xccdf:Profile> and display it to the reader.
    :ivar fixtext: Data that describes how to bring a target system into compliance with this <xccdf:Rule>.
    :ivar fix: A command string, script, or other system modification statement that, if executed on the target system, can bring it into full, or at least better, compliance with this <xccdf:Rule>.
    :ivar check: The definition of, or a reference to, the target system check needed to test compliance with this <xccdf:Rule>. Sibling <xccdf:check> elements must have different values for the combination of their @selector and @system attributes, and must have different values for their @id attribute (if any).
    :ivar complex_check: A boolean expression composed of operators (and, or, not) and individual checks.
    :ivar signature: A digital signature asserting authorship and allowing verification of the integrity of the <xccdf:Rule>.
    :ivar id: Unique element identifier used by other elements to refer to this element.
    :ivar role: The <xccdf:Rule> element’s role in scoring and reporting.
    :ivar severity: Severity level code to be used for metrics and tracking.
    :ivar multiple: Applicable in cases where there are multiple instances of a target. For example, an <xccdf:Rule> may provide a recommendation about the configuration of application user accounts, but an application may have many user accounts. Each account would be considered an instance of the broader assessment target of user accounts. If the @multiple attribute is set to true, each instance of the target to which the <xccdf:Rule> can apply should be tested separately and the results should be recorded separately. If @multiple is set to false, the test results of such instances should be combined. If the checking system does not combine these results automatically, the results of each instance should be ANDed together to produce a single result. If the benchmark consumer cannot perform multiple instantiation, or if multiple instantiation of the <xccdf:Rule> is not applicable for the target system, then the benchmark consumer may ignore this attribute.
    """

    class Meta:
        namespace = XCCDF_1_2_NAMESPACE

    ident: List[Ident] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    impact_metric: Optional[str] = field(
        default=None,
        metadata={
            "name": "impact-metric",
            "type": "Element",
        }
    )
    profile_note: List[ProfileNote] = field(
        default_factory=list,
        metadata={
            "name": "profile-note",
            "type": "Element",
        }
    )
    fixtext: List[FixText] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fix: List[Fix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    check: List[Check] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    complex_check: Optional[ComplexCheck] = field(
        default=None,
        metadata={
            "name": "complex-check",
            "type": "Element",
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"xccdf_[^_]+_rule_.+",
        }
    )
    role: Role = field(
        default=Role.FULL,
        metadata={
            "type": "Attribute",
        }
    )
    severity: Severity = field(
        default=Severity.UNKNOWN,
        metadata={
            "type": "Attribute",
        }
    )
    multiple: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Group(SelectableItem):
    """

    An item that can hold other items. It allows an author to collect related items into a common structure and
    provide descriptive text and references about them.

    :ivar value: <xccdf:Value> elements that belong to this <xccdf:Group>.
    :ivar group: Sub-<xccdf:Groups> under this <xccdf:Group>.
    :ivar rule: <xccdf:Rule> elements that belong to this <xccdf:Group>.
    :ivar signature: A digital signature asserting authorship and allowing verification of the integrity of the <xccdf:Group>.
    :ivar id: Unique element identifier; used by other elements to refer to this element.
    """

    class Meta:
        namespace = XCCDF_1_2_NAMESPACE

    value: List[Value] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": XCCDF_1_2_NAMESPACE,
        }
    )
    group: List["Group"] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
            "namespace": XCCDF_1_2_NAMESPACE,
            "sequential": True,
        }
    )
    rule: List[Rule] = field(
        default_factory=list,
        metadata={
            "name": "Rule",
            "type": "Element",
            "namespace": XCCDF_1_2_NAMESPACE,
            "sequential": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"xccdf_[^_]+_group_.+",
        }
    )


@dataclass
class Benchmark(ParsableElement):
    """

    This is the root element of the XCCDF document; it must appear exactly once. It encloses the entire benchmark,
    and contains both descriptive information and structural information. Note that the order of <xccdf:Group> and
    <xccdf:Rule> child elements may matter for the appearance of a generated document. <xccdf:Group> and <xccdf:Rule>
    children may be freely intermingled, but they must appear after any <xccdf:Value> children. All the other
    children must appear in the order shown.

    :ivar status: Status of the <xccdf:Benchmark> indicating its level of maturity or consensus. If more than one <xccdf:status> element appears, the element's @date attribute should be included.
    :ivar dc_status: Holds additional status information using the Dublin Core format.
    :ivar title: Title of the <xccdf:Benchmark>; an <xccdf:Benchmark> should have an <xccdf:title>.
    :ivar description: Text that describes the <xccdf:Benchmark>; an <xccdf:Benchmark> should have an <xccdf:description>.
    :ivar notice: Legal notices (licensing information, terms of use, etc.), copyright statements, warnings, and other advisory notices about this <xccdf:Benchmark> and its use.
    :ivar front_matter: Introductory matter for the beginning of the <xccdf:Benchmark> document; intended for use during Document Generation.
    :ivar rear_matter: Concluding material for the end of the <xccdf:Benchmark> document; intended for use during Document Generation.
    :ivar reference: Supporting references for the <xccdf:Benchmark> document.
    :ivar plain_text: Definitions for reusable text blocks, each with a unique identifier.
    :ivar platform_specification: A list of identifiers for complex platform definitions, written in CPE applicability language format. Authors may define complex platforms within this element, and then use their locally unique identifiers anywhere in the <xccdf:Benchmark> element in place of a CPE name.
    :ivar platform: Applicable platforms for this <xccdf:Benchmark>. Authors should use the element to identify the systems or products to which the <xccdf:Benchmark> applies.
    :ivar version: Version number of the <xccdf:Benchmark>.
    :ivar metadata: XML metadata for the <xccdf:Benchmark>. Metadata allows many additional pieces of information, including authorship, publisher, support, and other similar details, to be embedded in an <xccdf:Benchmark>.
    :ivar model: URIs of suggested scoring models to be used when computing a score for this <xccdf:Benchmark>. A suggested list of scoring models and their URIs is provided in the XCCDF specification.
    :ivar profile: <xccdf:Profile> elements that reference and customize sets of items in the <xccdf:Benchmark>.
    :ivar value: Parameter <xccdf:Value> elements that support <xccdf:Rule> elements and descriptions in the <xccdf:Benchmark>.
    :ivar group: <xccdf:Group> elements that comprise the <xccdf:Benchmark>; each may contain additional <xccdf:Value>, <xccdf:Rule>, and other <xccdf:Group> elements.
    :ivar rule: <xccdf:Rule> elements that comprise the <xccdf:Benchmark>.
    :ivar test_result: <xccdf:Benchmark> test result records (one per <xccdf:Benchmark> run).
    :ivar signature: A digital signature asserting authorship and allowing verification of the integrity of the <xccdf:Benchmark>.
    :ivar id: Unique <xccdf:Benchmark> identifier.
    :ivar id_attribute: An identifier used for referencing elements included in an XML signature.
    :ivar resolved: True if <xccdf:Benchmark> has already undergone the resolution process.
    :ivar style: Name of an <xccdf:Benchmark> authoring style or set of conventions or constraints to which this <xccdf:Benchmark> conforms (e.g., “SCAP 1.2”).
    :ivar style_href: URL of a supplementary stylesheet or schema extension that can be used to verify conformance to the named style.
    :ivar lang:
    """

    class Meta:
        namespace = XCCDF_1_2_NAMESPACE

    status: List[Status] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    dc_status: List[DcStatus] = field(
        default_factory=list,
        metadata={
            "name": "dc-status",
            "type": "Element",
        }
    )
    title: List[Text] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    description: List[HtmlTextWithSub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    notice: List[Notice] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    front_matter: List[HtmlTextWithSub] = field(
        default_factory=list,
        metadata={
            "name": "front-matter",
            "type": "Element",
        }
    )
    rear_matter: List[HtmlTextWithSub] = field(
        default_factory=list,
        metadata={
            "name": "rear-matter",
            "type": "Element",
        }
    )
    reference: List[Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    plain_text: List[PlainText] = field(
        default_factory=list,
        metadata={
            "name": "plain-text",
            "type": "Element",
        }
    )
    platform_specification: Optional[PlatformSpecification] = field(
        default=None,
        metadata={
            "name": "platform-specification",
            "type": "Element",
            "namespace": "http://cpe.mitre.org/language/2.0",
        }
    )
    platform: List[Cpe2Idref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    version: Optional[Version] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    metadata: List[Metadata] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    model: List[Model] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    profile: List[Profile] = field(
        default_factory=list,
        metadata={
            "name": "Profile",
            "type": "Element",
        }
    )
    value: List[Value] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
        }
    )
    group: List[Group] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
            "sequential": True,
        }
    )
    rule: List[Rule] = field(
        default_factory=list,
        metadata={
            "name": "Rule",
            "type": "Element",
            "sequential": True,
        }
    )
    test_result: List[TestResult] = field(
        default_factory=list,
        metadata={
            "name": "TestResult",
            "type": "Element",
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"xccdf_[^_]+_benchmark_.+",
        }
    )
    id_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        }
    )
    resolved: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    style_href: Optional[str] = field(
        default=None,
        metadata={
            "name": "style-href",
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
