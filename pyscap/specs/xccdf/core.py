from .common import *


# Rule-related types


class WarningCategoryEnumType(Enum):
    """
    Allowed warning category keywords for the <xccdf:warning> element used in <xccdf:Rule> elements.
    """
    general = "general"  # Broad or general-purpose warning (default)
    functionality = "functionality"  # Warning about possible impacts to functionality or operational features
    performance = "performance"  # Warning about changes to target system performance or throughput
    hardware = "hardware"  # Warning about hardware restrictions or possible impacts to hardware
    legal = "legal"  # Warning about legal implications
    regulatory = "regulatory"  # Warning about regulatory obligations or compliance implications
    management = "management"  # Warning about impacts to the management or administration of the target system
    audit = "audit"  # Warning about impacts to audit or logging
    dependency = "dependency"  # Warning about dependencies between this element and other parts of the target system, or version dependencies


class FixStrategyEnumType(Enum):
    """
    Allowed @strategy keyword values for an <xccdf:Rule> element's <xccdf:fix> or <xccdf:fixtext> elements. The
    values indicate the method or approach for fixing non-compliance with a particular <xccdf:Rule>.
    """
    unknown = "unknown"  # Strategy not defined (default)
    configure = "configure"  # Adjust target configuration/settings
    combination = "combination"  # Combination of two or more approaches
    disable = "disable"  # Turn off or uninstall a target component
    enable = "enable"  # Turn on or install a target component
    patch = "patch"  # Apply a patch, hotfix, update, etc.
    policy = "policy"  # Remediation requires out-of-band adjustments to policies or procedures
    restrict = "restrict"  # Adjust permissions, access rights, filters, or other access restrictions
    update = "update"  # Install, upgrade or update the system


class RatingEnumType(Enum):
    """
    This type enumerates allowed rating values the disruption and complexity properties of an <xccdf:Rule> element's
    <xccdf:fix> or <xccdf:fixtext> elements.
    """
    unknown = "unknown"  # Rating unknown or impossible to estimate (default)
    low = "low"  # Little or no potential for disruption, very modest complexity
    medium = "medium"  # Some chance of minor disruption, substantial complexity
    high = "high"  # Likely to cause serious disruption, very complex


class CcOperatorEnumType(Enum):
    """
    The type for the allowed @operator names for the <xccdf:complex-check> operator attribute. Only AND and OR
    operators are supported. (The <xccdf:complex-check> has a separate mechanism for negation.)
    """
    OR = "OR"  # The logical OR of the component terms
    AND = "AND"  # The logical AND of the component terms


class IdentType:
    """
    Data type for the <xccdf:ident> element, a globally meaningful identifier for an <xccdf:Rule>. The body of
    <xccdf:ident> element is the name or identifier of a security configuration issue or vulnerability that the
    <xccdf:Rule> addresses. It has an associated URI that denotes the organization or naming scheme that assigned the
    name. By setting an <xccdf:ident> element on an <xccdf:Rule>, the <xccdf:Benchmark> author effectively declares
    that the <xccdf:Rule> instantiates, implements, or remediates the issue for which the name was assigned.
    """

    def __init__(
            self,
            content: str,
            system: str,
            other: list
    ):
        """

        :param content: The content of the element.
        :param system: Denotes the organization or naming scheme that assigned the identifier.
        :param other: May also have other attributes from other namespaces in order to provide additional metadata for the given identifier.
        """
        self.content = content
        self.system = system
        self.other = other


class WarningType(HtmlTextWithSubType):
    """
    Data type for the <xccdf:warning> element under the <xccdf:Rule> element. This element holds a note or caveat
    about the item intended to convey important cautionary information for the <xccdf:Benchmark> user.
    """

    def __init__(
            self,
            category: WarningCategoryEnumType = WarningCategoryEnumType.general,
            **kwargs
    ):
        """

        :param category: A hint as to the nature of the warning.
        """
        super().__init__(**kwargs)
        self.category = category


