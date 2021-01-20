from .types import *


# Base elements

class Item(ItemType):
    """
    An item is a named constituent of an <xccdf:Benchmark>. There are three types of items: <xccdf:Group>,
    <xccdf:Rule> and <xccdf:Value>. The <xccdf:Item> element type imposes constraints shared by all <xccdf:Group>,
    <xccdf:Rule> and <xccdf:Value> elements. The itemType is abstract, so the element <xccdf:Item> can never appear
    in a valid XCCDF document.
    """


# Global elements

class Status(StatusType):
    """
    The acceptance status of an element with an optional date attribute, which signifies the date of the status
    change. If an element does not have its own <xccdf:status> element, its status is that of its parent element. If
    there is more than one <xccdf:status> for a single element, then every instance of the <xccdf:status> element
    must have a @date attribute, and the <xccdf:status> element with the latest date is considered the current status.
    """


class Model:
    """
    A suggested scoring model for an <xccdf:Benchmark>, also encapsulating any parameters needed by the model. Every
    model is designated with a URI, which appears here as the system attribute. See the XCCDF specification for a
    list of standard scoring models and their associated URIs. Vendors may define their own scoring models and
    provide additional URIs to designate them. Some models may need additional parameters; to support such a model,
    zero or more <xccdf:param> elements may appear as children of the <xccdf:model> element.
    """


# Main elements

class Group(GroupType):
    """
    An item that can hold other items. It allows an author to collect related items into a common structure and
    provide descriptive text and references about them.
    """


class Rule(RuleType):
    """
    The <xccdf:Rule> element contains the description for a single item of guidance or constraint. <xccdf:Rule>
    elements form the basis for testing a target platform for compliance with an <xccdf:Benchmark>, for scoring,
    and for conveying descriptive prose, identifiers, references, and remediation information.
    """


class Value(ValueType):
    """
    The <xccdf:Value> element is a named parameter that can be substituted into properties of other elements within
    the <xccdf:Benchmark>, including the interior of structured check specifications and fix scripts.
    """


class Profile(ProfileType):
    """
    The <xccdf:Profile> element is a named tailoring for an <xccdf:Benchmark>. While an <xccdf:Benchmark> can be
    tailored in place by setting properties of various elements, <xccdf:Profile> elements allow one <xccdf:Benchmark>
    document to hold several independent tailorings.
    """


class TestResult(TestResultType):
    """
    The <xccdf:TestResult> element encapsulates the results of a single application of an <xccdf:Benchmark> to a
    single target platform. The <xccdf:TestResult> element normally appears as the child of the <xccdf:Benchmark>
    element, although it may also appear as the top-level element of an XCCDF results document. XCCDF is not intended
    to be a database format for detailed results; the <xccdf:TestResult> element offers a way to store the results of
    individual tests in modest detail, with the ability to reference lower-level testing data.
    """


class Tailoring(TailoringType):
    """
    The <xccdf:Tailoring> element holds one or more <xccdf:Profile> elements. These <xccdf:Profile> elements record
    additional tailoring activities that apply to a given <xccdf:Benchmark>. <xccdf:Tailoring> elements are separate
    from <xccdf:Benchmark> documents, but each <xccdf:Tailoring> element is associated with a specific
    <xccdf:Benchmark> document. By defining these tailoring actions separately from the <xccdf:Benchmark> document to
    which they apply, these actions can be recorded without affecting the integrity of the source itself.
    """


# Root element

class Benchmark:
    """
    This is the root element of the XCCDF document; it must appear exactly once. It encloses the entire benchmark,
    and contains both descriptive information and structural information. Note that the order of <xccdf:Group> and
    <xccdf:Rule> child elements may matter for the appearance of a generated document. <xccdf:Group> and <xccdf:Rule>
    children may be freely intermingled, but they must appear after any <xccdf:Value> children. All the other
    children must appear in the order shown.
    """
