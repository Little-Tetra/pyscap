from ..common.namespaces import (
    DC_NAMESPACE,
    DSIG_NAMESPACE,
    XML_NAMESPACE,
    XSD_NAMESPACE,
    XSI_NAMESPACE,
)

CPE2_NAMESPACE = "http://cpe.mitre.org/language/2.0"
CPE2_DICT_NAMESPACE = "http://cpe.mitre.org/dictionary/2.0"

XCCDF_NAMESPACE = "http://checklists.nist.gov/xccdf/1.2"

XCCDF_NAMESPACE_MAP = {
    "cpe2": CPE2_NAMESPACE,
    "cpe2-dict": CPE2_DICT_NAMESPACE,
    "dc": DC_NAMESPACE,
    "dsig": DSIG_NAMESPACE,
    "xccdf": XCCDF_NAMESPACE,
    "xml": XML_NAMESPACE,
    "xsd": XSD_NAMESPACE,
    "xsi": XSI_NAMESPACE
}