class FixTextType(HtmlTextWithSubType):
    """
    Data type for the <xccdf:fixtext> element, which contains data that describes how to bring a target system into
    compliance with an <xccdf:Rule>. Each <xccdf:fixtext> element may be associated with one or more <xccdf:fix>
    elements through the @fixref attribute. The body holds explanatory text about the fix procedures.
    """

    def __init__(
            self,
            fixref: str = None,
            reboot: bool = False,
            strategy: FixStrategyEnumType = FixStrategyEnumType.unknown,
            disruption: RatingEnumType = RatingEnumType.unknown,
            complexity: RatingEnumType = RatingEnumType.unknown,
            **kwargs
    ):
        """

        :param fixref: A reference to the @id of an <xccdf:fix> element.
        :param reboot: True if a reboot is known to be required and false otherwise.
        :param strategy: The method or approach for making the described fix.
        :param disruption: An estimate of the potential for disruption or operational degradation that the application of this fix will impose on the target.
        :param complexity: The estimated complexity or difficulty of applying the fix to the target.
        """
        super().__init__(**kwargs)
        self.fixref = fixref
        self.reboot = reboot
        self.strategy = strategy
        self.disruption = disruption
        self.complexity = complexity


class InstanceFixType:
    """
    Type for an <xccdf:instance> element which may appear in an <xccdf:fix> element. The <xccdf:instance> element
    inside an <xccdf:fix> element designates a spot where the name of the instance should be substituted into the fix
    template to generate the final fix data.
    """

    def __init__(
            self,
            context: str = "undefined"
    ):
        """

        :param context: Describes the scope or significance of the instance content. The context attribute is intended to be informative and does not affect basic processing.
        """
        self.context = context


class FixType:
    """
    Data type for the <xccdf:fix> element. The body of this element contains a command string, script,
    or other system modification statement that, if executed on the target system, can bring it into full,
    or at least better, compliance with this <xccdf:Rule>.
    """

    def __init__(
            self,
            sub: list[SubType] = None,
            instance: list[InstanceFixType] = None,
            id_: str = None,
            reboot: bool = False,
            strategy: FixStrategyEnumType = FixStrategyEnumType.unknown,
            disruption: RatingEnumType = RatingEnumType.unknown,
            complexity: RatingEnumType = RatingEnumType.unknown,
            system: str = None,
            platform: str = None
    ):
        """

        :param sub: Specifies an <xccdf:Value> or <xccdf:plain-text> element to be used for text substitution
        :param instance: Designates a spot where the name of the instance should be substituted into the fix template to generate the final fix data. If the @context attribute is omitted, the value of the @context defaults to “undefined”.
        :param id_: A local identifier for the element. It is optional for the @id to be unique; multiple <xccdf:fix> elements may have the same @id but different values for their other attributes. It is used primarily to allow <xccdf:fixtext> elements to be associated with one or more <xccdf:fix> elements
        :param reboot: True if a reboot is known to be required and false otherwise.
        :param strategy: The method or approach for making the described fix.
        :param disruption: An estimate of the potential for disruption or operational degradation that the application of this fix will impose on the target.
        :param complexity: The estimated complexity or difficulty of applying the fix to the target.
        :param system: A URI that identifies the scheme, language, engine, or process for which the fix contents are written. Table 17 in the XCCDF specification defines several general-purpose URNs that may be used for this, and tool vendors and system providers may define and use target-specific URNs.
        :param platform: In case different fix scripts or procedures are required for different target platform types (e.g., different patches for Windows Vista and Windows 7), this attribute allows a CPE name or CPE applicability language expression to be associated with an <xccdf:fix> element. This should appear on an <xccdf:fix> when the content applies to only one platform out of several to which the <xccdf:Rule> could apply.
        """
        if sub is None:
            sub = []
        if instance is None:
            instance = []

        self.sub = sub
        self.instance = instance
        self.id_ = id_
        self.reboot = reboot
        self.strategy = strategy
        self.disruption = disruption
        self.complexity = complexity
        self.system = system
        self.platform = platform


