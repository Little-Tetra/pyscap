from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from ..common.utils import scap_parser, scap_json_parser, scap_serializer, scap_json_serializer


@dataclass
class ArtifactRefType:
    """
    The ArtifactRefType type defines a single artifact reference that may be
    collected as part of a questionnaire assessment.

    :ivar idref: The identifier of a referenced artifact.
    :ivar required: The required element specifies whether the artifact
        must be included or not. If true, then it must be included. The
        questionnaire is not considered complete without it. Otherwise,
        it is                desired but not necessary.
    """
    idref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:artifact:[1-9][0-9]*",
        }
    )
    required: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ArtifactValueType:
    """
    The ArtifactValueType type defines structures containing either the
    artifact data itself or a pointer to it.
    """


class BooleanQuestionModelType(Enum):
    """
    The BooleanQuestionModelType type provides the acceptable models (i.e. set
    of acceptable responses) for a boolean_question.

    :cvar MODEL_YES_NO: MODEL_YES_NO represents a response set of {YES,
        NO}.
    :cvar MODEL_TRUE_FALSE: MODEL_TRUE_FALSE represents a response set
        of                   {TRUE, FALSE}.
    """
    MODEL_YES_NO = "MODEL_YES_NO"
    MODEL_TRUE_FALSE = "MODEL_TRUE_FALSE"


@dataclass
class ChoiceAnswerType:
    """
    The ChoiceAnswerType type defines structures containing a choice_ref
    attribute that identifies the selected choice.

    :ivar choice_ref: The choice_ref attribute specifies the id of the
        selected choice.
    """
    choice_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:choice:[1-9][0-9]*",
        }
    )


@dataclass
class ChoiceType:
    """
    The ChoiceType type defines structures that hold information about one
    acceptable answer to a choice_question.

    :ivar value:
    :ivar id: All choices are tagged with a unique identifier
        that may be referenced by a choice_test_action referencing the
        encapsulating choice_question.
    :ivar var_ref:
    """
    value: Optional[str] = field(
        default=None,
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:choice:[1-9][0-9]*",
        }
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:variable:[1-9][0-9]*",
        }
    )


@dataclass
class DocumentType:
    """
    The DocumentType type describes structures used to provide document-level
    information, including title, descriptions, and notices.

    :ivar title: The title element provides a title for this document.
    :ivar description: Each description element contains part of an
        overall description for the entire document. (Note that
        questionnaires contain their own description for questionnaire
        specific descriptions.) TODO: Consider changing this to XHTML
        structured text in the next revision.
    :ivar notice: Each notice element contains a notice or warning to
        the                  user of this document. TODO: Consider
        changing this to XHTML structured text in the next revision.
    """
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )
    description: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    notice: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )


class ExceptionalResultType(Enum):
    """
    The ExceptionalResultType type defines possible exceptional results of a
    question.

    :cvar UNKNOWN: An UNKNOWN value indicates that the result of a
        test cannot be determined.
    :cvar ERROR: An ERROR value indicates that an error occured
        while processing the check. Among other causes, this can
        indicate an                  unexpected response.
    :cvar NOT_TESTED: A NOT_TESTED value indicates that the check has
        not                   been tested yet.
    :cvar NOT_APPLICABLE: A NOT_APPLICABLE value indicates that the
        check is                   not relevant and can be skipped.
    """
    UNKNOWN = "UNKNOWN"
    ERROR = "ERROR"
    NOT_TESTED = "NOT_TESTED"
    NOT_APPLICABLE = "NOT_APPLICABLE"


@dataclass
class ExtensionContainerType:
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "min_occurs": 1,
        }
    )


@dataclass
class ItemBaseType:
    """The ItemBaseType complex type defines structures allowing a set of notes
    to be included.

    This type is inherited by many of the elements in the OCIL language.

    :ivar notes: An optional set of notes to describe additional
        information.
    :ivar revision: The specific refision of this item. This attribute
        is                   optional to support compatability with
        existing content.  By default                   the revision is
        '0' meaning that it is the initial revision. It is
        assumed that subsequent revisions will increment this value by
        1.
    """
    notes: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    revision: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )


class OperatorType(Enum):
    """
    The OperatorType simple type provides a list of possible operator values
    that operate on a set of test_action elements.

    :cvar AND_VALUE: The AND operator produces a true result if every
        argument is true. If one or more arguments are false, the result
        of                   the AND is false. See the truth table
        provided in the ResultType                   type for a complete
        list of how the various result types are
        combined by an AND operation.
    :cvar OR_VALUE: The OR operator produces a true result if one or
        more arguments is true. If every argument is false, the result
        of                   the OR is false. See the truth table
        provided in the ResultType                   type for a complete
        list of how the various result types are
        combined by an OR operation.
    """
    AND_VALUE = "AND"
    OR_VALUE = "OR"


@dataclass
class PatternType:
    """
    The PatternType type defines a structure that specifies a regular
    expression against which a string will be compared.
    """
    value: Optional[str] = field(
        default=None,
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:variable:[1-9][0-9]*",
        }
    )


@dataclass
class RangeValueType:
    """
    Defines a specific bound in a range.

    :ivar value:
    :ivar inclusive: The inclusive attribute specifies whether the
        value should be in the specified range. The default is true,
        indicating it is included.
    :ivar var_ref: A reference to a variable to use as the value.
    """
    value: Optional[Decimal] = field(
        default=None,
    )
    inclusive: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:variable:[1-9][0-9]*",
        }
    )


class ResultType(Enum):
    """The ResultType simple type defines acceptable result values for
    questionnaires and test_actions.

    || P   | F | E | U | NT | NA ||
    ---------------||-----------------------------||------------------||------------------------------------------
    || 1+ | 0   | 0   | 0   | 0   | 0+ || Pass
    || 0+ | 1+ | 0+ | 0+ | 0+ | 0+ || Fail
    AND     || 0+ | 0   | 1+ | 0+ | 0+ | 0+ || Error
    || 0+ | 0   | 0   | 1+ | 0+ | 0+ || Unknown
    || 0+ | 0   | 0   | 0   | 1+ | 0+ || Not Tested
    || 0   | 0   | 0   | 0   | 0   | 1+ || Not Applicable
    || 0   | 0   | 0   | 0   | 0   | 0   || Not Tested
    ---------------||-----------------------------||------------------||------------------------------------------
    || 1+ | 0+ | 0+ | 0+ | 0+ | 0+ || Pass
    || 0   | 1+ | 0   | 0   | 0   | 0+ || Fail
    OR      || 0   | 0+ | 1+ | 0+ | 0+ | 0+ || Error
    || 0   | 0+ | 0   | 1+ | 0+ | 0+ || Unknown
    || 0   | 0+ | 0   | 0   | 1+ | 0+ || Not Tested
    || 0   | 0   | 0   | 0   | 0   | 1+ || Not Applicable
    || 0   | 0   | 0   | 0   | 0   | 0   || Not Tested

    :cvar UNKNOWN: An UNKNOWN value indicates that the result of a
        test cannot be determined.
    :cvar ERROR: An ERROR value indicates that an error occured
        while processing the check. Among other causes, this can
        indicate an                  unexpected response.
    :cvar NOT_TESTED: A NOT_TESTED value indicates that the check has
        not                   been tested yet.
    :cvar NOT_APPLICABLE: A NOT_APPLICABLE value indicates that the
        check is                   not relevant and can be skipped.
    :cvar PASS_VALUE: A PASS value indicates that the check passed
        its test.
    :cvar FAIL: A FAIL value indicates that the check did not
        pass its test.
    """
    UNKNOWN = "UNKNOWN"
    ERROR = "ERROR"
    NOT_TESTED = "NOT_TESTED"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    PASS_VALUE = "PASS"
    FAIL = "FAIL"


