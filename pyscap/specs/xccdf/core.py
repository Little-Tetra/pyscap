from .base import *


# Value element

class ValueType(ItemType):
    """
    Data type for the <xccdf:Value> element, which is a named parameter that can be substituted into properties of
    other elements within the <xccdf:Benchmark>, including the interior of structured check specifications and fix
    scripts.
    """

    def __init__(
            self,
            id_: ValueIdType,
            value: SelStringType = None,
            complex_value: SelComplexValueType = None,
            default: SelStringType = None,
            complex_default: SelComplexValueType = None,
            match: list[SelStringType] = None,
            lower_bound: list[SelNumType] = None,
            upper_bound: list[SelNumType] = None,
            choices: list[SelChoicesType] = None,
            source: list[UriRefType] = None,
            signature: SignatureType = None,
            type_: ValueTypeType = ValueTypeType.string,
            operator: ValueOperatorType = ValueOperatorType.equals,
            interactive: bool = False,
            interface_hint: InterfaceHintType = None,
            **kwargs
    ):
        """

        :param id_: The unique identifier for this element.
        :param value: A simple (number, string, or boolean) value associated with this <xccdf:Value>. At any time an <xccdf:Value> has one active (simple or complex) value. If a selector value has been provided under <xccdf:Profile> selection or tailoring then the active <xccdf:value>/<xccdf:complex-value> is the one with a matching @selector. If there is no provided selector or if the provided selector does not match the @selector attribute of any <xccdf:value> or <xccdf:complex-value>, the active <xccdf:value>/<xccdf:complex-value> is the one with an empty or absent @selector or, failing that, the first <xccdf:value> or <xccdf:complex-value> in the XML. When an <xccdf:Value> is exported or used in text substitution, it is the currently active <xccdf:value> or <xccdf:complex-value> that is actually used. If there are multiple <xccdf:value> and/or <xccdf:complex-value> elements, only one may omit a @selector attribute and no two may have the same @selector value.
        :param complex_value: A complex (list) value associated with this <xccdf:Value>. See the description of the <xccdf:value> property for <xccdf:Rule> elements regarding activation of an <xccdf:complex-value>.
        :param default: The default value displayed to the user as a suggestion by benchmark producers during tailoring of this <xccdf:Value> element. (This is not the default value of an <xccdf:Value>; it is just the default display.) If there are multiple <xccdf:default> and/or <xccdf:complex-default> elements, only one may omit a @selector attribute and no two may have the same @selector value.
        :param complex_default: The default <xccdf:complex-value> displayed to the user as a suggestion by benchmark producers during tailoring of this <xccdf:Value> element. (This is not the default value of an <xccdf:Value>; it is just the default display.) If there are multiple <xccdf:default> and <xccdf:complex-default> elements, only one may omit a @selector attribute and no two may have the same @selector value.
        :param match: A Perl Compatible Regular Expression that a benchmark producer may apply during tailoring to validate a user’s input for the <xccdf:Value>. It uses implicit anchoring. It applies only when the @type property is “string” or “number” or a list of strings and/or numbers.
        :param lower_bound: Minimum legal value for this <xccdf:Value>. It is used to constrain value input during tailoring, when the @type property is “number”. Values supplied by the user for tailoring the <xccdf:Benchmark> must be equal to or greater than this number.
        :param upper_bound: Maximum legal value for this <xccdf:Value>. It is used to constrain value input during tailoring, when the @type is “number”. Values supplied by the user for tailoring the <xccdf:Benchmark> must be less than or equal to than this number.
        :param choices: A list of legal or suggested choices (values) for an <xccdf:Value> element, to be used during tailoring and document generation.
        :param source: URI indicating where the tool may acquire values, value bounds, or value choices for this <xccdf:Value> element. XCCDF does not attach any meaning to the URI; it may be an arbitrary community or tool-specific value, or a pointer directly to a resource. If several instances of the <xccdf:source> property appear, then they represent alternative means or locations for obtaining the value in descending order of preference (i.e., most preferred first).
        :param signature: A digital signature asserting authorship and allowing verification of the integrity of the <xccdf:Value>.
        :param type_: The data type of the <xccdf:Value>. A tool may choose any convenient form to store an <xccdf:Value> element’s <xccdf:value> element, but the @type attribute conveys how the <xccdf:Value> should be treated for user input validation purposes during tailoring processing. The @type attribute may also be used to give additional guidance to the user or to validate the user’s input. In the case of a list of values, the @type attribute, if present, applies to all elements of the list individually.
        :param operator: The operator to be used for comparing this <xccdf:Value> to some part of the test system’s configuration during <xccdf:Rule> checking.
        :param interactive: Whether tailoring for this <xccdf:Value> should be performed during <xccdf:Benchmark> application. The benchmark consumer may ignore the attribute if asking the user is not feasible or not supported.
        :param interface_hint: A hint or recommendation to a benchmark consumer or producer about how the user might select or adjust the <xccdf:Value>.
        """
        super().__init__(**kwargs)
        if match is None:
            match = []
        if lower_bound is None:
            lower_bound = []
        if upper_bound is None:
            upper_bound = []
        if choices is None:
            choices = []
        if source is None:
            source = []

        self.id_ = id_
        self.value = value
        self.complex_value = complex_value
        self.default = default
        self.complex_default = complex_default
        self.match = match
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.choices = choices
        self.source = source
        self.signature = signature
        self.type_ = type_
        self.operator = operator
        self.interactive = interactive
        self.interface_hint = interface_hint