class CheckImportType:
    """
    Data type for the <xccdf:check-import> element, which specifies a value that the <xccdf:Benchmark> author wishes
    to retrieve from the checking system during testing of a target system. The @import-name attribute identifies
    some structure in the checking system that is then retrieved. The mapping from the values of this attribute to
    specific checking system structures is beyond the scope of the XCCDF specification. When the <xccdf:check-import>
    element appears in the context of an <xccdf:Rule>, then it should be empty and any content must be ignored. When
    the <xccdf:check-import> element appears in the context of an <xccdf:rule-result>, then its body holds the
    imported value.
    """

    def __init__(
            self,
            import_name: str,
            content: list = None,
            import_xpath: str = None
    ):
        """

        :param import_name: An identifier indicating some structure in the checking system to be collected.
        :param content: The content of the element.
        :param import_xpath: An XPath that is used to select specific values or structures from the imported structure. This allows further refinement of the collected data if the imported value takes the form of XML structures.
        """
        if content is None:
            content = []
        self.import_name = import_name
        self.content = content
        self.import_xpath = import_xpath


class CheckExportType:
    """
    Data type for the <xccdf:check-export> element, which specifies a mapping from an <xccdf:Value> element to a
    checking system variable (i.e., external name or id for use by the checking system). This supports export of
    tailoring <xccdf:Value> elements from the XCCDF processing environment to the checking system. The interface
    between the XCCDF benchmark consumer and the checking system should support, at a minimum, passing the
    <xccdf:value> property of the <xccdf:Value> element, but may also support passing the <xccdf:Value> element's
    @type and @operator properties.
    """

    def __init__(
            self,
            value_id: str,
            export_name: str
    ):
        """

        :param value_id: The id of the <xccdf:Value> element to export.
        :param export_name: An identifier indicating some structure in the checking system into which the identified <xccdf:Value> element's properties will be mapped.
        """
        self.value_id = value_id
        self.export_name = export_name


class CheckContentRefType:
    """
    Data type for the <xccdf:check-content-ref> element, which points to the code for a detached check in another
    file. This element has no body, just a couple of attributes: @href and @name. The @name is optional, if it does
    not appear then this reference is to the entire document.
    """

    def __init__(
            self,
            href: str,
            name: str = None
    ):
        """

        :param href: Identifies the referenced document containing checking instructions.
        :param name: Identifies a particular part or element of the referenced check document.
        """
        self.href = href
        self.name = name


class CheckContentType:
    """
    Data type for the <xccdf:check-content> element. The body of this element holds the actual code of a check,
    in the language or system specified by the <xccdf:check> element’s @system attribute. The body of this element
    may be any XML, but cannot contain any XCCDF elements. XCCDF tools do not process its content directly but
    instead pass the content directly to checking engines.
    """

    def __init__(
            self,
            other: list = None
    ):
        """

        :param other:
        """
        if other is None:
            other = []
        self.other = other


