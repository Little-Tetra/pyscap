from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser, JsonParser
from xsdata.formats.dataclass.serializers import XmlSerializer, JsonSerializer

scap_context = XmlContext()
scap_parser = XmlParser(context=scap_context)
scap_json_parser = JsonParser(context=scap_context)
scap_serializer = XmlSerializer(context=scap_context)
scap_json_serializer = JsonSerializer(context=scap_context)
