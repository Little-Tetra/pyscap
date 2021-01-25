from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser, JsonParser
from xsdata.formats.dataclass.serializers import XmlSerializer, JsonSerializer

from .namespaces import XCCDF_NAMESPACE_MAP
from .xccdf_1_2 import Benchmark

xccdf_context = XmlContext()
xccdf_parser = XmlParser(context=xccdf_context)
xccdf_json_parser = JsonParser(context=xccdf_context)
xccdf_serializer = XmlSerializer(context=xccdf_context)
xccdf_json_serializer = JsonSerializer(context=xccdf_context)


def load(file):
    with open(file, "rb") as fp:
        benchmark = xccdf_parser.parse(fp, Benchmark)
    return benchmark


def load_json(file):
    with open(file, "rb") as fp:
        benchmark = xccdf_json_parser.parse(fp, Benchmark)
    return benchmark


def dump(benchmark: Benchmark, file):
    with open(file, "w", encoding="utf8") as fp:
        xccdf_serializer.write(fp, benchmark, ns_map=XCCDF_NAMESPACE_MAP)


def dump_json(benchmark: Benchmark, file):
    with open(file, "w", encoding="utf8") as fp:
        xccdf_json_serializer.write(fp, benchmark)