class CheckType:
    """
    Data type for the <xccdf:check> element. The <xccdf:check> element identifies instructions for tests to determine
    compliance with the <xccdf:Rule> as well as parameters controlling the reporting of those test results. The
    <xccdf:check> element must have at least one child element.
    """

    def __init__(
            self,
            system: str,
            check_import: list[CheckImportType] = None,
            check_export: list[CheckExportType] = None,
            check_content_ref: list[CheckContentRefType] = None,
            check_content: CheckContentType = None,
            negate: bool = False,
            id_: str = None,
            selector: str = "",
            multi_check: bool = False,
            base: str = None
    ):
        """

        :param system: The URI for a checking system. If the checking system uses XML namespaces, then the system attribute for the system should be its namespace.
        :param check_import: Identifies a value to be retrieved from the checking system during testing of a target system. This element's body must be empty within an <xccdf:check>. After the associated check results have been collected, the result structure returned by the checking engine is processed to collect the named information. This information is then recorded in the check-import element in the corresponding <xccdf:rule-result>.
        :param check_export: A mapping from an <xccdf:Value> element to a checking system variable (i.e., external name or id for use by the checking system). This supports export of tailoring values from the XCCDF processing environment to the checking system.
        :param check_content_ref: Points to code for a detached check in another location that uses the language or system specified by the <xccdf:check> element’s @system attribute. If multiple <xccdf:check-content-ref> elements appear, they represent alternative locations from which a benchmark consumer may obtain the check content. Benchmark consumers should process the alternatives in the order in which they appear in the XML. The first <xccdf:check-content-ref> from which content can be successfully retrieved should be used.
        :param check_content: Holds the actual code of a check, in the language or system specified by the <xccdf:check> element’s @system attribute. If both <xccdf:check-content-ref> and <xccdf:check-content> elements appear in a single <xccdf:check> element, benchmark consumers should use the <xccdf:check-content> element only if none of the references can be resolved to provide content.
        :param negate: If set to true, the final result of the <xccdf:check> is negated according to the truth table given below.
        :param id_: Unique identifier for this element. Optional, but must be globally unique if present.
        :param selector: This may be referenced from <xccdf:Profile> selection elements or used during manual tailoring to refine the application of the <xccdf:Rule>. If no selector values are specified for a given <xccdf:Rule> by <xccdf:Profile> elements or manual tailoring, all <xccdf:check> elements with non-empty @selector attributes are ignored. If an <xccdf:Rule> has multiple <xccdf:check> elements with the same @selector attribute, each must employ a different checking system, as identified by the @system attribute of the <xccdf:check> element.
        :param multi_check: Applicable in cases where multiple checks are executed to determine compliance with a single <xccdf:Rule>. This situation can arise when an <xccdf:check> includes an <xccdf:check-content-ref> element that does not include a @name attribute. The default behavior of a nameless <xccdf:check-content-ref> is to execute all checks in the referenced check content location and AND their results together into a single <xccdf:rule-result> using the AND truth table below. This corresponds to a @multi-check attribute value of “false”. If, however, the @multi-check attribute is set to "true" and a nameless <xccdf:check-content-ref> is used, the <xccdf:Rule> produces a separate <xccdf:rule-result> for each check.
        :param base:
        """
        if check_import is None:
            check_import = []
        if check_export is None:
            check_export = []
        if check_content_ref is None:
            check_content_ref = []

        self.system = system
        self.check_import = check_import
        self.check_export = check_export
        self.check_content_ref = check_content_ref
        self.check_content = check_content
        self.negate = negate
        self.id_ = id_
        self.selector = selector
        self.multi_check = multi_check
        self.base = base


class ComplexCheckType:
    """
    The type for an element that contains a boolean combination of <xccdf:checks>. This element can have only
    <xccdf:complex-check> and <xccdf:check> elements as children. Child elements may appear in any order but at least
    one child element must be present. It has two attributes, @operator and @negate, which dictate how <xccdf:check>
    or <xccdf:complex-check> child elements are to be combined. Truth tables for these operations appear below.
    """

    def __init__(
            self,
            operator: CcOperatorEnumType,
            check: list[CheckType] = None,
            complex_check: list[ComplexCheckType] = None,
            negate: bool = False
    ):
        """

        :param operator: Indicates whether the child <xccdf:check> and/or <xccdf:complex-check> elements of this <xccdf:complex-check> should be combined using an AND or OR operation
        :param check: Instructions for a single test.
        :param complex_check: A child <xccdf:complex-check>, allowing another level of logic in combining component checks.
        :param negate: If true, negate the final result of this <xccdf:complex-check> after the child elements are combined using the identified operator.
        """
        self.operator = operator
        self.check = check
        self.complex_check = complex_check
        self.negate = negate


