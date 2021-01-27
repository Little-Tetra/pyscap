from ..common.namespaces import (
    DC_NAMESPACE,
    DSIG_NAMESPACE,
    XML_NAMESPACE,
    XSD_NAMESPACE,
    XSI_NAMESPACE,
)
from ..cpe import CPE_LANGUAGE_2_NAMESPACE, CPE_DICTIONARY_2_NAMESPACE

XCCDF_NAMESPACE = "http://checklists.nist.gov/xccdf/1.2"

XCCDF_NAMESPACE_MAP = {
    "cpe2": CPE_LANGUAGE_2_NAMESPACE,
    "cpe2-dict": CPE_DICTIONARY_2_NAMESPACE,
    "dc": DC_NAMESPACE,
    "dsig": DSIG_NAMESPACE,
    "xccdf": XCCDF_NAMESPACE,
    "xml": XML_NAMESPACE,
    "xsd": XSD_NAMESPACE,
    "xsi": XSI_NAMESPACE
}