class Value(ValueType):
    """
    The <xccdf:Value> element is a named parameter that can be substituted into properties of other elements within
    the <xccdf:Benchmark>, including the interior of structured check specifications and fix scripts.
    """


# Rule element

class RuleType(SelectableItemType):
    """
    Data type for the <xccdf:Rule> element that represents a specific <xccdf:Benchmark> test.
    """

    def __init__(
            self,
            id_: RuleIdType,
            ident: list[IdentType] = None,
            impact_metric: str = None,
            profile_note: list[ProfileNoteType] = None,
            fixtext: list[FixTextType] = None,
            fix: list[FixType] = None,
            check: list[CheckType] = None,
            complex_check: ComplexCheckType = None,
            signature: SignatureType = None,
            role: RoleEnumType = RoleEnumType.full,
            severity: SeverityEnumType = SeverityEnumType.unknown,
            multiple: bool = False,
            **kwargs
    ):
        """

        :param id_: Unique element identifier used by other elements to refer to this element.
        :param ident: A globally meaningful identifier for this <xccdf:Rule>. This may be the name or identifier of a security configuration issue or vulnerability that the <xccdf:Rule> assesses.
        :param impact_metric: The potential impact of failure to conform to the <xccdf:Rule>, expressed as a CVSS 2.0 base vector.
        :param profile_note: Text that describes special aspects of the <xccdf:Rule> related to one or more <xccdf:Profile> elements. This allows an author to document things within <xccdf:Rule> elements that are specific to a given <xccdf:Profile>, and then select the appropriate text based on the selected <xccdf:Profile> and display it to the reader.
        :param fixtext: Data that describes how to bring a target system into compliance with this <xccdf:Rule>.
        :param fix: A command string, script, or other system modification statement that, if executed on the target system, can bring it into full, or at least better, compliance with this <xccdf:Rule>.
        :param check: The definition of, or a reference to, the target system check needed to test compliance with this <xccdf:Rule>. Sibling <xccdf:check> elements must have different values for the combination of their @selector and @system attributes, and must have different values for their @id attribute (if any).
        :param complex_check: A boolean expression composed of operators (and, or, not) and individual checks.
        :param signature: A digital signature asserting authorship and allowing verification of the integrity of the <xccdf:Rule>.
        :param role: The <xccdf:Rule> element’s role in scoring and reporting.
        :param severity: Severity level code to be used for metrics and tracking.
        :param multiple: Applicable in cases where there are multiple instances of a target. For example, an <xccdf:Rule> may provide a recommendation about the configuration of application user accounts, but an application may have many user accounts. Each account would be considered an instance of the broader assessment target of user accounts. If the @multiple attribute is set to true, each instance of the target to which the <xccdf:Rule> can apply should be tested separately and the results should be recorded separately. If @multiple is set to false, the test results of such instances should be combined. If the checking system does not combine these results automatically, the results of each instance should be ANDed together to produce a single result. If the benchmark consumer cannot perform multiple instantiation, or if multiple instantiation of the <xccdf:Rule> is not applicable for the target system, then the benchmark consumer may ignore this attribute.
        """
        super().__init__(**kwargs)
        if ident is None:
            ident = []
        if profile_note is None:
            profile_note = []
        if fixtext is None:
            fixtext = []
        if fix is None:
            fix = []
        if check is None:
            check = []
        self.id_ = id_
        self.ident = ident
        self.impact_metric = impact_metric
        self.profile_note = profile_note
        self.fixtext = fixtext
        self.fix = fix
        self.check = check
        self.complex_check = complex_check
        self.signature = signature
        self.role = role
        self.severity = severity
        self.multiple = multiple