class WeightType:
    """
    Data type for an <xccdf:Rule> element's weight, a non-negative real number.
    """

    def __init__(
            self,
            content: float
    ):
        """

        :param content: The content of the element.
        """

        self.content = content


# Value-related types

class ValueTypeType(Enum):
    """
    Allowed data types for <xccdf:Value> elements, string, numeric, and boolean. A tool may choose any convenient
    form to store an <xccdf:Value> element’s <xccdf:value> element, but the @type conveys how the value should be
    treated for user input validation purposes during tailoring processing. The @type may also be used to give
    additional guidance to the user or to validate the user’s input. For example, if an <xccdf:value> element’s @type
    attribute is “number”, then a tool might choose to reject user tailoring input that is not composed of digits. In
    the case of a list of values, the @type applies to all elements of the list individually. Note that checking
    systems may have their own understanding of data types that may not be identical to the typing indicated in XCCDF
    """
    number = "number"  # A numeric value. This may be decimal or integer.
    string = "string"  # Any character data
    boolean = "boolean"  # True/false


class ValueOperatorType(Enum):
    """
    This type enumerates allowed values of the @operator property of <xccdf:Value> elements. The specific
    interpretation of these operators depends on the checking system used.
    """
    equals = "equals"
    not_equal = "not equal"
    greater_than = "greater than"
    less_than = "less than"
    greater_than_or_equal = "greater than or equal"
    less_than_or_equal = "less than or equal"
    pattern_match = "pattern match"


class InterfaceHintType(Enum):
    """
    Allowed interface hint values. <xccdf:Value> elements may contain a hint or recommendation to a benchmark
    consumer or producer about how the user might select or adjust the <xccdf:Value>. This type enumerates the
    possible values of this hint.
    """
    choice = "choice"  # Multiple choice
    text_line = "textline"  # Multiple lines of text
    text = "text"  # Single line of text
    date = "date"  # Date
    datetime = "datetime"  # Date and time


class ComplexValueType:
    """
    Data type that supports values that are lists of simple types. Each element in the list is represented by an instance of the <xccdf:item> child element. If there are no <xccdf:item> child elements then this represents an empty list.
    """

    def __init__(
            self,
            item: list[str] = None
    ):
        """

        :param item: A single item in the list of values.
        """
        if item is None:
            item = []
        self.item = item


class SelComplexValueType(ComplexValueType):
    """
    Data type that supports values that are lists of simple types with an associated @selector attribute used in tailoring.
    """

    def __init__(
            self,
            selector: str = "",
            **kwargs
    ):
        """

        :param selector: This may be referenced from <xccdf:Profile> selection elements or used during manual tailoring to refine the application of this property. If no selectors are specified for a given item by <xccdf:Profile> elements or manual tailoring, properties with empty or non-existent @selector attributes are activated. If a selector is applied that does not match the @selector attribute of any of a given type of property, then no <xccdf:choices> element is considered activated. The only exception is the <xccdf:value> and <xccdf:complex-value> properties of an <xccdf:Value> element - if there is no <xccdf:value> or <xccdf:complex-value> property with a matching @selector value then the <xccdf:value>/<xccdf:complex-value> property with an empty or absent @selector attribute becomes active. If there is no such <xccdf:value> or <xccdf:complex-value>, then the first <xccdf:value> or <xccdf:complex-value> listed becomes active. This reflects the fact that all <xccdf:Value> elements require an active value property at all times.
        """
        super().__init__(**kwargs)
        self.selector = selector


