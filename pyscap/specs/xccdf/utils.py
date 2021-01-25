from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser, JsonParser
from xsdata.formats.dataclass.serializers import XmlSerializer, JsonSerializer

from .cpe_language_2_3 import __NAMESPACE__ as CPE_LANGUAGE_2_3_NAMESPACE
from .xccdf_1_2 import __NAMESPACE__ as XCCDF_1_2_NAMESPACE, Benchmark
from ...common.namespaces import HTML_NAMESPACE, XHTML_NAMESPACE, DC_NAMESPACE

context = XmlContext()
parser = XmlParser(context=context)
json_parser = JsonParser(context=context)
serializer = XmlSerializer(context=context)
json_serializer = JsonSerializer(context=context)

xccdf_ns_map = {
    None: XCCDF_1_2_NAMESPACE,
    "cpe2": CPE_LANGUAGE_2_3_NAMESPACE,
    "html": HTML_NAMESPACE,
    "xhtml": XHTML_NAMESPACE,
    "dc": DC_NAMESPACE
}


def load(file):
    with open(file, "rb") as fp:
        benchmark = parser.parse(fp, Benchmark)
    return benchmark


def dump(benchmark: Benchmark, file):
    with open(file, "w", encoding="utf8") as fp:
        serializer.write(fp, benchmark, ns_map=xccdf_ns_map)


def load_json(file):
    with open(file, "rb") as fp:
        benchmark = json_parser.parse(fp, Benchmark)
    return benchmark


def dump_json(benchmark: Benchmark, file):
    with open(file, "w", encoding="utf8") as fp:
        json_serializer.write(fp, benchmark)
