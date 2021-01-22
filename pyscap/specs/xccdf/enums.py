from enum import Enum


class CcOperatorEnumType(Enum):
    """The type for the allowed @operator names for the.

    <xccdf:complex-check> operator attribute. Only AND and OR
    operators are supported. (The <xccdf:complex-check> has a
    separate mechanism for negation.)

    :cvar OR_VALUE: The logical OR of the component terms
    :cvar AND_VALUE: The logical AND of the component
        terms
    """
    OR_VALUE = "OR"
    AND_VALUE = "AND"


class FixStrategyEnumType(Enum):
    """Allowed @strategy keyword values for an.

    <xccdf:Rule> element's <xccdf:fix> or
    <xccdf:fixtext> elements. The values indicate the method or
    approach for fixing non-compliance with a particular
    <xccdf:Rule>.

    :cvar UNKNOWN: Strategy not defined
        (default)
    :cvar CONFIGURE: Adjust target
        configuration/settings
    :cvar COMBINATION: Combination of two or more
        approaches
    :cvar DISABLE: Turn off or uninstall a target component
    :cvar ENABLE: Turn on or install a target
        component
    :cvar PATCH: Apply a patch, hotfix, update,
        etc.
    :cvar POLICY: Remediation requires out-of-band adjustments to
        policies or procedures
    :cvar RESTRICT: Adjust permissions, access rights, filters, or
        other access restrictions
    :cvar UPDATE: Install, upgrade or update the
        system
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


class InterfaceHintType(Enum):
    """Allowed interface hint values.

    <xccdf:Value> elements may contain a hint or recommendation to
    a benchmark consumer or producer about how the user might select or
    adjust the <xccdf:Value>. This type enumerates the possible
    values of this hint.

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


class MsgSevEnumType(Enum):
    """Allowed values to indicate the severity of messages from the checking
    engine.

    These values don't affect scoring themselves but are present merely
    to convey diagnostic information from the checking engine. Benchmark
    consumers may choose to log these messages or display them to the
    user.

    :cvar ERROR: Denotes a serious problem identified; test did
        not run.
    :cvar WARNING: Denotes a possible issue; test may not have
        run.
    :cvar INFO: Denotes important information about the tests.
    """
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


class RatingEnumType(Enum):
    """This type enumerates allowed rating values the disruption and complexity
    properties of an <xccdf:Rule> element's.

    <xccdf:fix> or <xccdf:fixtext> elements.

    :cvar UNKNOWN: Rating unknown or impossible to estimate
        (default)
    :cvar LOW: Little or no potential for disruption, very
        modest complexity
    :cvar MEDIUM: Some chance of minor disruption, substantial
        complexity
    :cvar HIGH: Likely to cause serious disruption, very
        complex
    """
    UNKNOWN = "unknown"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class ResultEnumType(Enum):
    """
    Allowed result indicators for a test.

    :cvar PASS_VALUE: The target system or system component satisfied
        all the conditions of the <xccdf:Rule>.
    :cvar FAIL: The target system or system component did not
        satisfy all the conditions of the <xccdf:Rule>.
    :cvar ERROR: The checking engine could not complete the
        evaluation; therefore the status of the target’s compliance with
        the                         <xccdf:Rule> is not certain.
        This could happen, for example, if a
        testing tool was run with insufficient privileges and could not
        gather all                         of the necessary information.
    :cvar UNKNOWN: The testing tool encountered some problem and
        the result is unknown. For example, a result of ‘unknown’ might
        be given if                         the testing tool was unable
        to interpret the output of the checking engine
        (the output has no meaning to the testing tool).
    :cvar NOTAPPLICABLE: The <xccdf:Rule> was not applicable to
        the target of the test. For example, the <xccdf:Rule>
        might have been                         specific to a different
        version of the target OS, or it might have been a
        test against a platform feature that was not installed.
    :cvar NOTCHECKED: The <xccdf:Rule> was not evaluated by the
        checking engine. This status is designed for <xccdf:Rule>
        elements                         that have no check. It may also
        correspond to a status returned by a
        checking engine if the checking engine does not support the
        indicated check                         code.
    :cvar NOTSELECTED: The <xccdf:Rule> was not selected in the
        <xccdf:Benchmark>.
    :cvar INFORMATIONAL: The <xccdf:Rule> was checked, but the
        output from the checking engine is simply information for
        auditors or                         administrators; it is not a
        compliance category. This status value is
        designed for <xccdf:Rule> elements whose main purpose is
        to extract                         information from the target
        rather than test the target.
    :cvar FIXED: The <xccdf:Rule> had failed, but was then
        fixed (possibly by a tool that can automatically apply
        remediation, or                         possibly by the human
        auditor).
    """
    PASS_VALUE = "pass"
    FAIL = "fail"
    ERROR = "error"
    UNKNOWN = "unknown"
    NOTAPPLICABLE = "notapplicable"
    NOTCHECKED = "notchecked"
    NOTSELECTED = "notselected"
    INFORMATIONAL = "informational"
    FIXED = "fixed"