class Rule(RuleType):
    """
    The <xccdf:Rule> element contains the description for a single item of guidance or constraint. <xccdf:Rule>
    elements form the basis for testing a target platform for compliance with an <xccdf:Benchmark>, for scoring,
    and for conveying descriptive prose, identifiers, references, and remediation information.
    """


# Group element

class GroupType(SelectableItemType):
    """
    Data type for the <xccdf:Group> element. A <xccdf:Group> element contains descriptive information about a portion
    of an <xccdf:Benchmark>, as well as <xccdf:Rule>, <xccdf:Value>, and/or other <xccdf:Group> elements
    """

    def __init__(
            self,
            id_: GroupIdType,
            value: list[Value] = None,
            group: list[Group] = None,
            rule: list[Rule] = None,
            signature: SignatureType = None,
            **kwargs
    ):
        """

        :param id_: Unique element identifier; used by other elements to refer to this element.
        :param value: <xccdf:Value> elements that belong to this <xccdf:Group>.
        :param group: Sub-<xccdf:Groups> under this <xccdf:Group>.
        :param rule: <xccdf:Rule> elements that belong to this <xccdf:Group>.
        :param signature: A digital signature asserting authorship and allowing verification of the integrity of the <xccdf:Group>.
        """
        super().__init__(**kwargs)
        if value is None:
            value = []
        if group is None:
            group = []
        if rule is None:
            rule = []

        self.id_ = id_
        self.value = value
        self.group = group
        self.rule = rule
        self.signature = signature


class Group(GroupType):
    """
    An item that can hold other items. It allows an author to collect related items into a common structure and
    provide descriptive text and references about them.
    """


# Profile element

