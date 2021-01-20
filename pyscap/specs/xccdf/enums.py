from enum import Enum


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
    or_ = "OR"  # The logical OR of the component terms
    and_ = "AND"  # The logical AND of the component terms


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


class SubUseEnumType(Enum):
    """
    This holds the possible values of the @use attribute within an <xccdf:sub> element. The @use attribute is only
    applicable with the subType's @idref attribute holds the value of the @id of an <xccdf:Value> element.
    """
    value = "value"  # Replace with the selected <xccdf:value> or <xccdf:complex-value> of an <xccdf:Value>.
    title = "title"  # Replace with the <xccdf:title> of the <xccdf:Value>.
    legacy = "legacy"  # Use the context-dependent processing of <xccdf:sub> elements outlined in XCCDF 1.1.4.