class SelChoicesType:
    """
    The type of the <xccdf:choice> element, which specifies a list of legal or suggested choices for an <xccdf:Value>
    object.
    """

    def __init__(
            self,
            choice: str = None,
            complex_choice: ComplexValueType = None,
            must_match: bool = None,
            selector: str = ""
    ):
        """

        :param choice: A single choice holding a simple type. (I.e., number, string, or boolean.)
        :param complex_choice: A single choice holding a list of simple types.
        :param must_match: True if the listed choices are the only permissible settings for the given <xccdf:Value>. False if choices not specified in this <xccdf:choices> element are acceptable settings for this <xccdf:Value>.
        :param selector: This may be referenced from <xccdf:Profile> selection elements or used during manual tailoring to refine the application of the <xccdf:Rule>. If no selectors are specified for a given <xccdf:Value> by <xccdf:Profile> elements or manual tailoring, an <xccdf:choice> element with an empty or non-existent @selector attribute is activated. If a selector is applied that does not match the @selector attribute of any <xccdf:choices> element, then no <xccdf:choices> element is considered activated.
        """
        self.choice = choice
        self.complex_choice = complex_choice
        self.must_match = must_match
        self.selector = selector


class SelStringType:
    """
    This type is for an element that has string content and a @selector attribute for use in tailoring.
    """

    def __init__(
            self,
            content: str,
            selector: str = ""
    ):
        """

        :param content: The content of the element.
        :param selector: This may be referenced from <xccdf:Profile> selection elements or used during manual tailoring to refine the application of this property. If no selectors are specified for a given property by <xccdf:Profile> elements or manual tailoring, properties with empty or non-existent @selector attributes are activated. If a selector is applied that does not match the @selector attribute of any of a given type of property, then no property of that type is considered activated. The only exception is the <xccdf:value> and <xccdf:complex-value> properties of an <xccdf:Value> element - if there is no <xccdf:value> or <xccdf:complex-value> property with a matching @selector value then the <xccdf:value>/<xccdf:complex-value> property with an empty or absent @selector attribute becomes active. If there is no such <xccdf:value> or <xccdf:complex-value>, then the first <xccdf:value> or <xccdf:complex-value> listed in the XML becomes active. This reflects the fact that all <xccdf:Value> elements require an active value property at all times.
        """
        self.content = content
        self.selector = selector


class SelNumType:
    """
    This type is for an element that has numeric content and a @selector attribute for use during tailoring.
    """

    def __init__(
            self,
            content: float,
            selector: str = ""
    ):
        """

        :param content: The content of the element.
        :param selector: This may be referenced from <xccdf:Profile> selection elements or used during manual tailoring to refine the application of this property. If no selectors are specified for a given property by <xccdf:Profile> elements or manual tailoring, properties with empty or non-existent @selector attributes are activated. If a selector is applied that does not match the @selector attribute of any of a given type of property, then no property of that type considered activated.
        """
        self.content = content
        self.selector = selector


class UriRefType:
    """
    Data type for elements that have no content and a single @uri attribute.
    """

    def __init__(
            self,
            uri: str
    ):
        """

        :param uri: A URI.
        """
        self.uri = uri


# Profile-related types


class SeverityEnumType(Enum):
    """
    Allowed severity values for the @severity attribute of an <xccdf:Rule>. The value of this attribute provides an
    indication of the importance of the <xccdf:Rule> element's recommendation. This information is informative only
    and does not affect scoring.
    """
    unknown = "unknown"  # Severity not defined (default).
    info = "info"  # <xccdf:Rule> is informational and failure does not represent a problem.
    low = "low"  # Not a serious problem.
    medium = "medium"  # Fairly serious problem.
    high = "high"  # A grave or critical problem.


class RoleEnumType(Enum):
    """
    Allowed checking and scoring roles for an <xccdf:Rule>.
    """
    full = "full"  # If the <xccdf:Rule> is selected, then check it and let the result contribute to the score and appear in reports (default).
    unscored = "unscored"  # If the <xccdf:Rule> is selected, then check it and include it in the test report, but give the result a status of informational and do not use the result in score computations.
    unchecked = "unchecked"  # Do not check the <xccdf:Rule>; just force the result status to notchecked.