class ProfileType:
    """
    Data type for the <xccdf:Profile> element, which holds a specific tailoring of the <xccdf:Benchmark>. The main
    part of an <xccdf:Profile> is the selectors: <xccdf:select>, <xccdf:set-value>, <xccdf:set-complex-value>,
    <xccdf:refine-rule>, and <xccdf:refine-value>. An <xccdf:Profile> may also be signed with an XML-Signature.
    """

    def __init__(
            self,
            id_: ProfileIdType,
            title: list[TextWithSubType],
            status: list[Status] = None,
            dc_status: list[DcStatusType] = None,
            version: VersionType = None,
            description: list[HtmlTextWithSubType] = None,
            reference: list[ReferenceType] = None,
            platform: list[OverrideableCPE2idrefType] = None,
            select: list[ProfileSelectType] = None,
            set_complex_value: list[ProfileSetComplexValueType] = None,
            set_value: list[ProfileSetValueType] = None,
            refine_value: list[ProfileRefineValueType] = None,
            refine_rule: list[ProfileRefineRuleType] = None,
            metadata: list[MetadataType] = None,
            signature: SignatureType = None,
            prohibit_changes: bool = False,
            abstract: bool = False,
            note_tag: str = None,
            extends: str = None,
            base: str = None,
            xml_id: str = None
    ):
        """

        :param id_: Unique identifier for this <xccdf:Profile>.
        :param title: Title of the <xccdf:Profile>.
        :param status: Status of the <xccdf:Profile> and date at which it attained that status. Authors may use this element to record the maturity or consensus level of an <xccdf:Profile>. If the <xccdf:status> is not given explicitly, then the <xccdf:Profile> is taken to have the same status as its parent <xccdf:Benchmark>.
        :param dc_status: Holds additional status information using the Dublin Core format.
        :param version: Version information about this <xccdf:Profile>.
        :param description: Text that describes the <xccdf:Profile>.
        :param reference: A reference where the user can learn more about the subject of this <xccdf:Profile>.
        :param platform: A target platform for this <xccdf:Profile>.
        :param select: Select or deselect <xccdf:Group> and <xccdf:Rule> elements.
        :param set_complex_value: Set the value of an <xccdf:Value> to a list.
        :param set_value: Set the value of an <xccdf:Value> to a simple data value.
        :param refine_value: Customize the properties of an <xccdf:Value>.
        :param refine_rule: Customize the properties of an <xccdf:Rule> or <xccdf:Group>.
        :param metadata: Metadata associated with this <xccdf:Profile>.
        :param signature: A digital signature asserting authorship and allowing verification of the integrity of the <xccdf:Profile>.
        :param prohibit_changes: Whether or not products should prohibit changes to this <xccdf:Profile>.
        :param abstract: If true, then this <xccdf:Profile> exists solely to be extended by other <xccdf:Profile> elements.
        :param note_tag: Tag identifier to specify which <xccdf:profile-note> element from an <xccdf:Rule> should be associated with this <xccdf:Profile>.
        :param extends: The id of an <xccdf:Profile> on which to base this <xccdf:Profile>.
        :param base:
        :param xml_id: An identifier used for referencing elements included in an XML signature.
        """
        if status is None:
            status = []
        if dc_status is None:
            dc_status = []
        if description is None:
            description = []
        if reference is None:
            reference = []
        if platform is None:
            platform = []
        if select is None:
            select = []
        if set_complex_value is None:
            set_complex_value = []
        if set_value is None:
            set_value = []
        if refine_value is None:
            refine_value = []
        if refine_rule is None:
            refine_rule = []
        if metadata is None:
            metadata = []
        self.id_ = id_
        self.title = title
        self.status = status
        self.dc_status = dc_status
        self.version = version
        self.description = description
        self.reference = reference
        self.platform = platform
        self.select = select
        self.set_complex_value = set_complex_value
        self.set_value = set_value
        self.refine_value = refine_value
        self.refine_rule = refine_rule
        self.metadata = metadata
        self.signature = signature
        self.prohibit_changes = prohibit_changes
        self.abstract = abstract
        self.note_tag = note_tag
        self.extends = extends
        self.base = base
        self.xml_id = xml_id


class Profile(ProfileType):
    """
    The <xccdf:Profile> element is a named tailoring for an <xccdf:Benchmark>. While an <xccdf:Benchmark> can be
    tailored in place by setting properties of various elements, <xccdf:Profile> elements allow one <xccdf:Benchmark>
    document to hold several independent tailorings.
    """


