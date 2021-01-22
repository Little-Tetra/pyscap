from dataclasses import dataclass, field
from typing import Optional


# Supporting types

@dataclass
class TextType:
    """
    This type allows the xml:lang attribute to associate a specific language
    with an element's string content.
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
