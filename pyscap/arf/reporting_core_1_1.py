from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional
from xml.etree.ElementTree import QName


class RelationshipTypeScope(Enum):
    INCLUSIVE = "inclusive"
    EXCLUSIVE = "exclusive"


@dataclass
class RelationshipType:
    """The relationship-type encapsulates a complete relationship from a
    subject to one or more objects.

    It is the responsibility of the XML Schema adopting this type to
    implement the necessary id/idref instances to ensure that @subject
    and ref refer to valid elements.

    :ivar ref: Must contain the ID of the object of the relationship
        being established. The                         implementing XML
        Schema of relationship-type SHOULD implement the necessary
        id/idref constructs                         to ensure a valid
        reference is constructed.
    :ivar type: Specifies the type of relationship (predicate) being
        defined between the subject and                     the object
        of the relationship. The value is a QName that should reference
        a term in a controlled                     vocabulary which is
        understood by both the producing and consuming parties.
    :ivar scope: Indicates how multiple &lt;ref&gt; elements should be
        interpreted in this                     relationship. If
        "inclusive" is specified, then the relationship being defined is
        between the                     subject and the collection of
        objects indicated by the &lt;ref&gt; elements (i.e. the
        relationship is not necessarily relevant for any one particular
        object being referenced, but for the
        collection of objects referenced). If "exclusive" is specified,
        then the relationship being defined                     is
        between the content payload and each object individually (i.e.
        this is the same as specifying                     multiple
        relationship elements, each with the same @type and subject).
    :ivar subject: Must contain the ID of the subject of the
        relationship being established. The
        implementing XML Schema of relationship-type SHOULD implement
        the necessary id/idref constructs to                     ensure
        a valid reference is constructed.
    :ivar other_attributes: A placeholder so that content creators can
        add attributes as                     desired.
    """

    class Meta:
        name = "relationship-type"

    ref: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "namespace": "http://scap.nist.gov/schema/reporting-core/1.1"
        }
    )
    type: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    scope: RelationshipTypeScope = field(
        default=RelationshipTypeScope.INCLUSIVE,
        metadata={
            "type": "Attribute",
        }
    )
    subject: Optional[str] = field(
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
class RelationshipsContainerType:
    """
    :ivar relationships: Contains a collection of relationship elements.
    """

    class Meta:
        name = "relationships-container-type"

    relationships: Optional["RelationshipsContainerType.Relationships"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/reporting-core/1.1"
        }
    )

    @dataclass
    class Relationships:
        relationship: List[RelationshipType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
                "namespace": "http://scap.nist.gov/schema/reporting-core/1.1"
            }
        )