# TestResult element

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

    def __init__(
            self,
            target: list[str],
            score: list[ScoreType],
            id_: TestResultIdType,
            end_time: datetime.datetime,
            benchmark: BenchmarkReferenceType = None,
            tailoring_file: TailoringReferenceType = None,
            title: list[TextType] = None,
            remark: list[TextType] = None,
            organization: list[str] = None,
            identity: IdentityType = None,
            profile: IdrefType = None,
            target_address: list[str] = None,
            target_facts: TargetFactsType = None,
            target_id_ref: list[TargetIdRefType] = None,
            other: list = None,
            platform: list[CPE2idrefType] = None,
            set_value: ProfileSetValueType = None,
            set_complex_value: ProfileSetComplexValueType = None,
            rule_result: list[RuleResultType] = None,
            metadata: list[MetadataType] = None,
            signature: SignatureType = None,
            start_time: datetime.datetime = None,
            test_system: str = None,
            version: str = None,
            xml_id: str = None
    ):
        """

        :param target: Name or description of the target system whose test results are recorded in the <xccdf:TestResult> element (the system to which an <xccdf:Benchmark> test was applied). Each appearance of the element supplies a name by which the target host or device was identified at the time the test was run. The name may be any string, but applications should include the fully qualified DNS name whenever possible.
        :param score: An overall score for this <xccdf:Benchmark> test.
        :param id_: Unique identifier for this element.
        :param end_time: Time when testing was completed and the results recorded.
        :param benchmark: Reference to the <xccdf:Benchmark> for which the <xccdf:TestResult> records results. This property is required if this <xccdf:TestResult> element is the top-level element and optional otherwise.
        :param tailoring_file: The tailoring file element contains attributes used to identify an <xccdf:Tailoring> element used to guide the assessment reported on in this <xccdf:TestResult>. The tailoring element is required in an <xccdf:TestResult> if and only if an <xccdf:Tailoring> element guided the assessment recorded in the <xccdf:TestResult> or if the <xccdf:Tailoring> element records manual tailoring actions applied to this assessment.
        :param title: Title of the test.
        :param remark: A remark about the test, possibly supplied by the person administering the <xccdf:Benchmark> assessment
        :param organization: The name of the organization or other entity responsible for applying this <xccdf:Benchmark> and generating this result. When multiple <xccdf:organization> elements are used to indicate multiple organization names in a hierarchical organization, the highest-level organization should appear first.
        :param identity: Information about the system identity or user employed during application of the <xccdf:Benchmark>. If used, specifies the name of the authenticated identity.
        :param profile: The <xccdf:profile> element holds the value of the @id attribute value of the <xccdf:Profile> selected to be used in the assessment reported on by this <xccdf:TestResult>. This <xccdf:Profile> might be from the <xccdf:Benchmark> or from an <xccdf:Tailoring> file, if used. This element should appear if and only if an <xccdf:Profile> was selected to guide the assessment.
        :param target_address: Network address of the target system to which an <xccdf:Benchmark> test was applied. Typical forms for the address include IP version 4 (IPv4), IP version 6 (IPv6), and Ethernet media access control (MAC).
        :param target_facts: A list of named facts about the target system or platform.
        :param target_id_ref: References to external structures with identifying information about the target of this assessment.
        :param other: Identifying information expressed in other XML formats can be included here.
        :param platform: A platform on the target system. There should be one instance of this property for every platform that the target system was found to meet.
        :param set_value: Specific setting for a single <xccdf:Value> element used during the test.
        :param set_complex_value: Specific setting for a single <xccdf:Value> element used during the test when the given value is set to a complex type, such as a list.
        :param rule_result: The result of a single instance of an <xccdf:Rule> application against the target. The <xccdf:TestResult> must include at least one <xccdf:rule-result> record for each <xccdf:Rule> that was selected in the resolved <xccdf:Benchmark>.
        :param metadata: XML metadata associated with this <xccdf:TestResult>.
        :param signature: A digital signature asserting authorship and allowing verification of the integrity of the <xccdf:TestResult>.
        :param start_time: Time when testing began.
        :param test_system: Name of the benchmark consumer program that generated this <xccdf:TestResult> element; should be either a CPE name or a CPE applicability language expression.
        :param version: The version number string copied from the <xccdf:Benchmark> used to direct this assessment.
        :param xml_id: An identifier used for referencing elements included in an XML signature.
        """
        if title is None:
            title = []
        if remark is None:
            remark = []
        if organization is None:
            organization = []
        if target_address is None:
            target_address = []
        if target_id_ref is None:
            target_id_ref = []
        if other is None:
            other = []
        if platform is None:
            platform = []
        if rule_result is None:
            rule_result = []
        if metadata is None:
            metadata = []
        self.target = target
        self.score = score
        self.id_ = id_
        self.end_time = end_time
        self.benchmark = benchmark
        self.tailoring_file = tailoring_file
        self.title = title
        self.remark = remark
        self.organization = organization
        self.identity = identity
        self.profile = profile
        self.target_address = target_address
        self.target_facts = target_facts
        self.target_id_ref = target_id_ref
        self.other = other
        self.platform = platform
        self.set_value = set_value
        self.set_complex_value = set_complex_value
        self.rule_result = rule_result
        self.metadata = metadata
        self.signature = signature
        self.start_time = start_time
        self.test_system = test_system
        self.version = version
        self.xml_id = xml_id


