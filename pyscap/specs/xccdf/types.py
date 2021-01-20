# Element types

class ItemType:
    """
    This abstract itemType represents the basic data shared by all <xccdf:Group>, <xccdf:Rule> and <xccdf:Value>
    elements. All elements in an itemType are optional, although each element that builds on the itemType may add its
    own elements, some of which will be required for that element.
    """


class SelectableItemType(ItemType):
    """
    This abstract item type represents the basic data shared by all <xccdf:Group> and <xccdf:Rule> elements.
    """


class StatusType:
    """
    The statusType represents the possible levels of maturity or consensus level for its parent element as recorded
    by an <xccdf:status> element.
    """


class GroupType(SelectableItemType):
    """
    Data type for the <xccdf:Group> element. A <xccdf:Group> element contains descriptive information about a portion
    of an <xccdf:Benchmark>, as well as <xccdf:Rule>, <xccdf:Value>, and/or other <xccdf:Group> elements
    """


class RuleType(SelectableItemType):
    """
    Data type for the <xccdf:Rule> element that represents a specific <xccdf:Benchmark> test.
    """


class ValueType(ItemType):
    """
    Data type for the <xccdf:Value> element, which is a named parameter that can be substituted into properties of
    other elements within the <xccdf:Benchmark>, including the interior of structured check specifications and fix
    scripts.
    """


class ProfileType:
    """
    Data type for the <xccdf:Profile> element, which holds a specific tailoring of the <xccdf:Benchmark>. The main
    part of an <xccdf:Profile> is the selectors: <xccdf:select>, <xccdf:set-value>, <xccdf:set-complex-value>,
    <xccdf:refine-rule>, and <xccdf:refine-value>. An <xccdf:Profile> may also be signed with an XML-Signature.
    """


class TestResultType:
    """
    The <xccdf:TestResult> element encapsulates the results of a single application of an <xccdf:Benchmark> to a
    single target platform. The <xccdf:TestResult> element normally appears as the child of the <xccdf:Benchmark>
    element, although it may also appear as the top-level element of an XCCDF results document. XCCDF is not intended
    to be a database format for detailed results; the <xccdf:TestResult> element offers a way to store the results of
    individual tests in modest detail, with the ability to reference lower-level testing data.
    """


class TailoringType:
    """
    The <xccdf:Tailoring> element holds one or more <xccdf:Profile> elements. These <xccdf:Profile> elements record
    additional tailoring activities that apply to a given <xccdf:Benchmark>. <xccdf:Tailoring> elements are separate
    from <xccdf:Benchmark> documents, but each <xccdf:Tailoring> element is associated with a specific
    <xccdf:Benchmark> document. By defining these tailoring actions separately from the <xccdf:Benchmark> document to
    which they apply, these actions can be recorded without affecting the integrity of the source itself.
    """