@dataclass
class SetExpressionBaseType:
    """The SetExpressionBaseType type is the base type of all set expressions.

    It defines the value to use if the expression evaluates to TRUE.

    :ivar value: The value element contains the data to be stored on
        the variable if the expression evaluates to TRUE.
    """
    value: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )


@dataclass
class SetExpressionBooleanType:
    """
    :ivar value: The boolean value to match.
    """
    value: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SubstitutionTextType:
    """
    A type that is used to represent text from a variable that may be inserted
    into a text string within this model.
    """
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:variable:[1-9][0-9]*",
        }
    )


@dataclass
class TestActionRefType:
    """
    The TestActionRefType type defines a structure that holds a reference (id)
    to a test_action or questionnaire.

    :ivar value:
    :ivar negate: The negate attribute can be used to specify
        whether to toggle the result from PASS to FAIL, and vice versa.
        A result other than PASS or FAIL (e.g. ERROR, NOT_TESTED)
        will be unchanged by a negate operation.
    """
    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:testaction:[1-9][0-9]*|ocil:[A-Za-z0-9_\-\.]+:questionnaire:[1-9][0-9]*",
        }
    )
    negate: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TextType:
    """
    The TextType complex type defines an element that holds basic string
    information.

    :ivar value:
    :ivar lang: This attribute specifies the language in which
        to interpret the information.
    """
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


class UserResponseType(Enum):
    """The UserResponseType type defines structures containing the type of
    response.

    The question could have been answered or an exceptional condition
    may have occurred.

    :cvar UNKNOWN: An UNKNOWN value indicates that the result of a
        test cannot be determined.
    :cvar ERROR: An ERROR value indicates that an error occured
        while processing the check. Among other causes, this can
        indicate an                  unexpected response.
    :cvar NOT_TESTED: A NOT_TESTED value indicates that the check has
        not                   been tested yet.
    :cvar NOT_APPLICABLE: A NOT_APPLICABLE value indicates that the
        check is                   not relevant and can be skipped.
    :cvar ANSWERED: Indicates that the question was answered.
    """
    UNKNOWN = "UNKNOWN"
    ERROR = "ERROR"
    NOT_TESTED = "NOT_TESTED"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    ANSWERED = "ANSWERED"


class VariableDataType(Enum):
    """
    The VariableDataType simple type defines how a variable data value should
    be treated or used.

    :cvar TEXT: The TEXT value specifies that the variable data
        value should be treated as text.
    :cvar NUMERIC: The NUMERIC value specifies that the variable data
        value should be treated as numeric.
    """
    TEXT = "TEXT"
    NUMERIC = "NUMERIC"


@dataclass
class ArtifactRefsType:
    """
    The ArtifactRefsType type defines a collection of artifact references that
    may be collected as part of a questionnaire assessment.

    :ivar artifact_ref: A single reference to an artifact.
    """
    artifact_ref: List[ArtifactRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )


@dataclass
class ArtifactType(ItemBaseType):
    """
    The ArtifactType type defines structures containing information about an
    artifact such as title, description, persistence, and if it's required to
    complete an answer to a question.

    :ivar title: The title element holds a short summary or a
        caption about the artifact.
    :ivar description: The description element holds information that
        describes what the artifact is about.
    :ivar id: Each item is required to have a unique identifier
        that conforms to the definition of NCName in the Recommendation
        "Namespaces in XML 1.0", i.e., all XML 1.0 names that do not
        contain              colons.
    :ivar persistent: The persistent attribute specifies whether the
        artifact is time sensitive or not. If the value is true, then a
        snapshot or a copy must be kept. Otherwise, a pointer to the
        location               of the artifact is enough. The default
        value is               true.
    """
    title: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )
    description: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:artifact:[1-9][0-9]*",
        }
    )
    persistent: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ChoiceGroupType:
    """The ChoiceGroupType type defines a group of choices that may then be
    reused in multiple choice_question elements.

    For example, a document may include multiple choice_questions with
    the options of "Good", "Fair", or "Poor". By defining these choices
    in a single choice_group, the author would not need to list them out
    explicitly in every choice_question.

    :ivar choice: Holds the information associated with one of the
        possible responses for a choice_question.
    :ivar id: Holds the id of this choice group. This id is
        referenced within choice_question elements to include the
        choices                contained in a group.
    """
    choice: List[ChoiceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:choicegroup:[1-9][0-9]*",
        }
    )


