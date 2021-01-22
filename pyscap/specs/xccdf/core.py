from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from .base import ItemType, SelectableItemType
from .common import ProfileNoteType, TextType, IdrefType, Cpe2IdrefType, Status, VersionType, TextWithSubType, \
    HtmlTextWithSubType, OverrideableCpe2IdrefType, Model
from .components import SelStringType, SelComplexValueType, SelNumType, SelChoicesType, UriRefType, SignatureType, \
    IdentType, FixTextType, FixType, CheckType, BenchmarkReferenceType, TailoringReferenceType, IdentityType, \
    TargetFactsType, TargetIdRefType, ProfileSetValueType, ProfileSetComplexValueType, RuleResultType, ScoreType, \
    MetadataType, DcStatusType, ReferenceType, ProfileSelectType, ProfileRefineValueType, ProfileRefineRuleType, \
    TailoringBenchmarkReferenceType, TailoringVersionType, NoticeType, PlainTextType
from .enums import ValueTypeType, ValueOperatorType, InterfaceHintType, RoleEnumType, SeverityEnumType
from ..cpe import PlatformSpecification


@dataclass
class ValueType(ItemType):
    """
    Data type for the <xccdf:Value> element, which is a named parameter
    that can be substituted into properties of other elements within the
    <xccdf:Benchmark>, including the interior of structured check
    specifications and fix scripts.

    :ivar value: A simple (number, string, or
        boolean) value associated with this <xccdf:Value>. At any
        time an <xccdf:Value> has one active (simple or complex)
        value. If a selector value has been provided under
        <xccdf:Profile> selection or tailoring then the active
        <xccdf:value>/<xccdf:complex-value> is the one with
        a matching @selector. If there is no provided selector or if the
        provided selector does not match the @selector attribute of any
        <xccdf:value> or <xccdf:complex-value>, the active
        <xccdf:value>/<xccdf:complex-value> is the one with
        an empty or absent @selector or, failing that, the first
        <xccdf:value> or <xccdf:complex-value> in the XML.
        When an <xccdf:Value> is exported or used in text
        substitution, it is the currently active <xccdf:value> or
        <xccdf:complex-value> that is actually used. If there are
        multiple <xccdf:value> and/or <xccdf:complex-value>
        elements, only one may omit a @selector attribute and no two may
        have the same @selector value.
    :ivar complex_value: A complex (list) value associated
        with this <xccdf:Value>. See the description of the
        <xccdf:value> property for <xccdf:Rule> elements
        regarding activation of an <xccdf:complex-value>.
    :ivar default: The default value displayed to the
        user as a suggestion by benchmark producers during tailoring of
        this <xccdf:Value> element. (This is not the default value
        of an <xccdf:Value>; it is just the default display.) If
        there are multiple <xccdf:default> and/or
        <xccdf:complex-default> elements, only one may omit a
        @selector attribute and no two may have the same @selector
        value.
    :ivar complex_default: The default
        <xccdf:complex-value> displayed to the user as a
        suggestion by benchmark producers during tailoring of this
        <xccdf:Value> element. (This is not the default value of
        an <xccdf:Value>; it is just the default display.) If
        there are multiple <xccdf:default> and
        <xccdf:complex-default> elements, only one may omit a
        @selector attribute and no two may have the same @selector
        value.
    :ivar match: A Perl Compatible Regular Expression
        that a benchmark producer may apply during tailoring to validate
        a                                 user’s input for the
        <xccdf:Value>. It uses implicit
        anchoring. It applies only when the @type property is “string”
        or                                 “number” or a list of strings
        and/or numbers.
    :ivar lower_bound: Minimum legal value for this
        <xccdf:Value>. It is used to constrain value input during
        tailoring, when the @type property is “number”. Values supplied
        by                                 the user for tailoring the
        <xccdf:Benchmark> must be equal to
        or greater than this number.
    :ivar upper_bound: Maximum legal value for this
        <xccdf:Value>. It is used to constrain value input during
        tailoring, when the @type is “number”. Values supplied by the
        user                                 for tailoring the
        <xccdf:Benchmark> must be less than or equal
        to than this number.
    :ivar choices: A list of legal or suggested choices
        (values) for an <xccdf:Value> element, to be used during
        tailoring and document generation.
    :ivar source: URI indicating where the tool may
        acquire values, value bounds, or value choices for this
        <xccdf:Value> element. XCCDF does not attach any meaning
        to                                 the URI; it may be an
        arbitrary community or tool-specific value, or
        a pointer directly to a resource. If several instances of the
        <xccdf:source> property appear, then they represent
        alternative means or locations for obtaining the value in
        descending                                 order of preference
        (i.e., most preferred first).
    :ivar signature: A digital signature asserting
        authorship and allowing verification of the integrity of the
        <xccdf:Value>.
    :ivar id: The unique identifier for this element.
    :ivar type: The data type of the <xccdf:Value>. A
        tool may choose any convenient form to store an
        <xccdf:Value>                             element’s
        <xccdf:value> element, but the @type attribute conveys
        how the <xccdf:Value> should be treated for user input
        validation                             purposes during tailoring
        processing. The @type attribute may also be
        used to give additional guidance to the user or to validate the
        user’s                             input. In the case of a list
        of values, the @type attribute, if present,
        applies to all elements of the list individually.
    :ivar operator: The operator to be used for comparing this
        <xccdf:Value> to some part of the test system’s
        configuration                             during
        <xccdf:Rule> checking.
    :ivar interactive: Whether tailoring for this
        <xccdf:Value> should be performed during
        <xccdf:Benchmark>                             application.
        The benchmark consumer may ignore the attribute if asking
        the user is not feasible or not supported.
    :ivar interface_hint: A hint or recommendation to a benchmark
        consumer or producer about how the user might select or adjust
        the                             <xccdf:Value>.
    """

    class Meta:
        name = "valueType"

    value: List[SelStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    complex_value: List[SelComplexValueType] = field(
        default_factory=list,
        metadata={
            "name": "complex-value",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    default: List[SelStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    complex_default: List[SelComplexValueType] = field(
        default_factory=list,
        metadata={
            "name": "complex-default",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    match: List[SelStringType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    lower_bound: List[SelNumType] = field(
        default_factory=list,
        metadata={
            "name": "lower-bound",
            "type": "Element",
            "namespace": "",
        }
    )
    upper_bound: List[SelNumType] = field(
        default_factory=list,
        metadata={
            "name": "upper-bound",
            "type": "Element",
            "namespace": "",
        }
    )
    choices: List[SelChoicesType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    source: List[UriRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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
    type: ValueTypeType = field(
        default=ValueTypeType.STRING,
        metadata={
            "type": "Attribute",
        }
    )
    operator: ValueOperatorType = field(
        default=ValueOperatorType.EQUALS,
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
    interface_hint: Optional[InterfaceHintType] = field(
        default=None,
        metadata={
            "name": "interfaceHint",
            "type": "Attribute",
        }
    )


@dataclass
class Value(ValueType):
    """The <xccdf:Value> element is a named parameter that can be
    substituted into properties of other elements within the.

    <xccdf:Benchmark>, including the interior of structured check
    specifications and fix scripts.
    """

    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class RuleType(SelectableItemType):
    """
    Data type for the <xccdf:Rule> element that represents a specific
    <xccdf:Benchmark> test.

    :ivar ident: A globally meaningful identifier for
        this <xccdf:Rule>. This may be the name or identifier of a
        security configuration issue or vulnerability that the
        <xccdf:Rule> assesses.
    :ivar impact_metric: The potential impact of failure to
        conform to the <xccdf:Rule>, expressed as a CVSS 2.0 base
        vector.
    :ivar profile_note: Text that describes special aspects of
        the <xccdf:Rule> related to one or more
        <xccdf:Profile>                                 elements.
        This allows an author to document things within
        <xccdf:Rule> elements that are specific to a given
        <xccdf:Profile>, and then select the appropriate text
        based on                                 the selected
        <xccdf:Profile> and display it to the
        reader.
    :ivar fixtext: Data that describes how to bring a
        target system into compliance with this
        <xccdf:Rule>.
    :ivar fix: A command string, script, or other
        system modification statement that, if executed on the target
        system, can bring it into full, or at least better, compliance
        with                                 this <xccdf:Rule>.
    :ivar check: The definition of, or a reference
        to, the target system check needed to test compliance with this
        <xccdf:Rule>. Sibling <xccdf:check> elements must
        have different values for the combination of their @selector and
        @system attributes, and must have different values for their @id
        attribute (if any).
    :ivar complex_check: A boolean expression composed of
        operators (and, or, not) and individual
        checks.
    :ivar signature: A digital signature asserting
        authorship and allowing verification of the integrity of the
        <xccdf:Rule>.
    :ivar id: Unique element identifier used by other
        elements to refer to this element.
    :ivar role: The <xccdf:Rule> element’s role in
        scoring and reporting.
    :ivar severity: Severity level code to be used for metrics
        and tracking.
    :ivar multiple: Applicable in cases where there are
        multiple instances of a target. For example, an
        <xccdf:Rule> may                             provide a
        recommendation about the configuration of application user
        accounts, but an application may have many user accounts. Each
        account                             would be considered an
        instance of the broader assessment target of user
        accounts. If the @multiple attribute is set to true, each
        instance of                             the target to which the
        <xccdf:Rule> can apply should be tested
        separately and the results should be recorded separately. If
        @multiple                             is set to false, the test
        results of such instances should be combined.
        If the checking system does not combine these results
        automatically, the                             results of each
        instance should be ANDed together to produce a single
        result. If the benchmark consumer cannot perform multiple
        instantiation,                             or if multiple
        instantiation of the <xccdf:Rule> is not applicable
        for the target system, then the benchmark consumer may ignore
        this                             attribute.
    """

    class Meta:
        name = "ruleType"

    ident: List[IdentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    impact_metric: Optional[str] = field(
        default=None,
        metadata={
            "name": "impact-metric",
            "type": "Element",
            "namespace": "",
        }
    )
    profile_note: List[ProfileNoteType] = field(
        default_factory=list,
        metadata={
            "name": "profile-note",
            "type": "Element",
            "namespace": "",
        }
    )
    fixtext: List[FixTextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    fix: List[FixType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    check: List[CheckType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    complex_check: Optional[ComplexCheckType] = field(
        default=None,
        metadata={
            "name": "complex-check",
            "type": "Element",
            "namespace": "",
        }
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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
    role: RoleEnumType = field(
        default=RoleEnumType.FULL,
        metadata={
            "type": "Attribute",
        }
    )
    severity: SeverityEnumType = field(
        default=SeverityEnumType.UNKNOWN,
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
class Rule(RuleType):
    """The <xccdf:Rule> element contains the description for a single
    item of guidance or constraint. <xccdf:Rule> elements form the basis
    for testing a target platform for compliance with an.

    <xccdf:Benchmark>, for scoring, and for conveying descriptive
    prose, identifiers, references, and remediation information.
    """

    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class GroupType(SelectableItemType):
    """Data type for the <xccdf:Group> element. A.

    <xccdf:Group> element contains descriptive information about a
    portion of an <xccdf:Benchmark>, as well as
    <xccdf:Rule>, <xccdf:Value>, and/or other
    <xccdf:Group> elements

    :ivar value: <xccdf:Value> elements that
        belong to this <xccdf:Group>.
    :ivar group: Sub-<xccdf:Groups> under this
        <xccdf:Group>.
    :ivar rule: <xccdf:Rule> elements that
        belong to this <xccdf:Group>.
    :ivar signature: A digital signature asserting
        authorship and allowing verification of the integrity of the
        <xccdf:Group>.
    :ivar id: Unique element identifier; used by other
        elements to refer to this element.
    """

    class Meta:
        name = "groupType"

    value: List[Value] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://checklists.nist.gov/xccdf/1.2",
        }
    )
    group: List["Group"] = field(
        default_factory=list,
        metadata={
            "name": "Group",
            "type": "Element",
            "namespace": "http://checklists.nist.gov/xccdf/1.2",
            "sequential": True,
        }
    )
    rule: List[Rule] = field(
        default_factory=list,
        metadata={
            "name": "Rule",
            "type": "Element",
            "namespace": "http://checklists.nist.gov/xccdf/1.2",
            "sequential": True,
        }
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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
class Group(GroupType):
    """An item that can hold other items.

    It allows an author to collect related items into a common structure
    and provide descriptive text and references about them.
    """

    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class TestResultType:
    """Data type for the <xccdf:TestResult> element, which holds the
    results of one application of the <xccdf:Benchmark>. The.

    <xccdf:TestResult> element normally appears as the child of
    the <xccdf:Benchmark> element, although it may also appear as
    the top-level element of an XCCDF results document. XCCDF is not
    intended to be a database format for detailed results; the
    <xccdf:TestResult> element offers a way to store the results
    of individual tests in modest detail, with the ability to reference
    lower-level testing data. Although several of the child elements of
    this type technically support the @override attribute, the
    <xccdf:TestResult> element cannot be extended. Therefore,
    @override has no meaning within an <xccdf:TestResult> element
    and its children, and should not be used for them.

    :ivar benchmark: Reference to the <xccdf:Benchmark> for
        which the <xccdf:TestResult> records results. This
        property is                         required if this
        <xccdf:TestResult> element is the top-level element
        and optional otherwise.
    :ivar tailoring_file: The tailoring file element contains attributes
        used to identify an <xccdf:Tailoring> element used to
        guide the                         assessment reported on in this
        <xccdf:TestResult>. The tailoring
        element is required in an <xccdf:TestResult> if and only
        if an                         <xccdf:Tailoring> element
        guided the assessment recorded in the
        <xccdf:TestResult> or if the <xccdf:Tailoring>
        element records                         manual tailoring actions
        applied to this assessment.
    :ivar title: Title of the test.
    :ivar remark: A remark about the test, possibly supplied by
        the person administering the <xccdf:Benchmark>
        assessment
    :ivar organization: The name of the organization or other entity
        responsible for applying this <xccdf:Benchmark> and
        generating this                         result. When multiple
        <xccdf:organization> elements are used to
        indicate multiple organization names in a hierarchical
        organization, the                         highest-level
        organization should appear first.
    :ivar identity: Information about the system identity or user
        employed during application of the <xccdf:Benchmark>. If
        used,                         specifies the name of the
        authenticated identity.
    :ivar profile: The <xccdf:profile> element holds the
        value of the @id attribute value of the <xccdf:Profile>
        selected to be                         used in the assessment
        reported on by this <xccdf:TestResult>. This
        <xccdf:Profile> might be from the <xccdf:Benchmark>
        or from an                         <xccdf:Tailoring> file,
        if used. This element should appear if and
        only if an <xccdf:Profile> was selected to guide the
        assessment.
    :ivar target: Name or description of the target system whose
        test results are recorded in the <xccdf:TestResult>
        element (the                         system to which an
        <xccdf:Benchmark> test was applied). Each
        appearance of the element supplies a name by which the target
        host or device                         was identified at the
        time the test was run. The name may be any string, but
        applications should include the fully qualified DNS name
        whenever possible.
    :ivar target_address: Network address of the target system to which
        an <xccdf:Benchmark> test was applied. Typical forms for
        the address                         include IP version 4 (IPv4),
        IP version 6 (IPv6), and Ethernet media access
        control (MAC).
    :ivar target_facts: A list of named facts about the target system
        or platform.
    :ivar target_id_ref: References to external structures with
        identifying information about the target of this
        assessment.
    :ivar other_element: Identifying information expressed in other
        XML formats can be included here.
    :ivar platform: A platform on the target system. There should
        be one instance of this property for every platform that the
        target system                         was found to meet.
    :ivar set_value: Specific setting for a single
        <xccdf:Value> element used during the test.
    :ivar set_complex_value: Specific setting for a single
        <xccdf:Value> element used during the test when the given
        value is                             set to a complex type, such
        as a list.
    :ivar rule_result: The result of a single instance of an
        <xccdf:Rule> application against the target. The
        <xccdf:TestResult> must include at least one
        <xccdf:rule-result>                         record for
        each <xccdf:Rule> that was selected in the resolved
        <xccdf:Benchmark>.
    :ivar score: An overall score for this
        <xccdf:Benchmark> test.
    :ivar metadata: XML metadata associated with this
        <xccdf:TestResult>.
    :ivar signature: A digital signature asserting authorship and
        allowing verification of the integrity of the
        <xccdf:TestResult>.
    :ivar id: Unique identifier for this                     element.
    :ivar start_time: Time when testing began.
    :ivar end_time: Time when testing was completed and the results
        recorded.
    :ivar test_system: Name of the benchmark consumer program that
        generated this <xccdf:TestResult> element; should be
        either a CPE name or                     a CPE applicability
        language expression.
    :ivar version: The version number string copied from the
        <xccdf:Benchmark> used to direct this assessment.
    :ivar id_attribute: An identifier used for referencing elements
        included in an XML signature.
    """

    class Meta:
        name = "testResultType"

    benchmark: Optional[BenchmarkReferenceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    tailoring_file: Optional[TailoringReferenceType] = field(
        default=None,
        metadata={
            "name": "tailoring-file",
            "type": "Element",
            "namespace": "",
        }
    )
    title: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    remark: List[TextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    organization: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    identity: Optional[IdentityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    profile: Optional[IdrefType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    target: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    target_address: List[str] = field(
        default_factory=list,
        metadata={
            "name": "target-address",
            "type": "Element",
            "namespace": "",
        }
    )
    target_facts: Optional[TargetFactsType] = field(
        default=None,
        metadata={
            "name": "target-facts",
            "type": "Element",
            "namespace": "",
        }
    )
    target_id_ref: List[TargetIdRefType] = field(
        default_factory=list,
        metadata={
            "name": "target-id-ref",
            "type": "Element",
            "namespace": "",
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
    platform: List[Cpe2IdrefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    set_value: List[ProfileSetValueType] = field(
        default_factory=list,
        metadata={
            "name": "set-value",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    set_complex_value: List[ProfileSetComplexValueType] = field(
        default_factory=list,
        metadata={
            "name": "set-complex-value",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    rule_result: List[RuleResultType] = field(
        default_factory=list,
        metadata={
            "name": "rule-result",
            "type": "Element",
            "namespace": "",
        }
    )
    score: List[ScoreType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    metadata: List[MetadataType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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
class TestResult(TestResultType):
    """The <xccdf:TestResult> element encapsulates the results of a
    single application of an <xccdf:Benchmark> to a single target
    platform. The <xccdf:TestResult> element normally appears as the
    child of the.

    <xccdf:Benchmark> element, although it may also appear as the
    top-level element of an XCCDF results document. XCCDF is not
    intended to be a database format for detailed results; the
    <xccdf:TestResult> element offers a way to store the results
    of individual tests in modest detail, with the ability to reference
    lower-level testing data.
    """

    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class ProfileType:
    """Data type for the <xccdf:Profile> element, which holds a specific
    tailoring of the <xccdf:Benchmark>. The main part of an.

    <xccdf:Profile> is the selectors: <xccdf:select>,
    <xccdf:set-value>, <xccdf:set-complex-value>,
    <xccdf:refine-rule>, and <xccdf:refine-value>. An
    <xccdf:Profile> may also be signed with an XML-Signature.

    :ivar status: Status of the <xccdf:Profile> and date at
        which it attained that status. Authors may use this element to
        record the                         maturity or consensus level
        of an <xccdf:Profile>. If the
        <xccdf:status> is not given explicitly, then the
        <xccdf:Profile>                         is taken to have
        the same status as its parent
        <xccdf:Benchmark>.
    :ivar dc_status: Holds additional status information using the
        Dublin Core format.
    :ivar version: Version information about this
        <xccdf:Profile>.
    :ivar title: Title of the <xccdf:Profile>.
    :ivar description: Text that describes the <xccdf:Profile>.
    :ivar reference: A reference where the user can learn more about
        the subject of this <xccdf:Profile>.
    :ivar platform: A target platform for this
        <xccdf:Profile>.
    :ivar select: Select or deselect <xccdf:Group> and
        <xccdf:Rule> elements.
    :ivar set_complex_value: Set the value of an <xccdf:Value> to
        a list.
    :ivar set_value: Set the value of an <xccdf:Value> to
        a simple data value.
    :ivar refine_value: Customize the properties of an
        <xccdf:Value>.
    :ivar refine_rule: Customize the properties of an
        <xccdf:Rule> or <xccdf:Group>.
    :ivar metadata: Metadata associated with this
        <xccdf:Profile>.
    :ivar signature: A digital signature asserting authorship and
        allowing verification of the integrity of the
        <xccdf:Profile>.
    :ivar id: Unique identifier for this
        <xccdf:Profile>.
    :ivar prohibit_changes: Whether or not products should prohibit
        changes to                     this <xccdf:Profile>.
    :ivar abstract: If true, then this <xccdf:Profile> exists
        solely to be extended by other <xccdf:Profile> elements.
    :ivar note_tag: Tag identifier to specify which
        <xccdf:profile-note> element from an <xccdf:Rule>
        should be                     associated with this
        <xccdf:Profile>.
    :ivar extends: The id of an <xccdf:Profile> on which to base
        this <xccdf:Profile>.
    :ivar base:
    :ivar id_attribute: An identifier used for referencing elements
        included in an XML signature.
    """

    class Meta:
        name = "profileType"

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
            "min_occurs": 1,
        }
    )
    description: List[HtmlTextWithSubType] = field(
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
    platform: List[OverrideableCpe2IdrefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    select: List[ProfileSelectType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    set_complex_value: List[ProfileSetComplexValueType] = field(
        default_factory=list,
        metadata={
            "name": "set-complex-value",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    set_value: List[ProfileSetValueType] = field(
        default_factory=list,
        metadata={
            "name": "set-value",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    refine_value: List[ProfileRefineValueType] = field(
        default_factory=list,
        metadata={
            "name": "refine-value",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    refine_rule: List[ProfileRefineRuleType] = field(
        default_factory=list,
        metadata={
            "name": "refine-rule",
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    metadata: List[MetadataType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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
class Profile(ProfileType):
    """The <xccdf:Profile> element is a named tailoring for an
    <xccdf:Benchmark>.

    While an <xccdf:Benchmark> can be tailored in place by setting
    properties of various elements, <xccdf:Profile> elements allow
    one <xccdf:Benchmark> document to hold several independent
    tailorings.
    """

    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class TailoringType:
    """Data type for the <xccdf:Tailoring> element. The.

    <xccdf:Tailoring> element allows named tailorings (i.e.,
    <xccdf:Profile> elements) of an <xccdf:Benchmark> to be
    defined separately from the <xccdf:Benchmark> itself. The
    <xccdf:Profile> elements in an <xccdf:Tailoring> element
    can be used in two ways: First, an organization might wish to pre-
    define a set of tailoring actions to be applied on top of or instead
    of the tailoring performed by an <xccdf:Benchmark> element's
    <xccdf:Profile> elements. Second, an <xccdf:Tailoring>
    element can be used to record manual tailoring actions performed
    during the course of an assessment.

    :ivar benchmark: Identifies the <xccdf:Benchmark> to which
        this tailoring applies. A <xccdf:Tailoring> document is
        only                         applicable to a single
        <xccdf:Benchmark>. Note, however, that this is
        a purely informative field.
    :ivar status: Status of the tailoring and date at which it
        attained that status. Authors may use this element to record the
        maturity or                         consensus level of an
        <xccdf:Tailoring> element.
    :ivar dc_status: Holds additional status information using the
        Dublin Core format.
    :ivar version: The version of this <xccdf:Tailoring>
        element, with a required @time attribute that records when the
        <xccdf:Tailoring> element was created. This timestamp is
        necessary                         because, under some
        circumstances, a copy of an <xccdf:Tailoring>
        document might be automatically generated. Without the version
        and                         timestamp, tracking of these
        automatically created <xccdf:Tailoring>
        documents could become problematic.
    :ivar metadata: XML metadata for the <xccdf:Tailoring>
        element.
    :ivar profile: <xccdf:Profile> elements that reference
        and customize sets of items in an <xccdf:Benchmark>.
    :ivar signature: A digital signature asserting authorship and
        allowing verification of the integrity of the
        <xccdf:Tailoring>.
    :ivar id: Unique identifier for this                     element.
    :ivar id_attribute: An identifier used for referencing elements
        included in an XML signature.
    """

    class Meta:
        name = "tailoringType"

    benchmark: Optional[TailoringBenchmarkReferenceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
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
    version: Optional[TailoringVersionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    metadata: List[MetadataType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    profile: List[Profile] = field(
        default_factory=list,
        metadata={
            "name": "Profile",
            "type": "Element",
            "namespace": "http://checklists.nist.gov/xccdf/1.2",
            "min_occurs": 1,
        }
    )
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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
class Tailoring(TailoringType):
    """The <xccdf:Tailoring> element holds one or more.

    <xccdf:Profile> elements. These <xccdf:Profile> elements
    record additional tailoring activities that apply to a given
    <xccdf:Benchmark>. <xccdf:Tailoring> elements are
    separate from <xccdf:Benchmark> documents, but each
    <xccdf:Tailoring> element is associated with a specific
    <xccdf:Benchmark> document. By defining these tailoring
    actions separately from the <xccdf:Benchmark> document to
    which they apply, these actions can be recorded without affecting
    the integrity of the source itself.
    """

    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class Benchmark:
    """This is the root element of the XCCDF document; it must appear exactly
    once. It encloses the entire benchmark, and contains both descriptive
    information and structural information. Note that the order of.

    <xccdf:Group> and <xccdf:Rule> child elements may matter
    for the appearance of a generated document. <xccdf:Group> and
    <xccdf:Rule> children may be freely intermingled, but they
    must appear after any <xccdf:Value> children. All the other
    children must appear in the order shown.

    :ivar status: Status of the <xccdf:Benchmark>
        indicating its level of maturity or consensus. If more than one
        <xccdf:status> element appears, the element's @date
        attribute                             should be included.
    :ivar dc_status: Holds additional status information using
        the Dublin Core format.
    :ivar title: Title of the <xccdf:Benchmark>; an
        <xccdf:Benchmark> should have an
        <xccdf:title>.
    :ivar description: Text that describes the
        <xccdf:Benchmark>; an <xccdf:Benchmark> should have
        an                             <xccdf:description>.
    :ivar notice: Legal notices (licensing information, terms
        of use, etc.), copyright statements, warnings, and other
        advisory                             notices about this
        <xccdf:Benchmark> and its                             use.
    :ivar front_matter: Introductory matter for the beginning of
        the <xccdf:Benchmark> document; intended for use during
        Document                             Generation.
    :ivar rear_matter: Concluding material for the end of the
        <xccdf:Benchmark> document; intended for use during
        Document                             Generation.
    :ivar reference: Supporting references for the
        <xccdf:Benchmark> document.
    :ivar plain_text: Definitions for reusable text blocks, each
        with a unique identifier.
    :ivar platform_specification: A list of identifiers for complex
        platform                             definitions, written in CPE
        applicability language format. Authors may
        define complex platforms within this element, and then use their
        locally                             unique identifiers anywhere
        in the <xccdf:Benchmark> element in
        place of a CPE name.
    :ivar platform: Applicable platforms for this
        <xccdf:Benchmark>. Authors should use the element to
        identify the                             systems or products to
        which the <xccdf:Benchmark>
        applies.
    :ivar version: Version number of the
        <xccdf:Benchmark>.
    :ivar metadata: XML metadata for the
        <xccdf:Benchmark>. Metadata allows many additional pieces
        of                             information, including
        authorship, publisher, support, and other similar
        details, to be embedded in an
        <xccdf:Benchmark>.
    :ivar model: URIs of suggested scoring models to be used
        when computing a score for this <xccdf:Benchmark>. A
        suggested                             list of scoring models and
        their URIs is provided in the XCCDF
        specification.
    :ivar profile: <xccdf:Profile> elements that
        reference and customize sets of items in the
        <xccdf:Benchmark>.
    :ivar value: Parameter <xccdf:Value> elements that
        support <xccdf:Rule> elements and descriptions in the
        <xccdf:Benchmark>.
    :ivar group: <xccdf:Group> elements that
        comprise the <xccdf:Benchmark>; each may contain
        additional                                 <xccdf:Value>,
        <xccdf:Rule>, and other
        <xccdf:Group> elements.
    :ivar rule: <xccdf:Rule> elements that
        comprise the <xccdf:Benchmark>.
    :ivar test_result: <xccdf:Benchmark> test result records
        (one per <xccdf:Benchmark> run).
    :ivar signature: A digital signature asserting authorship
        and allowing verification of the integrity of the
        <xccdf:Benchmark>.
    :ivar id: Unique <xccdf:Benchmark>
        identifier.
    :ivar id_attribute: An identifier used for referencing elements
        included in an XML signature.
    :ivar resolved: True if <xccdf:Benchmark> has already
        undergone the resolution process.
    :ivar style: Name of an <xccdf:Benchmark> authoring
        style or set of conventions or constraints to which this
        <xccdf:Benchmark> conforms (e.g., “SCAP 1.2”).
    :ivar style_href: URL of a supplementary stylesheet or schema
        extension that can be used to verify conformance to the named
        style.
    :ivar lang:
    """

    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    status: List[Status] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
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
    title: List[TextType] = field(
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
    notice: List[NoticeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    front_matter: List[HtmlTextWithSubType] = field(
        default_factory=list,
        metadata={
            "name": "front-matter",
            "type": "Element",
            "namespace": "",
        }
    )
    rear_matter: List[HtmlTextWithSubType] = field(
        default_factory=list,
        metadata={
            "name": "rear-matter",
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
    plain_text: List[PlainTextType] = field(
        default_factory=list,
        metadata={
            "name": "plain-text",
            "type": "Element",
            "namespace": "",
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
    platform: List[Cpe2IdrefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    version: Optional[VersionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    metadata: List[MetadataType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
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
    signature: Optional[SignatureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
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
