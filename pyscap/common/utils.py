from pathlib import Path

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser, JsonParser
from xsdata.formats.dataclass.serializers import XmlSerializer, JsonSerializer

scap_context = XmlContext()
scap_parser = XmlParser(context=scap_context)
scap_json_parser = JsonParser(context=scap_context)
scap_serializer = XmlSerializer(context=scap_context)
scap_json_serializer = JsonSerializer(context=scap_context)


class ParsableElement:

    @classmethod
    def parse(cls, data, data_format="xml"):
        if data_format == "xml":
            parser = scap_parser
        elif data_format == "json":
            parser = scap_json_parser
        else:
            raise ValueError

        if isinstance(data, bytes):
            return parser.from_bytes(data, cls)
        else:
            return parser.from_path(Path(data))

    def write(self, file, data_format="xml"):
        if data_format == "xml":
            serializer = scap_serializer
        elif data_format == "json":
            serializer = scap_json_serializer
        else:
            raise ValueError

        with open(file, "w", encoding="utf8") as fp:
            serializer.write(fp, self)
