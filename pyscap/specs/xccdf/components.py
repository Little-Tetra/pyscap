from dataclasses import dataclass, field
from decimal import Decimal
from typing import Dict, List, Optional

from xsdata.models.datatype import XmlDateTime

from .common import TextType, SubType, HtmlTextWithSubType
from .enums import (
    ValueTypeType,
    MsgSevEnumType,
    ResultEnumType,
    SeverityEnumType,
    RoleEnumType,
    ValueOperatorType,
    CcOperatorEnumType,
    FixStrategyEnumType,
    RatingEnumType,
    WarningCategoryEnumType
)


# Benchmark-related types

@dataclass
class NoticeType:
    """Data type for an <xccdf:notice> element.

    <xccdf:notice> elements are used to include legal notices
    (licensing information, terms of use, etc.), copyright statements,
    warnings, and other advisory notices about this
    <xccdf:Benchmark> and its use. This information may be
    expressed using XHTML or may be a simply text expression. Each
    <xccdf:notice> element must have a unique identifier.

    :ivar w3_org_1999_xhtml_element:
    :ivar id: The unique identifier for this
        <xccdf:notice>.
    :ivar base:
    :ivar lang:
    """

    class Meta:
        name = "noticeType"

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
class DcStatusType:
    """
    Data type element for the <xccdf:dc-status> element, which holds
    status information about its parent element using the Dublin Core format,
    expressed as elements of the DCMI Simple DC Element specification.
    """

    class Meta:
        name = "dc-statusType"

    purl_org_dc_elements_1_1_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://purl.org/dc/elements/1.1/",
            "min_occurs": 1,
        }
    )


@dataclass
class PlainTextType:
    """The data type for an <xccdf:plain-text> element, which is a
    reusable text block for reference by the <xccdf:sub> element. This
    allows text to be defined once and then reused multiple times. Each.

    <xccdf:plain-text> element mush have a unique id.

    :ivar value:
    :ivar id: The unique identifier for this
        <xccdf:plain-text> element.
    """

    class Meta:
        name = "plainTextType"

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
class ReferenceType:
    """This element provides supplementary descriptive text for a XCCDF
    elements. When used, it has either a simple string value or a value
    consisting of simple Dublin Core elements. If a bare string appears, then
    it is taken to be the string content for a Dublin Core title element.
    Multiple.

    <xccdf:reference> elements may appear; a document generation
    processing tool may concatenate them, or put them into a reference
    list, and may choose to number them.

    :ivar purl_org_dc_elements_1_1_element:
    :ivar href: A URL pointing to the referenced
        resource.
    :ivar override: Used to manage inheritance
        processing.
    """

    class Meta:
        name = "referenceType"

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


@dataclass
class SignatureType:
    """
    The type of an <XMLDSig:signature> element, which holds an enveloped
    digital signature asserting authorship and allowing verification of the
    integrity of associated data (e.g., its parent element, other documents,
    portions of other documents).
    """

    class Meta:
        name = "signatureType"

    w3_org_2000_09_xmldsig_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )


@dataclass
class MetadataType:
    """Data type that supports inclusion of metadata about a document or
    element.

    This is particularly useful for facilitating the discovery and
    retrieval of XCCDF checklists from public repositories. When used,
    the contents of the <xccdf:metadata> element are expressed in
    XML. The <xccdf:Benchmark> element's metadata should contain
    information formatted using the Dublin Core Metadata Initiative
    (DCMI) Simple DC Element specification, as described in [DCES] and
    [DCXML]. Benchmark consumers should be prepared to process Dublin
    Core metadata in the <xccdf:metadata> element. Other metadata
    schemes, including ad-hoc elements, are also allowed, both in the
    <xccdf:Benchmark> and in other elements.
    """

    class Meta:
        name = "metadataType"

    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "min_occurs": 1,
        }
    )


# Value-related types

