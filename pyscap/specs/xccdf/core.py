from .globals import *


# Group

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


# Rule

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


# Value

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


# Profile

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


# TestResult

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


#  Tailoring

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


# Benchmark

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
