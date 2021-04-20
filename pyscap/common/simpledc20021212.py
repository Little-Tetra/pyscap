from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://purl.org/dc/elements/1.1/"


@dataclass
class ElementType:
    class Meta:
        name = "elementType"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Contributor(ElementType):
    class Meta:
        name = "contributor"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Coverage(ElementType):
    class Meta:
        name = "coverage"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Creator(ElementType):
    class Meta:
        name = "creator"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Date(ElementType):
    class Meta:
        name = "date"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Description(ElementType):
    class Meta:
        name = "description"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Format(ElementType):
    class Meta:
        name = "format"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Identifier(ElementType):
    class Meta:
        name = "identifier"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Language(ElementType):
    class Meta:
        name = "language"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Publisher(ElementType):
    class Meta:
        name = "publisher"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Relation(ElementType):
    class Meta:
        name = "relation"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Rights(ElementType):
    class Meta:
        name = "rights"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Source(ElementType):
    class Meta:
        name = "source"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Subject(ElementType):
    class Meta:
        name = "subject"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Title(ElementType):
    class Meta:
        name = "title"
        namespace = "http://purl.org/dc/elements/1.1/"


@dataclass
class Type(ElementType):
    class Meta:
        name = "type"
        namespace = "http://purl.org/dc/elements/1.1/"