class TestResult(TestResultType):
    """
    The <xccdf:TestResult> element encapsulates the results of a single application of an <xccdf:Benchmark> to a
    single target platform. The <xccdf:TestResult> element normally appears as the child of the <xccdf:Benchmark>
    element, although it may also appear as the top-level element of an XCCDF results document. XCCDF is not intended
    to be a database format for detailed results; the <xccdf:TestResult> element offers a way to store the results of
    individual tests in modest detail, with the ability to reference lower-level testing data.
    """


#  Tailoring element

class TailoringType:
    """
    Data type for the <xccdf:Tailoring> element. The <xccdf:Tailoring> element allows named tailorings (i.e.,
    <xccdf:Profile> elements) of an <xccdf:Benchmark> to be defined separately from the <xccdf:Benchmark> itself. The
    <xccdf:Profile> elements in an <xccdf:Tailoring> element can be used in two ways: First, an organization might
    wish to pre-define a set of tailoring actions to be applied on top of or instead of the tailoring performed by an
    <xccdf:Benchmark> element's <xccdf:Profile> elements. Second, an <xccdf:Tailoring> element can be used to record
    manual tailoring actions performed during the course of an assessment.
    """

    def __init__(
            self,
            profile: list[Profile],
            id_: TailoringIdType,
            version: TailoringVersionType,
            benchmark: TailoringBenchmarkReferenceType = None,
            status: list[Status] = None,
            dc_status: list[DcStatusType] = None,
            metadata: list[MetadataType] = None,
            signature: SignatureType = None,
            xml_id: str = None
    ):
        """

        :param profile: <xccdf:Profile> elements that reference and customize sets of items in an <xccdf:Benchmark>.
        :param id_: Unique identifier for this element.
        :param version: The version of this <xccdf:Tailoring> element, with a required @time attribute that records when the <xccdf:Tailoring> element was created. This timestamp is necessary because, under some circumstances, a copy of an <xccdf:Tailoring> document might be automatically generated. Without the version and timestamp, tracking of these automatically created <xccdf:Tailoring> documents could become problematic.
        :param benchmark: Identifies the <xccdf:Benchmark> to which this tailoring applies. A <xccdf:Tailoring> document is only applicable to a single <xccdf:Benchmark>. Note, however, that this is a purely informative field.
        :param status: Status of the tailoring and date at which it attained that status. Authors may use this element to record the maturity or consensus level of an <xccdf:Tailoring> element.
        :param dc_status: Holds additional status information using the Dublin Core format.
        :param metadata: XML metadata for the <xccdf:Tailoring> element.
        :param signature: A digital signature asserting authorship and allowing verification of the integrity of the <xccdf:Tailoring>.
        :param xml_id: An identifier used for referencing elements included in an XML signature.
        """
        if status is None:
            status = []
        if dc_status is None:
            dc_status = []
        if metadata is None:
            metadata = []
        self.profile = profile
        self.id_ = id_
        self.version = version
        self.benchmark = benchmark
        self.status = status
        self.dc_status = dc_status
        self.metadata = metadata
        self.signature = signature
        self.xml_id = xml_id