class ProfileSelectType:
    """
    Type for the <xccdf:select> element in an <xccdf:Profile>. This element designates an <xccdf:Rule>,
    <xccdf:Group>, or cluster of <xccdf:Rule> and <xccdf:Group> elements and overrides the @selected attribute on the
    designated items, providing a means for including or excluding <xccdf:Rule> elements from an assessment.
    """

    def __init__(
            self,
            idref: str,
            selected: bool,
            remark: list[TextType] = None
    ):
        """

        :param idref: The @id value of an <xccdf:Rule> or <xccdf:Group>, or the @cluster-id value of one or more <xccdf:Rule> or <xccdf:Group> elements.
        :param selected: The new value for the indicated item's @selected property.
        :param remark: Explanatory material or other prose.
        """
        if remark is None:
            remark = []
        self.idref = idref
        self.selected = selected
        self.remark = remark


class ProfileSetValueType:
    """
    Type for the <xccdf:set-value> element in an <xccdf:Profile>. This element upports the direct specification of
    simple value types such as numbers, strings, and boolean values. This overrides the <xccdf:value> and
    <xccdf:complex-value> element(s) of an <xccdf:Value> element.
    """

    def __init__(
            self,
            content: str,
            idref: str
    ):
        """

        :param content:
        :param idref: The @id value of an <xccdf:Value> or the @cluster-id value of one or more <xccdf:Value> elements
        """
        self.content = content
        self.idref = idref


class ProfileSetComplexValueType(ComplexValueType):
    """
    Type for the <xccdf:set-complex-value> element in an <xccdf:Profile>. This element supports the direct
    specification of complex value types such as lists. Zero or more <xccdf:item> elements may appear as children of
    this element; if no child elements are present, this element represents an empty list. This overrides the
    <xccdf:value> and <xccdf:complex-value> element(s) of an <xccdf:Value> element.
    """

    def __init__(
            self,
            idref: str,
            **kwargs
    ):
        """

        :param idref: The @id value of an <xccdf:Value> or the @cluster-id value of one or more <xccdf:Value> elements
        """
        super().__init__(**kwargs)
        self.idref = idref


class ProfileRefineValueType:
    """
    Type for the <xccdf:refine-value> element in an <xccdf:Profile>. This element designates the <xccdf:Value>
    constraints to be applied during tailoring for an <xccdf:Value> element or the <xccdf:Value> members of a cluster.
    """

    def __init__(
            self,
            idref: str,
            remark: list[TextType] = None,
            selector: str = None,
            operator: ValueOperatorType = None
    ):
        """

        :param idref: The @id value of an <xccdf:Value> or the @cluster-id value of one or more <xccdf:Value> elements
        :param remark: Explanatory material or other prose.
        :param selector: Holds a selector value corresponding to the value of a @selector property in an <xccdf:Value> element's child properties. Properties with a matching @selector are considered active and all other properties are inactive. This may mean that, after selector application, some classes of <xccdf:Value> properties will be completely inactive because none of those properties had a matching @selector. The only exception is the <xccdf:value> and <xccdf:complex-value> properties of an <xccdf:Value> element - if there is no <xccdf:value> or <xccdf:complex-value> property with a matching @selector value then the <xccdf:value>/<xccdf:complex-value> property with an empty or absent @selector attribute becomes active. If there is no such <xccdf:value> or <xccdf:complex-value>, then the first <xccdf:value> or <xccdf:complex-value> listed in the XML becomes active. This reflects the fact that all <xccdf:Value> elements require an active value property at all times.
        :param operator: The new value for the identified <xccdf:Value> element's @operator property.
        """
        if remark is None:
            remark = []
        self.idref = idref
        self.remark = remark
        self.selector = selector
        self.operator = operator


