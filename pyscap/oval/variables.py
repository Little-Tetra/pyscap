from dataclasses import dataclass, field
from typing import List, Optional

from .common import (
    GeneratorType,
    NotesType,
    SimpleDatatypeEnumeration,
)
from ..common.utils import scap_json_parser, scap_serializer, scap_json_serializer, scap_parser
from ..common.xmldsig import Signature

OVAL_VARIABLES_5_NAMESPACE = "http://oval.mitre.org/XMLSchema/oval-variables-5"


@dataclass
class VariableType:
    """Each variable element contains the associated datatype and value which
    will be substituted into the OVAL Definition that is referencing this
    specific variable.

    The notes section of a variable should be used to hold information
    that might be helpful to someone examining the technical aspects of
    the variable. Please refer to the description of the NotesType
    complex type for more information about the notes element.

    :ivar value:
    :ivar notes:
    :ivar id:
    :ivar datatype: Note that the 'record' datatype is not permitted on
        variables.
    :ivar instance: Use to specify multiple variable instances.
    :ivar comment:
    """
    value: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    notes: Optional[NotesType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:var:[1-9][0-9]*",
        }
    )
    datatype: Optional[SimpleDatatypeEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    instance: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class VariablesType:
    """The VariablesType complex type is a container for one or more variable
    elements.

    Each variable element holds the value of an external variable used
    in an OVAL Definition. Please refer to the description of the
    VariableType for more information about an individual variable.
    """
    variable: List[VariableType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class OvalVariables:
    """The oval_variables element is the root of an OVAL Variable Document.

    Its purpose is to bind together the different variables contained in
    the document. The generator section must be present and provides
    information about when the variable file was compiled and under what
    version. The optional Signature element allows an XML Signature as
    defined by the W3C to be attached to the document. This allows
    authentication and data integrity to be provided to the user.
    Enveloped signatures are supported. More information about the
    official W3C Recommendation regarding XML digital signatures can be
    found at http://www.w3.org/TR/xmldsig-core/.
    """

    class Meta:
        name = "oval_variables"
        namespace = OVAL_VARIABLES_5_NAMESPACE

    generator: Optional[GeneratorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    variables: Optional[VariablesType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )

    @classmethod
    def load(cls, file):
        with open(file, "rb") as fp:
            variables = scap_parser.parse(fp, cls)
        return variables

    @classmethod
    def load_json(cls, file):
        with open(file, "rb") as fp:
            variables = scap_json_parser.parse(fp, cls)
        return variables

    def dump(self, file):
        with open(file, "w", encoding="utf8") as fp:
            scap_serializer.write(fp, self)

    def dump_json(self, file):
        with open(file, "w", encoding="utf8") as fp:
            scap_json_serializer.write(fp, self)