class Tailoring(TailoringType):
    """
    The <xccdf:Tailoring> element holds one or more <xccdf:Profile> elements. These <xccdf:Profile> elements record
    additional tailoring activities that apply to a given <xccdf:Benchmark>. <xccdf:Tailoring> elements are separate
    from <xccdf:Benchmark> documents, but each <xccdf:Tailoring> element is associated with a specific
    <xccdf:Benchmark> document. By defining these tailoring actions separately from the <xccdf:Benchmark> document to
    which they apply, these actions can be recorded without affecting the integrity of the source itself.
    """


# Benchmark element

class Benchmark:
    """
    This is the root element of the XCCDF document; it must appear exactly once. It encloses the entire benchmark,
    and contains both descriptive information and structural information. Note that the order of <xccdf:Group> and
    <xccdf:Rule> child elements may matter for the appearance of a generated document. <xccdf:Group> and <xccdf:Rule>
    children may be freely intermingled, but they must appear after any <xccdf:Value> children. All the other
    children must appear in the order shown.
    """

    def __init__(
            self,
            id_: BenchmarkIdType,
            status: list[Status],
            dc_status: list[DcStatusType] = None,
            title: list[TextType] = None,
            description: list[HtmlTextWithSubType] = None,
            notice: list[NoticeType] = None,
            front_matter: list[HtmlTextWithSubType] = None,
            rear_matter: list[HtmlTextWithSubType] = None,
            reference: list[ReferenceType] = None,
            plain_text: list[PlainTextType] = None,
            platform_specification: PlatformSpecification = None,
            platform: list[CPE2idrefType] = None,
            version: VersionType = None,
            metadata: list[MetadataType] = None,
            model: list[Model] = None,
            profile: list[Profile] = None,
            value: list[Value] = None,
            group: list[Group] = None,
            rule: list[Rule] = None,
            test_result: list[TestResult] = None,
            signature: SignatureType = None,
            xml_id: str = None,
            resolved: bool = False,
            style: str = None,
            style_href: str = None,
            lang: str = None
    ):
        if dc_status is None:
            dc_status = []
        if title is None:
            title = []
        if description is None:
            description = []
        if notice is None:
            notice = []
        if front_matter is None:
            front_matter = []
        if rear_matter is None:
            rear_matter = []
        if reference is None:
            reference = []
        if plain_text is None:
            plain_text = []
        if platform is None:
            platform = []
        if metadata is None:
            metadata = []
        if model is None:
            model = []
        if profile is None:
            profile = []
        if value is None:
            value = []
        if group is None:
            group = []
        if rule is None:
            rule = []
        if test_result is None:
            test_result = []

        self.id_ = id_
        self.status = status
        self.dc_status = dc_status
        self.title = title
        self.description = description
        self.notice = notice
        self.front_matter = front_matter
        self.rear_matter = rear_matter
        self.reference = reference
        self.plain_text = plain_text
        self.platform_specification = platform_specification
        self.platform = platform
        self.version = version
        self.metadata = metadata
        self.model = model
        self.profile = profile
        self.value = value
        self.group = group
        self.rule = rule
        self.test_result = test_result
        self.signature = signature
        self.xml_id = xml_id
        self.resolved = resolved
        self.style = style
        self.style_href = style_href
        self.lang = lang


# Xccdf

class Xccdf:
    def __init__(self, file_path=None):
        self.benchmark = None
        if file_path is not None:
            self.load(file_path)

    def load(self, file_path):
        pass

    def dump(self, file_path):
        pass
