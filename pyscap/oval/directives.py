from dataclasses import dataclass, field
from typing import List, Optional

from .common import GeneratorType
from .namespaces import OVAL_NAMESPACE_MAP
from .results import ClassDirectivesType, DefaultDirectivesType
from ..common.utils import scap_parser, scap_json_parser, scap_serializer, scap_json_serializer
from ..common.xmldsig import Signature


@dataclass
class OvalDirectives:
    """The oval_directives element is the root of an OVAL Directive Document.

    Its purpose is to bind together the generator and the set of
    directives contained in the document. The generator section must be
    present and provides information about when the directives document
    was compiled and under what version. The optional Signature element
    allows an XML Signature as defined by the W3C to be attached to the
    document. This allows authentication and data integrity to be
    provided to the user. Enveloped signatures are supported. More
    information about the official W3C Recommendation regarding XML
    digital signatures can be found at http://www.w3.org/TR/xmldsig-
    core/.

    :ivar generator: The required generator section provides information
        about when the directives document was compiled and under what
        version.
    :ivar directives: The required directives section presents flags
        describing what information must be been included in an oval
        results document. This element represents the default set of
        directives. These directives apply to all classes of definitions
        for which there is not a class specific set of directives.
    :ivar class_directives: The optional class_directives section
        presents flags describing what information has been included in
        the results document for a specific OVAL Definition class. The
        directives for a particlar class override the default
        directives.
    :ivar signature: The optional Signature element allows an XML
        Signature as defined by the W3C to be attached to the document.
        This allows authentication and data integrity to be provided to
        the user. Enveloped signatures are supported. More information
        about the official W3C Recommendation regarding XML digital
        signatures can be found at http://www.w3.org/TR/xmldsig-core/.
    """

    class Meta:
        name = "oval_directives"
        namespace = "http://oval.mitre.org/XMLSchema/oval-directives-5"

    generator: Optional[GeneratorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    directives: Optional[DefaultDirectivesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    class_directives: List[ClassDirectivesType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
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
            directives = scap_parser.parse(fp, cls)
        return directives

    @classmethod
    def load_json(cls, file):
        with open(file, "rb") as fp:
            directives = scap_json_parser.parse(fp, cls)
        return directives

    def dump(self, file):
        with open(file, "w", encoding="utf8") as fp:
            scap_serializer.write(fp, self, ns_map=OVAL_NAMESPACE_MAP)

    def dump_json(self, file):
        with open(file, "w", encoding="utf8") as fp:
            scap_json_serializer.write(fp, self, ns_map=OVAL_NAMESPACE_MAP)