@dataclass
class ComplexValueType:
    """Data type that supports values that are lists of simple types. Each
    element in the list is represented by an instance of the.

    <xccdf:item> child element. If there are no <xccdf:item>
    child elements then this represents an empty list.

    :ivar item: A single item in the list of values.
    """

    class Meta:
        name = "complexValueType"

    item: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class SelComplexValueType(ComplexValueType):
    """
    Data type that supports values that are lists of simple types with an
    associated @selector attribute used in tailoring.

    :ivar selector: This may be referenced from
        <xccdf:Profile> selection elements or used during manual
        tailoring                             to refine the application
        of this property. If no selectors are
        specified for a given item by <xccdf:Profile> elements or
        manual                             tailoring, properties with
        empty or non-existent @selector attributes
        are activated. If a selector is applied that does not match the
        @selector attribute of any of a given type of property, then no
        <xccdf:choices> element is considered activated. The only
        exception is the <xccdf:value> and <xccdf:complex-
        value>                             properties of an
        <xccdf:Value> element - if there is no
        <xccdf:value> or <xccdf:complex-value> property with
        a                             matching @selector value then the
        <xccdf:value>/<xccdf:complex-value> property with an
        empty                             or absent @selector attribute
        becomes active. If there is no such
        <xccdf:value> or <xccdf:complex-value>, then the
        first                             <xccdf:value> or
        <xccdf:complex-value> listed becomes
        active. This reflects the fact that all <xccdf:Value>
        elements                             require an active value
        property at all times.
    """

    class Meta:
        name = "selComplexValueType"

    selector: str = field(
        default="",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SelChoicesType:
    """
    The type of the <xccdf:choice> element, which specifies a list of
    legal or suggested choices for an <xccdf:Value> object.

    :ivar choice: A single choice holding a simple type. (I.e.,
        number, string, or boolean.)
    :ivar complex_choice: A single choice holding a list of simple
        types.
    :ivar must_match: True if the listed choices are the only
        permissible                     settings for the given
        <xccdf:Value>. False if choices not specified in
        this <xccdf:choices> element are acceptable settings for
        this                     <xccdf:Value>.
    :ivar selector: This may be referenced from <xccdf:Profile>
        selection elements or used during manual tailoring to refine the
        application of                     the <xccdf:Rule>. If no
        selectors are specified for a given
        <xccdf:Value> by <xccdf:Profile> elements or manual
        tailoring, an                     <xccdf:choice> element
        with an empty or non-existent @selector attribute
        is activated. If a selector is applied that does not match the
        @selector                     attribute of any
        <xccdf:choices> element, then no <xccdf:choices>
        element is considered activated.
    """

    class Meta:
        name = "selChoicesType"

    choice: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    complex_choice: List[ComplexValueType] = field(
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
class SelStringType:
    """
    This type is for an element that has string content and a @selector
    attribute for use in tailoring.

    :ivar value:
    :ivar selector: This may be referenced from
        <xccdf:Profile> selection elements or used during manual
        tailoring                             to refine the application
        of this property. If no selectors are
        specified for a given property by <xccdf:Profile> elements
        or                             manual tailoring, properties with
        empty or non-existent @selector
        attributes are activated. If a selector is applied that does not
        match                             the @selector attribute of any
        of a given type of property, then no
        property of that type is considered activated. The only
        exception is the                             <xccdf:value>
        and <xccdf:complex-value> properties of an
        <xccdf:Value> element - if there is no <xccdf:value>
        or                             <xccdf:complex-value>
        property with a matching @selector value
        then the <xccdf:value>/<xccdf:complex-value>
        property with                             an empty or absent
        @selector attribute becomes active. If there is no
        such <xccdf:value> or <xccdf:complex-value>, then
        the first                             <xccdf:value> or
        <xccdf:complex-value> listed in the XML
        becomes active. This reflects the fact that all
        <xccdf:Value>                             elements require
        an active value property at all
        times.
    """

    class Meta:
        name = "selStringType"

    value: Optional[str] = field(
        default=None,
    )
    selector: str = field(
        default="",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SelNumType:
    """
    This type is for an element that has numeric content and a @selector
    attribute for use during tailoring.

    :ivar value:
    :ivar selector: This may be referenced from
        <xccdf:Profile> selection elements or used during manual
        tailoring                             to refine the application
        of this property. If no selectors are
        specified for a given property by <xccdf:Profile> elements
        or                             manual tailoring, properties with
        empty or non-existent @selector
        attributes are activated. If a selector is applied that does not
        match                             the @selector attribute of any
        of a given type of property, then no
        property of that type considered activated.
    """

    class Meta:
        name = "selNumType"

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
class UriRefType:
    """
    Data type for elements that have no content and a single @uri attribute.

    :ivar uri: A URI.
    """

    class Meta:
        name = "uriRefType"

    uri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


# Rule-related types

@dataclass
class IdentType:
    """Data type for the <xccdf:ident> element, a globally meaningful
    identifier for an <xccdf:Rule>. The body of.

    <xccdf:ident> element is the name or identifier of a security
    configuration issue or vulnerability that the <xccdf:Rule>
    addresses. It has an associated URI that denotes the organization or
    naming scheme that assigned the name. By setting an
    <xccdf:ident> element on an <xccdf:Rule>, the
    <xccdf:Benchmark> author effectively declares that the
    <xccdf:Rule> instantiates, implements, or remediates the issue
    for which the name was assigned.

    :ivar value:
    :ivar system: Denotes the organization or naming scheme
        that assigned the identifier.
    :ivar other_attributes: May also have other attributes from other
        namespaces in order to provide additional metadata for the given
        identifier.
    """

    class Meta:
        name = "identType"

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
class WarningType(HtmlTextWithSubType):
    """Data type for the <xccdf:warning> element under the
    <xccdf:Rule> element.

    This element holds a note or caveat about the item intended to
    convey important cautionary information for the
    <xccdf:Benchmark> user.

    :ivar content:
    :ivar category: A hint as to the nature of the
        warning.
    """

    class Meta:
        name = "warningType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    category: WarningCategoryEnumType = field(
        default=WarningCategoryEnumType.GENERAL,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class FixTextType(HtmlTextWithSubType):
    """Data type for the <xccdf:fixtext> element, which contains data
    that describes how to bring a target system into compliance with an.

    <xccdf:Rule>. Each <xccdf:fixtext> element may be
    associated with one or more <xccdf:fix> elements through the
    @fixref attribute. The body holds explanatory text about the fix
    procedures.

    :ivar content:
    :ivar fixref: A reference to the @id of an
        <xccdf:fix> element.
    :ivar reboot: True if a reboot is known to be required
        and false otherwise.
    :ivar strategy: The method or approach for making the
        described fix.
    :ivar disruption: An estimate of the potential for disruption
        or operational degradation that the application of this fix will
        impose                             on the target.
    :ivar complexity: The estimated complexity or difficulty of
        applying the fix to the target.
    """

    class Meta:
        name = "fixTextType"

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
    strategy: FixStrategyEnumType = field(
        default=FixStrategyEnumType.UNKNOWN,
        metadata={
            "type": "Attribute",
        }
    )
    disruption: RatingEnumType = field(
        default=RatingEnumType.UNKNOWN,
        metadata={
            "type": "Attribute",
        }
    )
    complexity: RatingEnumType = field(
        default=RatingEnumType.UNKNOWN,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class InstanceFixType:
    """Type for an <xccdf:instance> element which may appear in an
    <xccdf:fix> element. The <xccdf:instance> element inside an.

    <xccdf:fix> element designates a spot where the name of the
    instance should be substituted into the fix template to generate the
    final fix data.

    :ivar context: Describes the scope or significance of the instance
        content. The context attribute is intended to be informative and
        does not affect                     basic processing.
    """

    class Meta:
        name = "instanceFixType"

    context: str = field(
        default="undefined",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class FixType:
    """Data type for the <xccdf:fix> element.

    The body of this element contains a command string, script, or other
    system modification statement that, if executed on the target
    system, can bring it into full, or at least better, compliance with
    this <xccdf:Rule>.

    :ivar content:
    :ivar sub: Specifies an <xccdf:Value> or
        <xccdf:plain-text> element to be used for text
        substitution
    :ivar instance: Designates a spot where the name of the
        instance should be substituted into the fix template to generate
        the final                         fix data. If the @context
        attribute is omitted, the value of the @context
        defaults to “undefined”.
    :ivar id: A local identifier for the element. It is optional
        for the @id to be unique; multiple <xccdf:fix> elements
        may have the same                     @id but different values
        for their other attributes. It is used primarily to
        allow <xccdf:fixtext> elements to be associated with one
        or more                     <xccdf:fix> elements
    :ivar reboot: True if a reboot is known to be required and false
        otherwise.
    :ivar strategy: The method or approach for making the described
        fix.
    :ivar disruption: An estimate of the potential for disruption or
        operational degradation that the application of this fix will
        impose on the                     target.
    :ivar complexity: The estimated complexity or difficulty of applying
        the fix to the target.
    :ivar system: A URI that identifies the scheme, language, engine,
        or process for which the fix contents are written. Table 17 in
        the XCCDF                     specification defines several
        general-purpose URNs that may be used for this,
        and tool vendors and system providers may define and use target-
        specific                     URNs.
    :ivar platform: In case different fix scripts or procedures are
        required for different target platform types (e.g., different
        patches for                     Windows Vista and Windows 7),
        this attribute allows a CPE name or CPE
        applicability language expression to be associated with an
        <xccdf:fix>                     element. This should
        appear on an <xccdf:fix> when the content applies to
        only one platform out of several to which the <xccdf:Rule>
        could apply.
    """

    class Meta:
        name = "fixType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    sub: List[SubType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    instance: List[InstanceFixType] = field(
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
    strategy: FixStrategyEnumType = field(
        default=FixStrategyEnumType.UNKNOWN,
        metadata={
            "type": "Attribute",
        }
    )
    disruption: RatingEnumType = field(
        default=RatingEnumType.UNKNOWN,
        metadata={
            "type": "Attribute",
        }
    )
    complexity: RatingEnumType = field(
        default=RatingEnumType.UNKNOWN,
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
class CheckImportType:
    """Data type for the <xccdf:check-import> element, which specifies a
    value that the <xccdf:Benchmark> author wishes to retrieve from the
    checking system during testing of a target system.

    The @import-name attribute identifies some structure in the checking
    system that is then retrieved. The mapping from the values of this
    attribute to specific checking system structures is beyond the scope
    of the XCCDF specification. When the <xccdf:check-import>
    element appears in the context of an <xccdf:Rule>, then it
    should be empty and any content must be ignored. When the
    <xccdf:check-import> element appears in the context of an
    <xccdf:rule-result>, then its body holds the imported value.

    :ivar any_element:
    :ivar import_name: An identifier indicating some structure in the
        checking system to be collected.
    :ivar import_xpath: An XPath that is used to select specific values
        or                     structures from the imported structure.
        This allows further refinement of the
        collected data if the imported value takes the form of XML
        structures.
    """

    class Meta:
        name = "checkImportType"

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
class CheckExportType:
    """Data type for the <xccdf:check-export> element, which specifies a
    mapping from an <xccdf:Value> element to a checking system variable
    (i.e., external name or id for use by the checking system). This supports
    export of tailoring <xccdf:Value> elements from the XCCDF processing
    environment to the checking system. The interface between the XCCDF
    benchmark consumer and the checking system should support, at a minimum,
    passing the.

    <xccdf:value> property of the <xccdf:Value> element, but
    may also support passing the <xccdf:Value> element's @type and
    @operator properties.

    :ivar value_id: The id of the <xccdf:Value> element to
        export.
    :ivar export_name: An identifier indicating some structure in the
        checking system into which the identified <xccdf:Value>
        element's                     properties will be mapped.
    """

    class Meta:
        name = "checkExportType"

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
class CheckContentRefType:
    """Data type for the <xccdf:check-content-ref> element, which points
    to the code for a detached check in another file.

    This element has no body, just a couple of attributes: @href and
    @name. The @name is optional, if it does not appear then this
    reference is to the entire document.

    :ivar href: Identifies the referenced document containing
        checking instructions.
    :ivar name: Identifies a particular part or element of the
        referenced check document.
    """

    class Meta:
        name = "checkContentRefType"

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
class CheckContentType:
    """Data type for the <xccdf:check-content> element.

    The body of this element holds the actual code of a check, in the
    language or system specified by the <xccdf:check> element’s
    @system attribute. The body of this element may be any XML, but
    cannot contain any XCCDF elements. XCCDF tools do not process its
    content directly but instead pass the content directly to checking
    engines.
    """

    class Meta:
        name = "checkContentType"

    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "mixed": True,
        }
    )


@dataclass
class CheckType:
    """Data type for the <xccdf:check> element. The.

    <xccdf:check> element identifies instructions for tests to
    determine compliance with the <xccdf:Rule> as well as
    parameters controlling the reporting of those test results. The
    <xccdf:check> element must have at least one child element.

    :ivar check_import: Identifies a value to be retrieved from the
        checking system during testing of a target system. This
        element's body must                         be empty within an
        <xccdf:check>. After the associated check results
        have been collected, the result structure returned by the
        checking engine is                         processed to collect
        the named information. This information is then
        recorded in the check-import element in the corresponding
        <xccdf:rule-result>.
    :ivar check_export: A mapping from an <xccdf:Value> element
        to a checking system variable (i.e., external name or id for use
        by the                         checking system). This supports
        export of tailoring values from the XCCDF
        processing environment to the checking system.
    :ivar check_content_ref: Points to code for a detached check in
        another                         location that uses the language
        or system specified by the
        <xccdf:check> element’s @system attribute. If multiple
        <xccdf:check-content-ref> elements appear, they represent
        alternative                         locations from which a
        benchmark consumer may obtain the check content.
        Benchmark consumers should process the alternatives in the order
        in which                         they appear in the XML. The
        first <xccdf:check-content-ref> from which
        content can be successfully retrieved should be used.
    :ivar check_content: Holds the actual code of a check, in the
        language or system specified by the <xccdf:check>
        element’s @system                         attribute. If both
        <xccdf:check-content-ref> and
        <xccdf:check-content> elements appear in a single
        <xccdf:check>                         element, benchmark
        consumers should use the <xccdf:check-content>
        element only if none of the references can be resolved to
        provide                         content.
    :ivar system: The URI for a checking system. If the checking
        system uses XML namespaces, then the system attribute for the
        system should be                     its namespace.
    :ivar negate: If set to true, the final result of the
        <xccdf:check> is negated according to the truth table
        given below.
    :ivar id: Unique identifier for this element. Optional, but
        must be globally unique if present.
    :ivar selector: This may be referenced from <xccdf:Profile>
        selection elements or used during manual tailoring to refine the
        application of                     the <xccdf:Rule>. If no
        selector values are specified for a given
        <xccdf:Rule> by <xccdf:Profile> elements or manual
        tailoring, all                     <xccdf:check> elements
        with non-empty @selector attributes are ignored. If
        an <xccdf:Rule> has multiple <xccdf:check> elements
        with the same                     @selector attribute, each must
        employ a different checking system, as identified
        by the @system attribute of the <xccdf:check> element.
    :ivar multi_check: Applicable in cases where multiple checks are
        executed to determine compliance with a single
        <xccdf:Rule>. This                     situation can arise
        when an <xccdf:check> includes an
        <xccdf:check-content-ref> element that does not include a
        @name attribute.                     The default behavior of a
        nameless <xccdf:check-content-ref> is to execute
        all checks in the referenced check content location and AND
        their results                     together into a single
        <xccdf:rule-result> using the AND truth table
        below. This corresponds to a @multi-check attribute value of
        “false”. If,                     however, the @multi-check
        attribute is set to "true" and a nameless
        <xccdf:check-content-ref> is used, the <xccdf:Rule>
        produces a                     separate <xccdf:rule-
        result> for each check.
    :ivar base:
    """

    class Meta:
        name = "checkType"

    check_import: List[CheckImportType] = field(
        default_factory=list,
        metadata={
            "name": "check-import",
            "type": "Element",
        }
    )
    check_export: List[CheckExportType] = field(
        default_factory=list,
        metadata={
            "name": "check-export",
            "type": "Element",
        }
    )
    check_content_ref: List[CheckContentRefType] = field(
        default_factory=list,
        metadata={
            "name": "check-content-ref",
            "type": "Element",
        }
    )
    check_content: Optional[CheckContentType] = field(
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
class ComplexCheckType:
    """The type for an element that contains a boolean combination of
    <xccdf:checks>. This element can have only.

    <xccdf:complex-check> and <xccdf:check> elements as
    children. Child elements may appear in any order but at least one
    child element must be present. It has two attributes, @operator and
    @negate, which dictate how <xccdf:check> or <xccdf:complex-
    check> child elements are to be combined. Truth tables for these
    operations appear below.

    :ivar check: Instructions for a single                         test.
    :ivar complex_check: A child <xccdf:complex-check>, allowing
        another level of logic in combining component checks.
    :ivar operator: Indicates whether the child <xccdf:check>
        and/or <xccdf:complex-check> elements of this
        <xccdf:complex-check>                     should be
        combined using an AND or OR operation
    :ivar negate: If true, negate the final result of this
        <xccdf:complex-check> after the child elements are
        combined using the                     identified operator.
    """

    class Meta:
        name = "complexCheckType"

    check: List[CheckType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    complex_check: List["ComplexCheckType"] = field(
        default_factory=list,
        metadata={
            "name": "complex-check",
            "type": "Element",
        }
    )
    operator: Optional[CcOperatorEnumType] = field(
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


# Profile-related types

@dataclass
class ProfileSelectType:
    """Type for the <xccdf:select> element in an.

    <xccdf:Profile>. This element designates an
    <xccdf:Rule>, <xccdf:Group>, or cluster of
    <xccdf:Rule> and <xccdf:Group> elements and overrides
    the @selected attribute on the designated items, providing a means
    for including or excluding <xccdf:Rule> elements from an
    assessment.

    :ivar remark: Explanatory material or other
        prose.
    :ivar idref: The @id value of an <xccdf:Rule> or
        <xccdf:Group>, or the @cluster-id value of one or more
        <xccdf:Rule>                     or <xccdf:Group>
        elements.
    :ivar selected: The new value for the indicated item's @selected
        property.
    """

    class Meta:
        name = "profileSelectType"

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
    selected: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ProfileSetValueType:
    """Type for the <xccdf:set-value> element in an.

    <xccdf:Profile>. This element upports the direct specification
    of simple value types such as numbers, strings, and boolean values.
    This overrides the <xccdf:value> and <xccdf:complex-
    value> element(s) of an <xccdf:Value> element.

    :ivar value:
    :ivar idref: The @id value of an <xccdf:Value> or
        the @cluster-id value of one or more <xccdf:Value>
        elements
    """

    class Meta:
        name = "profileSetValueType"

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


@dataclass
class ProfileSetComplexValueType(ComplexValueType):
    """Type for the <xccdf:set-complex-value> element in an
    <xccdf:Profile>. This element supports the direct specification of
    complex value types such as lists. Zero or more <xccdf:item> elements
    may appear as children of this element; if no child elements are present,
    this element represents an empty list. This overrides the
    <xccdf:value> and.

    <xccdf:complex-value> element(s) of an <xccdf:Value>
    element.

    :ivar idref: The @id value of an <xccdf:Value> or
        the @cluster-id value of one or more <xccdf:Value>
        elements
    """

    class Meta:
        name = "profileSetComplexValueType"

    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ProfileRefineValueType:
    """Type for the <xccdf:refine-value> element in an.

    <xccdf:Profile>. This element designates the
    <xccdf:Value> constraints to be applied during tailoring for
    an <xccdf:Value> element or the <xccdf:Value> members of
    a cluster.

    :ivar remark: Explanatory material or other
        prose.
    :ivar idref: The @id value of an <xccdf:Value> or the
        @cluster-id value of one or more <xccdf:Value> elements
    :ivar selector: Holds a selector value corresponding to the value
        of a @selector property in an <xccdf:Value> element's
        child properties.                     Properties with a matching
        @selector are considered active and all other
        properties are inactive. This may mean that, after selector
        application, some                     classes of
        <xccdf:Value> properties will be completely inactive
        because                     none of those properties had a
        matching @selector. The only exception is the
        <xccdf:value> and <xccdf:complex-value> properties
        of an                     <xccdf:Value> element - if there
        is no <xccdf:value> or
        <xccdf:complex-value> property with a matching @selector
        value then the
        <xccdf:value>/<xccdf:complex-value> property with an
        empty or absent                     @selector attribute becomes
        active. If there is no such <xccdf:value> or
        <xccdf:complex-value>, then the first <xccdf:value>
        or                     <xccdf:complex-value> listed in the
        XML becomes active. This reflects the                     fact
        that all <xccdf:Value> elements require an active value
        property at                     all times.
    :ivar operator: The new value for the identified
        <xccdf:Value> element's @operator property.
    """

    class Meta:
        name = "profileRefineValueType"

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
    selector: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    operator: Optional[ValueOperatorType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ProfileRefineRuleType:
    """Type for the <xccdf:refine-rule> element in an.

    <xccdf:Profile>. A <xccdf:refine-rule> element allows
    the author to select <xccdf:check> statements and override the
    @weight, @severity, and @role of an <xccdf:Rule>,
    <xccdf:Group>, or cluster of <xccdf:Rule> and
    <xccdf:Group> elements. Despite the name, this selector does
    apply for <xccdf:Group> elements and for clusters that include
    <xccdf:Group> elements, but it only affects their @weight
    attribute.

    :ivar remark: Explanatory material or other
        prose.
    :ivar idref: The @id value of an <xccdf:Rule> or
        <xccdf:Group>, or the @cluster-id value of one or more
        <xccdf:Rule>                     or <xccdf:Group>
        elements.
    :ivar weight: The new value for the identified element's @weight
        property.
    :ivar selector: Holds a selector value corresponding to the value
        of a @selector property in an <xccdf:Rule> element's
        <xccdf:check>                     element. If the selector
        specified does not match any of the @selector
        attributes specified on any of the <xccdf:check> children
        of an                     <xccdf:Rule>, then the
        <xccdf:check> child element without a
        @selector attribute is used. If there is no child without a
        @selector attribute,                     then that Rule would
        have no effective <xccdf:check>
        element.
    :ivar severity: The new value for the identified <xccdf:Rule>
        element's @severity property.
    :ivar role: The new value for the identified <xccdf:Rule>
        element's @role property.
    """

    class Meta:
        name = "profileRefineRuleType"

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
    severity: Optional[SeverityEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    role: Optional[RoleEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


# TestResult-related types


@dataclass
class BenchmarkReferenceType:
    """
    Type for a reference to the <xccdf:Benchmark> document.

    :ivar href: The URI of the <xccdf:Benchmark> document.
    :ivar id: The value of that <xccdf:Benchmark> element's
        @id attribute.
    """

    class Meta:
        name = "benchmarkReferenceType"

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


@dataclass
class ScoreType:
    """
    Type for a score value in an <xccdf:TestResult>.

    :ivar value:
    :ivar system: A URI indicating the scoring model used to
        create this score.
    :ivar maximum: The maximum possible score value that could
        have been achieved under the named scoring system.
    """

    class Meta:
        name = "scoreType"

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
class FactType:
    """Data type for an <xccdf:fact> element, which holds information
    about a target system: a name-value pair with a type.

    The content of the element is the value, and the @name attribute
    indicates the name. The @name is in the form of a URI that indicates
    the nature of the fact. A table of defined fact URIs appears in
    section 6.6.3 of the XCCDF specification. Additional URIs may be
    defined by authors to indicate additional kinds of facts.

    :ivar value:
    :ivar name: A URI that indicates the name of the fact.
    :ivar type: The data type of the fact value.
    """

    class Meta:
        name = "factType"

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
    type: ValueTypeType = field(
        default=ValueTypeType.BOOLEAN,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TargetFactsType:
    """Data type for the <xccdf:target-facts> elements in
    <xccdf:TestResult> elements.

    A <xccdf:target-facts> element holds a list of named facts
    about the target system or platform. Each fact is an element of type
    factType. Each <xccdf:fact> must have a name, but duplicate
    names are allowed. (For example, if you had a fact about MAC
    addresses, and the target system had three NICs, then you'd need
    three instances of the "urn:xccdf:fact:ethernet:MAC" fact.)

    :ivar fact: A named fact about the target system or
        platform.
    """

    class Meta:
        name = "targetFactsType"

    fact: List[FactType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class TargetIdRefType:
    """Type for an <xccdf:target-id-ref> element in an.

    <xccdf:TestResult> element. This element contains references
    to external structures with identifying information about the target
    of an assessment.

    :ivar system: Indicates the language in which this identifying
        information is expressed. If the identifying language uses XML
        namespaces, then                     the @system attribute for
        the language should be its                     namespace.
    :ivar href: Points to the external resource (e.g., a file) that
        contains the identifying information.
    :ivar name: Identifies a specific structure within the
        referenced file. If the @name attribute is absent, the reference
        is to the                     entire resource indicated in the
        @href attribute.
    """

    class Meta:
        name = "targetIdRefType"

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
class IdentityType:
    """Type for an <xccdf:identity> element in an.

    <xccdf:TestResult>. It contains information about the system
    identity or user employed during application of the
    <xccdf:Benchmark>. If used, shall specify the name of the
    authenticated identity.

    :ivar value:
    :ivar authenticated: Whether the identity was authenticated with
        the target system during the application of the
        <xccdf:Benchmark>.
    :ivar privileged: Whether the identity was granted
        administrative or other special privileges beyond those of a
        normal                             user.
    """

    class Meta:
        name = "identityType"

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
class TailoringReferenceType:
    """Type for the <xccdf:tailoring> element within an.

    <xccdf:TestResult>. This element is used to indicate the
    identity and location of an <xccdf:Tailoring> file that was
    used to create the assessment results.

    :ivar href: The URI of the <xccdf:Tailoring> file's
        location.
    :ivar id: The <xccdf:Tailoring> element's @id value.
    :ivar version: The value of the <xccdf:Tailoring> element's
        <xccdf:version> property.
    :ivar time: The value of the @time attribute in the
        <xccdf:Tailoring> element's <xccdf:version>
        property.
    """

    class Meta:
        name = "tailoringReferenceType"

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
class OverrideType:
    """Type for an <xccdf:override> element in an.

    <xccdf:rule-result>. This element is used to record manual
    modification or annotation of a particular <xccdf:rule-
    result>. All attributes and child elements are required. It will
    not always be the case that the <xccdf:new-result> value will
    differ from the <xccdf:old-result> value. They might match if
    an authority wished to make a remark on the result without changing
    it. If <xccdf:new-result> and <xccdf:old-result> differ,
    the <xccdf:result> element of the enclosing <xccdf:rule-
    result> must match the <xccdf:new-result> value.

    :ivar old_result: The <xccdf:rule-result> status before
        this override.
    :ivar new_result: The new, override <xccdf:rule-result>
        status.
    :ivar remark: Rationale or explanation text for why or how
        the override was applied.
    :ivar time: When the override was applied.
    :ivar authority: Name or other identification for the human
        principal authorizing the override.
    """

    class Meta:
        name = "overrideType"

    old_result: Optional[ResultEnumType] = field(
        default=None,
        metadata={
            "name": "old-result",
            "type": "Element",
            "required": True,
        }
    )
    new_result: Optional[ResultEnumType] = field(
        default=None,
        metadata={
            "name": "new-result",
            "type": "Element",
            "required": True,
        }
    )
    remark: Optional[TextType] = field(
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
class MessageType:
    """Type for a message generated by the checking engine or XCCDF tool during
    <xccdf:Benchmark> testing.

    The message is contained in string format in the body of the
    element.

    :ivar value:
    :ivar severity: Denotes the seriousness of the
        message.
    """

    class Meta:
        name = "messageType"

    value: Optional[str] = field(
        default=None,
    )
    severity: Optional[MsgSevEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class InstanceResultType:
    """Type for an <xccdf:instance> element in an.

    <xccdf:rule-result>. The content is a string, but the element
    may also have two attributes: @context and @parentContext. Both
    attributes are intended to provide hints as to the nature of the
    substituted content. This body of this type records the details of
    the target system instance for multiply instantiated
    <xccdf:Rule> elements.

    :ivar value:
    :ivar context: Describes the scope or significance of the
        instance content.
    :ivar parent_context: Used to express nested structure in
        instance context structures.
    """

    class Meta:
        name = "instanceResultType"

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


@dataclass
class RuleResultType:
    """Type for the <xccdf:rule-result> element within an
    <xccdf:TestResult>.

    An <xccdf:rule-result> holds the result of applying an
    <xccdf:Rule> from the <xccdf:Benchmark> to a target
    system or component of a target system.

    :ivar result: Result of applying the referenced
        <xccdf:Rule> to a target or target component. (E.g., Pass,
        Fail, etc.)
    :ivar override: An XML block explaining how and why an auditor
        chose to override the result.
    :ivar ident: A long-term globally meaningful identifier for
        the issue, vulnerability, platform, etc. copied from the
        referenced                         <xccdf:Rule>.
    :ivar metadata: XML metadata associated with this
        <xccdf:rule-result>.
    :ivar message: Diagnostic messages from the checking engine.
        These elements do not affect scoring; they are present merely to
        convey                         diagnostic information from the
        checking engine.
    :ivar instance: Name of the target subsystem or component to
        which this result applies, for a multiply instantiated
        <xccdf:Rule>.                         The element is
        important for an <xccdf:Rule> that applies to
        components of the target system, especially when a target might
        have several                         such components, and where
        the @multiple attribute of the <xccdf:Rule>
        is set to true.
    :ivar fix: Fix script for this target platform, if
        available (would normally appear only for result values of
        “fail”). It is                         assumed to have been
        ‘instantiated’ by the testing tool and any
        substitutions or platform selections already made.
    :ivar check: Encapsulated or referenced results to
        detailed testing output from the checking engine (if
        any).
    :ivar complex_check: A copy of the <xccdf:Rule> element’s
        <xccdf:complex-check> element where each component
        <xccdf:check> element of the <xccdf:complex-check>
        element                             is an encapsulated or
        referenced results to detailed testing output from
        the checking engine (if any) as described in the
        <xccdf:rule-result> <xccdf:check>
        property.
    :ivar idref: The value of the @id property of an
        <xccdf:Rule>. This <xccdf:rule-result> reflects the
        result of                     applying this <xccdf:Rule>
        to a target or target component.
    :ivar role: The value of the @role property of the referenced
        <xccdf:Rule>.
    :ivar severity: The value of the @severity property of the
        referenced <xccdf:Rule>.
    :ivar time: Time when application of this instance of the
        referenced <xccdf:Rule> was completed.
    :ivar version: The value of the @version property of the
        referenced <xccdf:Rule>.
    :ivar weight: The value of the @weight property of the referenced
        <xccdf:Rule>.
    """

    class Meta:
        name = "ruleResultType"

    result: Optional[ResultEnumType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    override: List[OverrideType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ident: List[IdentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    metadata: List[MetadataType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    message: List[MessageType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    instance: List[InstanceResultType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fix: List[FixType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    check: List[CheckType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    complex_check: Optional[ComplexCheckType] = field(
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
    role: Optional[RoleEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    severity: Optional[SeverityEnumType] = field(
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


# Tailoring-related types


@dataclass
class TailoringBenchmarkReferenceType(BenchmarkReferenceType):
    """Identifies the <xccdf:Benchmark> to which an.

    <xccdf:Tailoring> element applies.

    :ivar version: Identifies the version of the referenced
        <xccdf:Benchmark>.
    """

    class Meta:
        name = "tailoringBenchmarkReferenceType"

    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TailoringVersionType:
    """Type for version information about an.

    <xccdf:Tailoring> element.

    :ivar value:
    :ivar time: The time when this version of the
        <xccdf:Tailoring> document was completed.
    """

    class Meta:
        name = "tailoringVersionType"

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