@dataclass
class EmbeddedArtifactValueType(ArtifactValueType):
    """
    The base data structure that holds artifact values that are embedded into
    the results model.

    :ivar mime_type: The MIME type of the embedded content.  Since the
        list of MIME types are continually expanding, this schema
        does not make an attempt to constrain the allowed
        values.
    """
    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class NamedItemBaseType(ItemBaseType):
    """
    The NamedItemBaseType complex type defines structures allowing a set of
    notes and the name of a target (system or user) to be included.

    :ivar name: The name element holds the name of a target
        (system or user).
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )


@dataclass
class OperationType:
    """
    The OperationType type defines structures that hold a set of test_actions
    and provide instructions as to how to aggregate their individual results
    into a single result.

    :ivar test_action_ref: The test_action_ref element holds the
        identifier                   of a test_action element. At least
        one test_action_ref must be                   included.
    :ivar operation: The operation attribute describes how to aggregate
        the                results of a set of test_actions. Its value
        defaults to the Boolean                operator "AND".
    :ivar negate: The negate attribute can be used to specify whether to
        toggle the result from PASS to FAIL, and vice versa. A result
        other                than PASS or FAIL (e.g. ERROR, NOT_TESTED)
        will be unchanged by                a negate operation.
    """
    test_action_ref: List[TestActionRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    operation: OperatorType = field(
        default=OperatorType.AND_VALUE,
        metadata={
            "type": "Attribute",
        }
    )
    negate: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class QuestionResultType:
    """
    The QuestionResultType complex type defines structures that hold
    information about a question and the response to it.

    :ivar question_ref: The question_ref attribute contains the id of a
        question.
    :ivar response: The response attribute classifies the response.
        If the answer to the question is standard, the response is set
        to                 ANSWERED (the default). If, however, the
        answer is exceptional                 (UNKNOWN, NOT_APPLICABLE,
        etc.) then this attribute will be set to                 the
        corresponding exceptional result.
    """
    question_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:question:[1-9][0-9]*",
        }
    )
    response: UserResponseType = field(
        default=UserResponseType.ANSWERED,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class QuestionTextType:
    """
    The QuestionTextType complex type defines a structure to hold the text and
    variables that comprise a question's text.

    :ivar content:
    :ivar sub: Allow the inclusion of arbitrary text contained within a
        variable.
    """
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    sub: List[SubstitutionTextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )


@dataclass
class RangeType:
    """
    The RangeType type defines a structure that specifies a range against which
    a numeric response is to be compared.

    :ivar min: The min element contains a minimum value for the range.
    :ivar max: The max element contains a maximum value for teh range.
    """
    min: Optional[RangeValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    max: Optional[RangeValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )


@dataclass
class ReferenceArtifactValueType(ArtifactValueType):
    """
    The data model that references external artifacts.

    :ivar reference: The reference element contains a URI, which
        is a pointer to the location of an artifact.
    """
    reference: Optional["ReferenceArtifactValueType.Reference"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )

    @dataclass
    class Reference:
        """
        :ivar href: The href attribute specifies a URI
            provided by the user.
        """
        href: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class ReferenceType(TextType):
    """The ReferenceType complex type defines structures used to hold
    information about an external reference given its URI and description.

    This structure may be used to reference other standards such as CVE,
    CCE, or CPE. To do so, the href attribute would give the relevant
    namespace. For example, the namespace of the current version of CPE
    is http://cpe.mitre.org/dictionary/2.0 and the body of this element
    would hold a specific CPE identifier. References to other
    information (documents, web pages, etc.) are also permitted.

    :ivar content:
    :ivar href: The href attribute holds the URI of an external
        reference. This may be the namespace associated with the
        information in the body or a web URL containing relevant
        information.
    """
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SetExpressionChoiceType(SetExpressionBaseType):
    """
    :ivar choice_ref: The choice_ref attribute is a reference to the
        choice                      associated with the question.
    """
    choice_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:choice:[1-9][0-9]*",
        }
    )


@dataclass
class SetExpressionPatternType(SetExpressionBaseType):
    """
    :ivar pattern: The pattern attribute is a string representation
        of the pattern to be matched.
    """
    pattern: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SetExpressionRangeType(SetExpressionBaseType):
    """
    :ivar min: The minimum decimal value of the range (inclusive).
    :ivar max: The maximum decimal value of the range (inclusive).
    """
    min: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    max: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VariableType(ItemBaseType):
    """
    The VariableType type defines structures used to hold a single value.

    :ivar description: The description element holds information
        that describes the value stored on the variable.
    :ivar id: Each item is required to have a unique
        identifier that conforms to the definition of NCName in the
        Recommendation "Namespaces in XML 1.0", i.e., all XML 1.0 names
        that do not contain colons.
    :ivar datatype: The datatype attribute specifies how to treat
        the variable's value. It can be TEXT or
        NUMERIC.
    """
    description: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:variable:[1-9][0-9]*",
        }
    )
    datatype: Optional[VariableDataType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ArtifactValue(ArtifactValueType):
    """
    The artifact_value element contains either a piece of artifact data itself
    or a pointer to it.
    """

    class Meta:
        name = "artifact_value"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class Expression(SetExpressionBaseType):
    """
    The expression element provides a substitution for a variety of expressions
    that can be used to compute a variable value.
    """

    class Meta:
        name = "expression"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class TestAction(ItemBaseType):
    """
    This is a common base element for the question_test_action element.
    """

    class Meta:
        name = "test_action"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class WhenBoolean(SetExpressionBooleanType):
    """The when_boolean element type defines criteria for evaluating the result
    of a boolean question result based on the answer selected.

    If the answer matches, the expression must evaluate to TRUE.
    """

    class Meta:
        name = "when_boolean"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ArtifactsType:
    """
    The ArtifactsType type defines structures containing a set of artifact
    elements.

    :ivar artifact: An artifact element holds information about an
        artifact, which is evidence supporting an answer. Examples
        include                    a file or submitted text.
    """
    artifact: List[ArtifactType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )


@dataclass
class BinaryArtifactValueType(EmbeddedArtifactValueType):
    """
    The data model that holds binary data-based artifacts.

    :ivar data: The data element contains a binary file,
        which was provided as an artifact.
    """
    data: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
            "format": "base64",
        }
    )


@dataclass
class BooleanQuestionResultType(QuestionResultType):
    """
    The BooleanQuestionResultType type defines structures containing a
    reference to a boolean_question, the response, and whether the question was
    successfully posed.

    :ivar answer: The value of the answer to the
        boolean_question. It could either be TRUE or
        FALSE.
    """
    answer: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
            "nillable": True,
        }
    )


@dataclass
class ChoiceQuestionResultType(QuestionResultType):
    """
    The ChoiceQuestionResultType type defines structures containing a reference
    to a choice_question, the response, and whether the question was
    successfully posed.

    :ivar answer: The answer element contains a choice_ref
        attribute that identifies the selected choice.
    """
    answer: Optional[ChoiceAnswerType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
            "nillable": True,
        }
    )


@dataclass
class ConstantVariableType(VariableType):
    """
    The ConstantVariableType type defines structures containing a value defined
    by the author of the document.

    :ivar value: The value element holds the data stored on
        the variable.
    """
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )


@dataclass
class ExternalVariableType(VariableType):
    """
    The ExternalVariableType type defines structures containing a value defined
    elsewhere or some external source.
    """


@dataclass
class LocalVariableType(VariableType):
    """The LocalVariableType type defines structures containing a value
    determined during evaluation. The value is determined based on the answer
    to the linked question. If one or more set elements are present, the value
    is computed based on those set elements.  The value stored in the first set
    element that produces a match pattern is used. If none of the set elements
    have a pattern that matches the response, then an error result is
    generated.

    If no set element is provided, the value used will be the same as
    the answer, with a few exceptions. The mappings are listed below. 1)
    If the question is a boolean question and the variable data type is
    NUMERIC, then the value based on the answer must be 1 for true and 0
    for false. 2) If the question is a boolean question and the variable
    data type is TEXT, then the value is determined by the question's
    model as follows: a) MODEL_YES_NO: the value must be yes if true or
    no if false. b) MODEL_TRUE_FALSE: the value must be true if true or
    false if false. 3) If the question is a choice question, the
    variable data type must be TEXT and the value must be set to the
    text value of the choice. 4) If the question is a numeric question,
    the variable data type must be NUMERIC and the value must be set to
    the value of the answer. 5) If the question is a string question,
    the variable data type must be TEXT and the value must be set to the
    value of the answer. If a local variable is referenced and the value
    cannot be determined, then the referencing question or test action
    should cause an ERROR result to be generated by all referencing test
    actions.

    :ivar set: The set element contains information
        describing how to compute the value to be stored on the
        variable. It holds the patterns, choice_refs, range or boolean
        values to be matched with the answer to the linked question;
        and the appropriate value to be stored on the variable based
        on the match.
    :ivar question_ref: The question_ref attribute holds the unique
        identifier of the question in which the variable is linked.
    """
    set: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    question_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:question:[1-9][0-9]*",
        }
    )


@dataclass
class NumericQuestionResultType(QuestionResultType):
    """
    The NumericQuestionResultType type defines structures containing a
    reference to a numeric_question, the provided response, and whether the
    question was successfully posed.

    :ivar answer: The decimal value of the answer to a
        numeric_question.
    """
    answer: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
            "nillable": True,
        }
    )


@dataclass
class ReferencesType:
    """
    The ReferencesType complex type contains a set of references.

    :ivar reference: The reference element contains information about
        any external references. Examples could include references to
        other                   standards such as CVE, CCE, or CPE.
    """
    reference: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )


@dataclass
class StepType:
    """The StepType complex type defines structures that describe one step (out
    of possibly multiple steps) that a user should take to respond to a
    question.

    The steps would appear as part of the question's instructions
    element.

    :ivar description: The description element contains information
        about this step.
    :ivar reference: The reference element contains information about
        any external references related to this step.
    :ivar step: The step element contains a substep for this
        step.
    :ivar is_done: The is_done attribute indicates whether this step has
        been done. The value is true when it is done. Otherwise, it is
        false.                It is an optional attribute that defaults
        to false.
    :ivar is_required: The is_required attribute indicates whether a
        step is                required or not. If it is not, then it
        can be skipped. It is an                optional attribute that
        defaults to true.
    """
    description: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    reference: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    step: List["StepType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    is_done: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    is_required: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class StringQuestionResultType(QuestionResultType):
    """
    The StringQuestionResultType type defines structures containing a reference
    to a string_question, the string provided in response, and whether the
    question was successfully posed.

    :ivar answer: The string value of the answer to a
        string_question.
    """
    answer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
            "nillable": True,
        }
    )


@dataclass
class SystemTargetType(NamedItemBaseType):
    """
    The SystemTargetType type defines structures containing information about
    the organization it belongs to, a set of ip addresses of computers/networks
    included in the system, descrioption about it, and the roles it performs.

    :ivar organization: The organization element specifies what
        company or institution the system belongs
        to.
    :ivar ipaddress: The ipaddress element holds the ip address of
        a target computer/network. TODO: define an IPv4/v6 address
        pattern
    :ivar description: The description element holds information on
        what the target system is about.
    """
    organization: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    ipaddress: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    description: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )


@dataclass
class TestActionConditionType:
    """The TestActionConditionType complex type specifies processing.

    instructions - either produce a result or move on to another test. The
    TestActionConditionType is extended by all handlers ("when_...") in
    test_actions.

    :ivar result: This element indicates that a final value (i.e.
        PASS, FAIL, ERROR, UNKNOWN, NOT_TESTED, NOT_APPLICABLE) should
        be returned if the encapsulating handler is invoked.
    :ivar test_action_ref: This element indicates that a new test_action
        should be processed if the encapsulating handler is invoked.
    :ivar artifact_refs: The artifact_refs element contains all the
        artifacts                   that must be requested when a
        question, test_action, or                   questionnaire has
        been evaluated.
    """
    result: Optional[ResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    test_action_ref: Optional[TestActionRefType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    artifact_refs: Optional[ArtifactRefsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )


@dataclass
class TextArtifactValueType(EmbeddedArtifactValueType):
    """
    The data model that holds text-based artifacts.

    :ivar data: The data element contains the text of an
        artifact that was provided as a text file or a block of
        text.
    """
    data: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )


@dataclass
class UserType(NamedItemBaseType):
    """
    The UserType type defines structures containing information about a user
    such as name, organization, position, email, and role.

    :ivar organization: The organization element specifies the
        company or institution that the user belongs
        to.
    :ivar position: The position element holds the job title or
        the position of the user within his/her
        organization.
    :ivar email: The email element holds the email address
        where the user can be contacted. TODO: define an email pattern
    """
    organization: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    position: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    email: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )


@dataclass
class QuestionResult(QuestionResultType):
    """A question_result element contains result information associated with a
    specific question.

    The specific type of question_result (boolean_question_result,
    choice_question_result, etc.) depends on the type of the associated
    question (boolean_question, choice_question, etc.)
    """

    class Meta:
        name = "question_result"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ReferenceArtifactValue(ReferenceArtifactValueType):
    """
    The reference_artifact_value element contains a reference to the location
    of an artifact.
    """

    class Meta:
        name = "reference_artifact_value"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class Target(NamedItemBaseType):
    """A target element describes the user, system, or role that applies to all
    questionnaires in scope.

    For instance, specifying that user Joe Smith should complete this
    document; applies to system with ip address of 123.45.67.89; applies
    to all systems functioning as (role) web servers; or all (role)
    administrators should complete this document.
    """

    class Meta:
        name = "target"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class Variable(VariableType):
    """
    A variable element holds information defined by the author, an answer
    value, or values from external sources.
    """

    class Meta:
        name = "variable"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class WhenChoice(SetExpressionChoiceType):
    """The when_choice element type defines criteria for evaluating the result
    of a choice question result based on the answer selected.

    If the choice_ref matches identifier of the selected choice, the
    expression must evaluate to TRUE.
    """

    class Meta:
        name = "when_choice"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class WhenPattern(SetExpressionPatternType):
    """The when_pattern element type defines criteria for evaluating the result
    of a numeric or string question result based on a pattern.

    If the pattern matches, the expression must evaluate to TRUE.
    """

    class Meta:
        name = "when_pattern"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class WhenRange(SetExpressionRangeType):
    """The when_range element type defines criteria for evaluating the result
    of a numeric question result based on the answer selected.

    If the answer is within the range (inclusive), the expression must
    evaluate to TRUE.
    """

    class Meta:
        name = "when_range"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ChoiceTestActionConditionType(TestActionConditionType):
    """
    The ChoiceTestActionConditionType type defines a structure that specifies
    the action to take in a choice_test_action when a particular choice is
    selected in response to a choice_question.

    :ivar choice_ref: The choice_ref element specifies the id of a
        choice.
    """
    choice_ref: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:choice:[1-9][0-9]*",
        }
    )


@dataclass
class CompoundTestActionType(ItemBaseType):
    """
    The CompoundTestActionType type describes the structures used to combine
    multiple test_action elements into a single result.

    :ivar title: The title element contains a descriptive
        heading for the set of test_actions.
    :ivar description: The description element holds information
        describing the set of test_actions.
    :ivar references: The references element holds one or more
        reference elements. Examples could include references to
        other standards, including but not limited to CVE, CCE,
        or CPE.
    :ivar actions: The actions element holds one or more
        test_action elements along with the operators used to combine
        them into a single result.
    """
    title: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    description: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    references: Optional[ReferencesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    actions: Optional[OperationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )


@dataclass
class EqualsTestActionConditionType(TestActionConditionType):
    """
    The EqualsTestActionConditionType defines a structure that specifies the
    action to take in a numeric_test_action when a particular value is given in
    response to a numeric_question.

    :ivar value: Each value holds what is to be matched.
    :ivar var_ref:
    """
    value: List[Decimal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:variable:[1-9][0-9]*",
        }
    )


@dataclass
class GeneratorType:
    """The GeneratorType type defines an element that is used to hold
    information about when a particular OCIL document was generated, what
    version of the schema was used, what tool was used to generate the
    document, and what version of the tool was used.

    Additional generator information is also allowed although it is not
    part of the official OCIL language. Individual organizations can
    place generator information that they feel is important.

    :ivar product_name: The product_name element specifies the name of
        the                   application used to generate the file.
    :ivar product_version: The product_version element specifies the
        version                   of the application used to generate
        the file.
    :ivar author: The author element identifies one of the authors
        of this document.
    :ivar schema_version: The schema_version element specifies the
        version                   of the OCIL schema that the document
        has been written in and that                   should be used
        for validation.
    :ivar timestamp: The timestamp element specifies when the
        particular OCIL document was generated. The format for the
        timestamp is yyyy-mm-ddThh:mm:ss.
    :ivar additional_data: The additional_data element can be used to
        contain metadata                   extensions about the
        generator used to create the OCIL document
        instance.
    """
    product_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    product_version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    author: List[UserType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    schema_version: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )
    additional_data: Optional[ExtensionContainerType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )


@dataclass
class InstructionsType:
    """
    The InstructionsType type defines a series of steps intended to guide the
    user in answering a question.

    :ivar title: The title element contains a descriptive heading
        for the instructions.
    :ivar step: Each step element contains a single step within the
        instructions.
    """
    title: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )
    step: List[StepType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )


@dataclass
class PatternTestActionConditionType(TestActionConditionType):
    """
    The PatternTestActionConditionType type defines a structure that specifies
    the action to take in a string_test_action when a string given in response
    to a string_question matches the given regular expression.

    :ivar pattern: Each pattern element holds a regular
        expression against which the response string is to be
        compared.
    """
    pattern: List[PatternType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )


@dataclass
class QuestionTestActionType(ItemBaseType):
    """The QuestionTestActionType type defines structures that are used to hold
    handlers for non-standard results (UNKNOWN, NOT_TESTED, NOT_APPLICABLE, and
    ERROR) received from a referenced question.

    All children of question_test_action extend this type.

    :ivar title: The title element contains a descriptive
        heading for this set of handlers.
    :ivar when_unknown: The when_unknown element contains processing
        instructions for when the received result is UNKNOWN.
    :ivar when_not_tested: The when_not_tested element contains
        processing instructions for when the received result is
        NOT_TESTED.
    :ivar when_not_applicable: The when_not_applicable element contains
        processing instructions for when the received result is
        NOT_APPLICABLE.
    :ivar when_error: The when_error element contains processing
        instructions for when the received result is ERROR.
    :ivar question_ref: The question_ref attribute contains the id
        value of a question element.
    :ivar id: Each item is required to have a unique
        identifier that conforms to the definition of NCName in the
        Recommendation "Namespaces in XML 1.0", i.e., all XML 1.0 names
        that do not contain colons.
    """
    title: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    when_unknown: Optional[TestActionConditionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    when_not_tested: Optional[TestActionConditionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    when_not_applicable: Optional[TestActionConditionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    when_error: Optional[TestActionConditionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    question_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:question:[1-9][0-9]*",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:testaction:[1-9][0-9]*",
        }
    )


@dataclass
class RangeTestActionConditionType(TestActionConditionType):
    """
    The RangeTestActionConditionType type defines a structure that specifies
    the action to take in a numeric_test_action when a value given in response
    to a numeric_question falls within the indicated range.

    :ivar range: Each range element holds a single numeric
        range.
    """
    range: List[RangeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )


@dataclass
class VariableSetType:
    """The VariableSetType type defines structures containing information
    describing how to compute a variable value.

    It holds the patterns, choice_refs, range, or boolean values to be
    matched; and the appropriate value to be stored on the variable
    based on the match.

    :ivar when_boolean:
    :ivar when_range:
    :ivar when_choice:
    :ivar when_pattern:
    :ivar expression: The expression element provides a substitution for
        a variety                   of expressions that can be used to
        compute a variable value.  Each expression
        must be evaluated in order until one expression matches.  The
        computed value                   of the set is the value of
        first expression that matches.
    """
    when_boolean: List[WhenBoolean] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    when_range: List[WhenRange] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    when_choice: List[WhenChoice] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    when_pattern: List[WhenPattern] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    expression: List[Expression] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )


@dataclass
class BinaryArtifactValue(BinaryArtifactValueType):
    """
    The binary_artifact_value element contains an artifact that was provided as
    a binary file.
    """

    class Meta:
        name = "binary_artifact_value"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class BooleanQuestionResult(BooleanQuestionResultType):
    """
    A boolean_question_result element contains a reference to a
    boolean_question, the response, and whether the question was successfully
    posed.
    """

    class Meta:
        name = "boolean_question_result"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ChoiceQuestionResult(ChoiceQuestionResultType):
    """
    A choice_question_result element contains a reference to a choice_question,
    the response, and whether the question was successfully posed.
    """

    class Meta:
        name = "choice_question_result"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ConstantVariable(ConstantVariableType):
    """
    A constant_variable element holds a value defined by the author of the
    document.
    """

    class Meta:
        name = "constant_variable"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ExternalVariable(ExternalVariableType):
    """
    An external_variable element is a variable defined elsewhere (an external
    source).
    """

    class Meta:
        name = "external_variable"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class LocalVariable(LocalVariableType):
    """A local_variable element holds a value defined during evaluation.

    It will try to match and set the value based on the answer to a
    question.
    """

    class Meta:
        name = "local_variable"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class NumericQuestionResult(NumericQuestionResultType):
    """
    A numeric_question_result element contains a reference to a
    numeric_question, the number provided in response, and whether the question
    was successfully posed.
    """

    class Meta:
        name = "numeric_question_result"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class StringQuestionResult(StringQuestionResultType):
    """
    A string_question_result element contains a reference to a string_question,
    the string provided in response, and whether the question was successfully
    posed.
    """

    class Meta:
        name = "string_question_result"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class System(SystemTargetType):
    """
    The system element contains information about the organization it belongs
    to, a set of ip addresses of computers/networks included in the system,
    description about it, and the roles it performs.
    """

    class Meta:
        name = "system"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class TextArtifactValue(TextArtifactValueType):
    """
    The text_artifact_value element contains an artifact that was provided as a
    text file or a block of text.
    """

    class Meta:
        name = "text_artifact_value"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class User(UserType):
    """
    A user element contains information about a target user such as name,
    organization, position, email, and role.
    """

    class Meta:
        name = "user"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ArtifactResultType:
    """
    The ArtifactResultType type defines structures containing information about
    the submitted artifact, its value, who provided and submitted it, and when
    it was submitted.

    :ivar reference_artifact_value:
    :ivar binary_artifact_value:
    :ivar text_artifact_value:
    :ivar artifact_value: The artifact_value element contains either the
        artifact data                   itself or a pointer to it.
    :ivar provider: The provider element contains information about the
        user or system that provided the artifact.
    :ivar submitter: The submitter element contains information about
        the user who submitted the artifact.
    :ivar artifact_ref: The artifact_ref holds the unique identifier of
        the                artifact object that describes what the
        artifact is about, the type of                data it holds, and
        other metadata.
    :ivar timestamp: The timestamp attribute holds the date and time
        when                the artifact was collected.
    """
    reference_artifact_value: Optional[ReferenceArtifactValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )
    binary_artifact_value: Optional[BinaryArtifactValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )
    text_artifact_value: Optional[TextArtifactValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )
    artifact_value: Optional[ArtifactValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )
    provider: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:user:[1-9][0-9]*|ocil:[A-Za-z0-9_\-\.]+:system:[1-9][0-9]*",
        }
    )
    submitter: Optional[UserType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )
    artifact_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:artifact:[1-9][0-9]*",
        }
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class BooleanQuestionTestActionType(QuestionTestActionType):
    """
    The BooleanQuestionTestActionType type defines a structure that references
    a boolean_question and includes handlers for TRUE (YES) or FALSE (NO)
    responses.

    :ivar when_true: The element when_true specifies the action to
        do when the answer is true.
    :ivar when_false: The element when_false specifies the action
        to do when the answer is false.
    """
    when_true: Optional[TestActionConditionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )
    when_false: Optional[TestActionConditionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )


@dataclass
class ChoiceQuestionTestActionType(QuestionTestActionType):
    """
    The ChoiceQuestionTestActionType type defines a structure that references a
    choice_question and includes handlers for the various choices set out in
    the choice_question.

    :ivar when_choice: Specifies the action to perform when the
        indicated choice is selected.
    """
    when_choice: List[ChoiceTestActionConditionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )


@dataclass
class NumericQuestionTestActionType(QuestionTestActionType):
    """
    The NumericQuestionTestActionType type defines a structure that references
    a numeric_question and includes handlers that indicate actions to perform
    based on whether the response matches a particular value or falls within a
    particular range.

    :ivar when_equals: This element holds information on what to
        do when the answer matches the specified value.
    :ivar when_range: This element holds information on what to
        do when the answer is within a specified range of values.
    """
    when_equals: List[EqualsTestActionConditionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    when_range: List[RangeTestActionConditionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )


@dataclass
class QuestionResultsType:
    """
    The QuestionResultsType type defines structures containing computed results
    of all evaluated question types.

    :ivar string_question_result:
    :ivar numeric_question_result:
    :ivar choice_question_result:
    :ivar boolean_question_result:
    :ivar question_result: A question_result element contains result
        information associated with a specific question. The specific
        type                   of question_result
        (boolean_question_result,
        choice_question_result, etc.) depends on the type of the
        associated                   question (boolean_question,
        choice_question, etc.)
    """
    string_question_result: List[StringQuestionResult] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    numeric_question_result: List[NumericQuestionResult] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    choice_question_result: List[ChoiceQuestionResult] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    boolean_question_result: List[BooleanQuestionResult] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    question_result: List[QuestionResult] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )


@dataclass
class QuestionType(ItemBaseType):
    """
    The QuestionType complex type defines a structure to describe a question
    and any instructions to help in determining an answer.

    :ivar question_text: The question_text element provides the text of
        the question to pose.
    :ivar instructions: An optional instructions element may be
        included to hold additional instructions to assist the user
        in determining the answer to the question.
    :ivar id: Each item is required to have a unique
        identifier that conforms to the definition of NCName in the
        Recommendation "Namespaces in XML 1.0", i.e., all XML 1.0 names
        that do not contain colons.
    """
    question_text: List[QuestionTextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    instructions: Optional[InstructionsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:question:[1-9][0-9]*",
        }
    )


@dataclass
class QuestionnaireType(CompoundTestActionType):
    """The QuestionnaireType type defines a structure that represents a
    specific question or set of questions that evaluate to a single result.

    A questionnaire may contain multiple test_actions. test_actions may
    be nested and aggregated through an acceptable operation to produce
    the result of a check.

    :ivar id: Each questionnaire is required to have a unique
        identifier that conforms to the definition of NCName in the
        Recommendation "Namespaces in XML 1.0", i.e., all XML 1.0 names
        that do not contain colons.
    :ivar child_only: This attribute specifies whether or not this
        questionnaire should only appear as a child of another
        questionnaire. All questionnaires must be defined within the
        body of the ocil element and, by default, interpreters might
        simply grab all questionnaires and evaluate them. However,
        questionnaires can reference other questionnaires through a
        test_action_ref. If an author references a questionnaire in
        this way, they may not wish that the questionnaire be
        evaluated except as a child of another questionnaire. By
        setting the child_only attribute to true, the author is
        indicating that the given questionnaire should not be a
        "top-level" questionnaire but should instead only be
        evaluated as the child of another questionnaire.
    """
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:questionnaire:[1-9][0-9]*",
        }
    )
    child_only: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class StringQuestionTestActionType(QuestionTestActionType):
    """
    The StringQuestionTestActionType type defines a structure that references a
    string_question and includes handlers that indicate actions to perform
    based on whether the response matches a given regular expression.

    :ivar when_pattern: This element holds information on what to do
        when the answer matches a specified regular expression
        pattern.
    """
    when_pattern: List[PatternTestActionConditionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )


@dataclass
class TargetsType:
    """
    The TargetsType type defines structures containing a set of target
    elements.

    :ivar system:
    :ivar user:
    :ivar target: A target element describes the user, system, or
        role that applies to all questionnaires in scope. For instance,
        specifying that user Joe Smith should complete this document;
        applies to system with ip address of 123.45.67.89; applies to
        all                   systems functioning as (role) web servers;
        or all (role)                   administrators should complete
        this document.
    """
    system: List[System] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    user: List[User] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    target: List[Target] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )


@dataclass
class VariablesType:
    """
    The VariablesType type defines structures containing a set of variables.

    :ivar external_variable:
    :ivar local_variable:
    :ivar constant_variable:
    :ivar variable: A variable element holds a value defined by the
        author, a value based on a question's answer, or a value from an
        external source.
    """
    external_variable: List[ExternalVariable] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    local_variable: List[LocalVariable] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    constant_variable: List[ConstantVariable] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    variable: List[Variable] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )


@dataclass
class QuestionTestAction(QuestionTestActionType):
    """The question_test_action element contains a reference to a single
    question along with a set of handlers that indicate how processing should
    proceed based on the answer provided.

    This element is abstract and is implemented in a document as a
    boolean_question_test_action, choice_question_test_action,
    numeric_question_test_action, or string_question_test_action. The
    type of question_test_action must match the type of question
    referenced (e.g. a boolean_question_test_action MUST reference a
    boolean_question.)
    """

    class Meta:
        name = "question_test_action"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ArtifactResultsType:
    """
    The ArtifactResultsType type defines structures containing a set of
    artifact_result elements.

    :ivar artifact_result: The artifact_result element contains an
        artifact,                   its value, who submitted it, and who
        provided                   it.
    """
    artifact_result: List[ArtifactResultType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )


@dataclass
class BooleanQuestionType(QuestionType):
    """
    The BooleanQuestionType type defines a question with valid responses of
    either {TRUE, FALSE} or {YES, NO}.

    :ivar default_answer: The default_answer attribute specifies the
        default value of the boolean_question. Its value may be set to
        true or false.
    :ivar model: The model attribute specifies whether the
        response should be from the set {True, False} or the set
        {YES, NO}. If the value of this attribute is not set, then
        it defaults to MODEL_YES_NO (i.e. response can either be
        YES or NO).
    """
    default_answer: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    model: BooleanQuestionModelType = field(
        default=BooleanQuestionModelType.MODEL_YES_NO,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ChoiceQuestionType(QuestionType):
    """The ChoiceQuestionType type defines a question with one or more
    acceptable answers specified by the author.

    The response will be one of these specified answers. Acceptable
    answers are specified either explicitly using the choice element or
    implicitly using the choice_group_ref element to reference a
    choice_group element. Choices are presented in the order in which
    they are provided. All the choices in a choice_group are inserted in
    the order in which they appear within the choice_group.

    :ivar choice: Holds the information associated with one of
        the possible responses to this choice_question.
    :ivar choice_group_ref: Holds a reference to a choice_group. The
        questions described in this choice group are used as possible
        responses for this choice_question.
    :ivar default_answer_ref: The default_answer_ref specifies the
        choice id                      of the default answer to the
        question.
    """
    choice: List[ChoiceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    choice_group_ref: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:choicegroup:[1-9][0-9]*",
        }
    )
    default_answer_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:choice:[1-9][0-9]*",
        }
    )


@dataclass
class NumericQuestionType(QuestionType):
    """The NumericQuestionType type defines a question that requires a numeric
    answer.

    Acceptable values may be positive or negative and may include
    decimals.

    :ivar default_answer: An optional default value may be specified as
        the answer.
    """
    default_answer: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class QuestionnairesType:
    """
    The QuestionnairesType type defines a container for a set of questionnaire
    elements.

    :ivar questionnaire: A questionnaire contains a set of questions
        that                   determines compliance with a check. Each
        questionnaire returns a                   value based on the
        responses to the various questions that it
        references. Each questionnaire acting as top-level should
        represent                    a single compliance check, such as
        might be referenced by an XCCDF                   Rule.
    """
    questionnaire: List[QuestionnaireType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )


@dataclass
class StringQuestionType(QuestionType):
    """
    The StringQuestionType type defines a question that requires a string
    answer.

    :ivar default_answer: An optional default value may be specified as
        the answer.
    """
    default_answer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class BooleanQuestionTestAction(BooleanQuestionTestActionType):
    """
    A boolean_question_test_action element references a boolean_question and
    includes handlers for TRUE (YES) or FALSE (NO) responses.
    """

    class Meta:
        name = "boolean_question_test_action"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ChoiceQuestionTestAction(ChoiceQuestionTestActionType):
    """
    A choice_question_test_action element references a choice_question and
    includes handlers for the various choices set out in the choice_question.
    """

    class Meta:
        name = "choice_question_test_action"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class NumericQuestionTestAction(NumericQuestionTestActionType):
    """
    A numeric_question_test_action element references a numeric_question and
    includes handlers that indicate actions to perform based on whether the
    response matches a particular value or falls within a particular range.
    """

    class Meta:
        name = "numeric_question_test_action"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class Question(QuestionType):
    """A question element contains information for one question that needs to
    be answered.

    It can be a boolean_question, choice_question, numeric_question, or
    string_question depending on the set of acceptable answers.
    """

    class Meta:
        name = "question"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class StringQuestionTestAction(StringQuestionTestActionType):
    """
    A string_question_test_action element references a string_question and
    includes handlers that indicate actions to perform based on whether the
    response matches a given regular expression.
    """

    class Meta:
        name = "string_question_test_action"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class QuestionnaireResultType:
    """
    The QuestionnaireResultType type defines structures containing the computed
    result, associated artifacts and targets of a particular questionnaire.

    :ivar artifact_results: The artifact_results element contains a set
        of                   retrieved artifacts.
    :ivar questionnaire_ref: The questionnaire_ref attribute identifies
        a                particular questionnaire using its id.
    :ivar result: The result attribute holds the result of evaluating
        the specified questionnaire.
    """
    artifact_results: Optional[ArtifactResultsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    questionnaire_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:questionnaire:[1-9][0-9]*",
        }
    )
    result: Optional[ResultType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TestActionResultType:
    """The TestActionResultType type defines structures containing all computed
    results of a TestActionType.

    One of these elements will appear for each test_action evaluated.

    :ivar artifact_results: The artifact_results element contains a set
        of                   retrieved artifacts.
    :ivar test_action_ref: The test_action_ref attribute identifies a
        specific                test_action using its id.
    :ivar result: The result attribute holds the result of evaluating
        the specified test_action specified.
    """
    artifact_results: Optional[ArtifactResultsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    test_action_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"ocil:[A-Za-z0-9_\-\.]+:testaction:[1-9][0-9]*|ocil:[A-Za-z0-9_\-\.]+:questionnaire:[1-9][0-9]*",
        }
    )
    result: Optional[ResultType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TestActionsType:
    """
    The TestActionsType type defines a container for a set of test action
    elements.

    :ivar string_question_test_action:
    :ivar numeric_question_test_action:
    :ivar choice_question_test_action:
    :ivar boolean_question_test_action:
    :ivar question_test_action:
    :ivar test_action: The test_action element contains information
        about                   what action to take based on the answer
        to a referenced question                   element within a
        questionnaire. It can be a compound_test_action,
        boolean_question_test_action, choice_question_test_action,
        numeric_question_test_action, or string_question_test_action.
    """
    string_question_test_action: List[StringQuestionTestAction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    numeric_question_test_action: List[NumericQuestionTestAction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    choice_question_test_action: List[ChoiceQuestionTestAction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    boolean_question_test_action: List[BooleanQuestionTestAction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    question_test_action: List[QuestionTestAction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    test_action: List[TestAction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )


@dataclass
class BooleanQuestion(BooleanQuestionType):
    """
    A boolean_question is a type of question element with valid responses of
    either {TRUE, FALSE} or {YES, NO}.
    """

    class Meta:
        name = "boolean_question"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class ChoiceQuestion(ChoiceQuestionType):
    """A choice_question is a type of question element with one or more
    acceptable answers specified by the author.

    One of these specified answers will be given as the response.
    Acceptable answers are specified either explicitly using the choice
    element or implicitly using the choice_group_ref element to
    reference a choice_group element. Choices are presented in the order
    in which they are provided. All the choices in a choice_group are
    inserted in the order in which they appear within the choice_group.
    """

    class Meta:
        name = "choice_question"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class NumericQuestion(NumericQuestionType):
    """A numeric_question is a type of question element that requires a numeric
    answer.

    Acceptable values may be positive or negative and may include
    decimals.
    """

    class Meta:
        name = "numeric_question"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class StringQuestion(StringQuestionType):
    """
    A string_question is a type of question element that requires a string
    answer.
    """

    class Meta:
        name = "string_question"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class QuestionnaireResultsType:
    """
    The QuestionnaireResultsType type defines structures containing computed
    results of all the evaluated questionnaires.

    :ivar questionnaire_result: The questionnaire_result element
        contains                   information about the result of a
        particular questionnaire.
    """
    questionnaire_result: List[QuestionnaireResultType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )


@dataclass
class QuestionsType:
    """
    The QuestionsType type defines structures containing a set of QuestionType
    and ChoiceGroupType elements.

    :ivar string_question:
    :ivar numeric_question:
    :ivar choice_question:
    :ivar boolean_question:
    :ivar question: The question element contains information for a
        single question to be answered. Based on the data type of
        acceptable answers to the question, it can be a
        boolean_question,                   choice_question,
        numeric_question, or string_question.
    :ivar choice_group: Holds choice groups which represent possible
        sets                   of choices for choice_questions.
        Choice_groups may be reused across                   multiple
        choice_questions.
    """
    string_question: List[StringQuestion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    numeric_question: List[NumericQuestion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    choice_question: List[ChoiceQuestion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    boolean_question: List[BooleanQuestion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    question: List[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )
    choice_group: List[ChoiceGroupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )


@dataclass
class TestActionResultsType:
    """
    The TestActionResultsType type defines structures containing computed
    results of all the evaluated test action types.

    :ivar test_action_result: The test_action_result element contains
        the result                   of a test_action evaluation. One of
        these elements will appear for                   each
        test_action evaluated.
    """
    test_action_result: List[TestActionResultType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "min_occurs": 1,
        }
    )


@dataclass
class ResultsType:
    """
    The ResultsType type defines structures containing results from
    questionnaires, test actions, questions, artifacts, and metadata about the
    start/end time of evaluation, any targets, and a short caption or title.

    :ivar title: The title element contains a descriptive heading or
        caption describing the result set.
    :ivar questionnaire_results: The questionnare_results element
        contains computed                   results of all the evaluated
        questionnaires.
    :ivar test_action_results: The test_action_results element contains
        computed                   results of all the evaluated
        test_action types.
    :ivar question_results: The question_results element contains
        computed                   results of all evaluated question
        types.
    :ivar artifact_results: The artifact_results element contains all
        artifacts                   that have been retrieved during
        evaluation. Scope is the entire                   document.
    :ivar targets: The targets element contains all the actual target
        users, systems, and roles for which the OCIL document has been
        applied.
    :ivar start_time: The start_time attribute is an optional attribute
        that                specifies when the evaluation of this OCIL
        file started.
    :ivar end_time: The end_time attribute is an optional attribute that
        specifies when the evaluation of this OCIL file ended.
    """
    title: Optional[TextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    questionnaire_results: Optional[QuestionnaireResultsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    test_action_results: Optional[TestActionResultsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    question_results: Optional[QuestionResultsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    artifact_results: Optional[ArtifactResultsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    targets: Optional[TargetsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Ociltype:
    """
    The OCILType represents the primary content model for the OCIL.

    :ivar generator: The generator element contains information
        related to the generation of the file. Specifically, a generator
        contains information about the application used to create the
        file, when it was created, and the schema to use to validate
        it.
    :ivar document: This element contains document-level information,
        including title, descriptions, and notices.
    :ivar questionnaires: The questionnaires element contains all the
        questionnaire constructs defined within the document.
    :ivar test_actions: The test_actions element contains all the
        boolean, choice, string, and numeric test actions defined within
        the document.
    :ivar questions: The questions element contains all the boolean,
        choice, string, and numeric questions, and any other supporting
        elements (e.g. choice group) defined within the
        document.
    :ivar artifacts: The artifacts element contains all the artifact
        constructs to be retrieved (as necessary) during
        evaluation.
    :ivar variables: The variables element contains all the constant,
        local, and external variables available to be used within the
        document.
    :ivar results: The results element contains the results of an
        evaluation of the OCIL file. This includes records of all
        questionnaire results, question results, and test_action
        results.
    """

    class Meta:
        name = "OCILType"

    generator: Optional[GeneratorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )
    document: Optional[DocumentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    questionnaires: Optional[QuestionnairesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )
    test_actions: Optional[TestActionsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )
    questions: Optional[QuestionsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
            "required": True,
        }
    )
    artifacts: Optional[ArtifactsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    variables: Optional[VariablesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )
    results: Optional[ResultsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        }
    )


@dataclass
class Ocil(Ociltype):
    """The ocil element is the root XML element of an OCIL document.

    It contains information about one or more questionnaires. It may
    also contain results elements to store prior responses.
    """

    class Meta:
        name = "ocil"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"

    @classmethod
    def load(cls, file):
        with open(file, "rb") as fp:
            benchmark = scap_parser.parse(fp, cls)
        return benchmark

    @classmethod
    def load_json(cls, file):
        with open(file, "rb") as fp:
            benchmark = scap_json_parser.parse(fp, cls)
        return benchmark

    def dump(self, file):
        with open(file, "w", encoding="utf8") as fp:
            scap_serializer.write(fp, self)

    def dump_json(self, file):
        with open(file, "w", encoding="utf8") as fp:
            scap_json_serializer.write(fp, self)
