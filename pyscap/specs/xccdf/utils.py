from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from .core import Benchmark
from .namespaces import XCCDF_NAMESPACE
from ..cpe import CPE_NAMESPACE
from ...common.namespaces import HTML_NAMESPACE, XHTML_NAMESPACE, DC_NAMESPACE

context = XmlContext()
parser = XmlParser(context=context)
serializer = XmlSerializer(context=context)

xccdf_ns_map = {
    None: XCCDF_NAMESPACE,
    "cpe2": CPE_NAMESPACE,
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