class RoleEnumType(Enum):
    """Allowed checking and scoring roles for an.

    <xccdf:Rule>.

    :cvar FULL: If the <xccdf:Rule> is selected, then
        check it and let the result contribute to the score and appear
        in reports                         (default).
    :cvar UNSCORED: If the <xccdf:Rule> is selected, then
        check it and include it in the test report, but give the result
        a status of                         informational and do not use
        the result in score computations.
    :cvar UNCHECKED: Do not check the <xccdf:Rule>; just force
        the result status to notchecked.
    """
    FULL = "full"
    UNSCORED = "unscored"
    UNCHECKED = "unchecked"


class SeverityEnumType(Enum):
    """Allowed severity values for the @severity attribute of an
    <xccdf:Rule>.

    The value of this attribute provides an indication of the importance
    of the <xccdf:Rule> element's recommendation. This information
    is informative only and does not affect scoring.

    :cvar UNKNOWN: Severity not defined (default).
    :cvar INFO: <xccdf:Rule> is informational and failure
        does not represent a problem.
    :cvar LOW: Not a serious problem.
    :cvar MEDIUM: Fairly serious problem.
    :cvar HIGH: A grave or critical problem.
    """
    UNKNOWN = "unknown"
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class StatusType(Enum):
    """The statusType represents the possible levels of maturity or consensus
    level for its parent element as recorded by an.

    <xccdf:status> element.

    :cvar ACCEPTED: Released as final
    :cvar DEPRECATED: No longer needed
    :cvar DRAFT: Released in draft state
    :cvar INCOMPLETE: Under initial development
    :cvar INTERIM: Revised and in the process of being
        finalized
    """
    ACCEPTED = "accepted"
    DEPRECATED = "deprecated"
    DRAFT = "draft"
    INCOMPLETE = "incomplete"
    INTERIM = "interim"


class SubUseEnumType(Enum):
    """This holds the possible values of the @use attribute within an
    <xccdf:sub> element.

    The @use attribute is only applicable with the subType's @idref
    attribute holds the value of the @id of an <xccdf:Value>
    element.

    :cvar VALUE: Replace with the selected <xccdf:value>
        or <xccdf:complex-value> of an <xccdf:Value>.
    :cvar TITLE: Replace with the <xccdf:title> of the
        <xccdf:Value>.
    :cvar LEGACY: Use the context-dependent processing of
        <xccdf:sub> elements outlined in XCCDF 1.1.4.
    """
    VALUE = "value"
    TITLE = "title"
    LEGACY = "legacy"


class ValueOperatorType(Enum):
    """This type enumerates allowed values of the @operator property of
    <xccdf:Value> elements.

    The specific interpretation of these operators depends on the
    checking system used.
    """
    EQUALS = "equals"
    NOT_EQUAL = "not equal"
    GREATER_THAN = "greater than"
    LESS_THAN = "less than"
    GREATER_THAN_OR_EQUAL = "greater than or equal"
    LESS_THAN_OR_EQUAL = "less than or equal"
    PATTERN_MATCH = "pattern match"


class ValueTypeType(Enum):
    """Allowed data types for <xccdf:Value> elements, string, numeric,
    and boolean. A tool may choose any convenient form to store an.

    <xccdf:Value> element’s <xccdf:value> element, but the
    @type conveys how the value should be treated for user input
    validation purposes during tailoring processing. The @type may also
    be used to give additional guidance to the user or to validate the
    user’s input. For example, if an <xccdf:value> element’s @type
    attribute is “number”, then a tool might choose to reject user
    tailoring input that is not composed of digits. In the case of a
    list of values, the @type applies to all elements of the list
    individually. Note that checking systems may have their own
    understanding of data types that may not be identical to the typing
    indicated in XCCDF

    :cvar NUMBER: A numeric value. This may be decimal or
        integer.
    :cvar STRING: Any character data
    :cvar BOOLEAN: True/false
    """
    NUMBER = "number"
    STRING = "string"
    BOOLEAN = "boolean"


class WarningCategoryEnumType(Enum):
    """Allowed warning category keywords for the.

    <xccdf:warning> element used in <xccdf:Rule> elements.

    :cvar GENERAL: Broad or general-purpose warning
        (default)
    :cvar FUNCTIONALITY: Warning about possible impacts to functionality
        or operational features
    :cvar PERFORMANCE: Warning about changes to target system
        performance or throughput
    :cvar HARDWARE: Warning about hardware restrictions or possible
        impacts to hardware
    :cvar LEGAL: Warning about legal
        implications
    :cvar REGULATORY: Warning about regulatory obligations or
        compliance implications
    :cvar MANAGEMENT: Warning about impacts to the management or
        administration of the target system
    :cvar AUDIT: Warning about impacts to audit or
        logging
    :cvar DEPENDENCY: Warning about dependencies between this element
        and other parts of the target system, or version
        dependencies
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