class ProfileRefineRuleType:
    """
    Type for the <xccdf:refine-rule> element in an <xccdf:Profile>. A <xccdf:refine-rule> element allows the author
    to select <xccdf:check> statements and override the @weight, @severity, and @role of an <xccdf:Rule>,
    <xccdf:Group>, or cluster of <xccdf:Rule> and <xccdf:Group> elements. Despite the name, this selector does apply
    for <xccdf:Group> elements and for clusters that include <xccdf:Group> elements, but it only affects their
    @weight attribute.
    """

    def __init__(
            self,
            idref: str,
            remark: list[TextType] = None,
            weight: WeightType = None,
            selector: str = None,
            severity: SeverityEnumType = None,
            role: RoleEnumType = None
    ):
        """

        :param idref: The @id value of an <xccdf:Rule> or <xccdf:Group>, or the @cluster-id value of one or more <xccdf:Rule> or <xccdf:Group> elements.
        :param remark: Explanatory material or other prose.
        :param weight: The new value for the identified element's @weight property.
        :param selector: Holds a selector value corresponding to the value of a @selector property in an <xccdf:Rule> element's <xccdf:check> element. If the selector specified does not match any of the @selector attributes specified on any of the <xccdf:check> children of an <xccdf:Rule>, then the <xccdf:check> child element without a @selector attribute is used. If there is no child without a @selector attribute, then that Rule would have no effective <xccdf:check> element.
        :param severity: The new value for the identified <xccdf:Rule> element's @severity property.
        :param role: The new value for the identified <xccdf:Rule> element's @role property.
        """
        if remark is None:
            remark = []
        self.idref = idref
        self.remark = remark
        self.weight = weight
        self.selector = selector
        self.severity = severity
        self.role = role


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


# Group element

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


# Rule element

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


# Value element

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


# Profile element

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


# TestResult element

class MsgSevEnumType(Enum):
    """
    Allowed values to indicate the severity of messages from the checking engine. These values don't affect scoring
    themselves but are present merely to convey diagnostic information from the checking engine. Benchmark consumers
    may choose to log these messages or display them to the user.
    """
    error = "error"  # Denotes a serious problem identified; test did not run.
    warning = "warning"  # Denotes a possible issue; test may not have run.
    info = "info"  # Denotes important information about the tests.


class ResultEnumType(Enum):
    """
    Allowed result indicators for a test.
    """
    pass_ = "pass"  # The target system or system component satisfied all the conditions of the <xccdf:Rule>.
    fail = "fail"  # The target system or system component did not satisfy all the conditions of the <xccdf:Rule>.
    error = "error"  # The checking engine could not complete the evaluation; therefore the status of the target’s compliance with the <xccdf:Rule> is not certain. This could happen, for example, if a testing tool was run with insufficient privileges and could not gather all of the necessary information.
    unknown = "unknown"  # The testing tool encountered some problem and the result is unknown. For example, a result of ‘unknown’ might be given if the testing tool was unable to interpret the output of the checking engine (the output has no meaning to the testing tool).
    not_applicable = "notapplicable"  # The <xccdf:Rule> was not applicable to the target of the test. For example, the <xccdf:Rule> might have been specific to a different version of the target OS, or it might have been a test against a platform feature that was not installed.
    not_checked = "notchecked"  # The <xccdf:Rule> was not evaluated by the checking engine. This status is designed for <xccdf:Rule> elements that have no check. It may also correspond to a status returned by a checking engine if the checking engine does not support the indicated check code.
    not_selected = "notselected"  # The <xccdf:Rule> was not selected in the <xccdf:Benchmark>.
    informational = "informational"  # The <xccdf:Rule> was checked, but the output from the checking engine is simply information for auditors or administrators; it is not a compliance category. This status value is designed for <xccdf:Rule> elements whose main purpose is to extract information from the target rather than test the target.
    fixed = "fixed"  # The <xccdf:Rule> had failed, but was then fixed (possibly by a tool that can automatically apply remediation, or possibly by the human auditor).


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
