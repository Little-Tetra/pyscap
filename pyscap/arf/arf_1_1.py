from dataclasses import dataclass, field
from typing import Dict, List, Optional

from xsdata.models.datatype import XmlDate

from .ai_1_1 import (
    Asset as AiAsset,
    Circuit,
    ComputingDevice,
    Data,
    Database,
    ItAsset,
    Network,
    Organization,
    Person,
    Service,
    Software,
    System,
    Website,
)
from .reporting_core_1_1 import RelationshipsContainerType
from ..common.utils import ParsableElement
from ..common.xlink import TypeType
from ..oval import OvalResults, OVAL_RESULTS_5_NAMESPACE
from ..sds import DataStreamCollection, SDS_1_2_NAMESPACE
from ..xccdf import TestResult, XCCDF_1_2_NAMESPACE
from ..xccdf.xccdf_1_1 import TestResult as TestResult_1_1, XCCDF_1_1_NAMESPACE

ARF_1_1_NAMESPACE = "http://scap.nist.gov/schema/asset-reporting-format/1.1"


@dataclass
class ObjectRef:
    """

    Report creators can embedding this element in a report with the @ref_id referencing the ID of an asset, report,
    or report request. This element effectively acts as a pointer, allowing content produces to reference higher
    level ARF constructs in a report, without duplicating the data in that ARF construct.
    """

    class Meta:
        name = "object-ref"
        namespace = ARF_1_1_NAMESPACE

    ref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ref-id",
            "type": "Attribute",
        }
    )


@dataclass
class RemoteResource:
    """

    Links to content stored external to this report.

    :ivar type: Fixed as a simple XLink.
    :ivar href: A URI to the remote content. Producers and consumers should both know how to resolve the URI in order to be interoperable.
    :ivar other_attributes: A placeholder so that content creators can add attributes as desired.
    """

    class Meta:
        name = "remote-resource"
        namespace = ARF_1_1_NAMESPACE

    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class ReportRequestContent:
    """

    :ivar other_element: Holds the content of a report request.
    :ivar other_attributes: A placeholder so that content creators can add attributes as desired.
    """
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "data-stream-collection",
                    "type": DataStreamCollection,
                    "namespace": SDS_1_2_NAMESPACE
                },
                {
                    "type": object,
                    "namespace": "##other",
                    "wildcard": True
                }
            ),
            "required": True,
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class ReportRequest:
    """

    :ivar content: Contains the content of the report request.
    :ivar remote_resource:
    :ivar id: An internal ID to identify this report request.
    :ivar other_attributes: A placeholder so that content creators can add attributes as desired.
    """

    content: Optional[ReportRequestContent] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    remote_resource: Optional[RemoteResource] = field(
        default=None,
        metadata={
            "name": "remote-resource",
            "type": "Element",
            "namespace": ARF_1_1_NAMESPACE,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class ReportRequests:
    report_request: List[ReportRequest] = field(
        default_factory=list,
        metadata={
            "name": "report-request",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ReportContent:
    """

    :ivar other_element:
    :ivar data_valid_start_date:
    :ivar data_valid_end_date:
    :ivar other_attributes: A placeholder so that content creators can add attributes as desired.
    """
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TestResult",
                    "type": TestResult,
                    "namespace": XCCDF_1_2_NAMESPACE
                },
                {
                    "name": "oval_results",
                    "type": OvalResults,
                    "namespace": OVAL_RESULTS_5_NAMESPACE
                },
                {
                    "name": "TestResult",
                    "type": TestResult_1_1,
                    "namespace": XCCDF_1_1_NAMESPACE
                },
                {
                    "type": object,
                    "namespace": "##other",
                    "wildcard": True
                }
            ),
            "required": True,
        }
    )
    data_valid_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "data-valid-start-date",
            "type": "Attribute",
        }
    )
    data_valid_end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "data-valid-end-date",
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class Report:
    """

    :ivar content: Contains the content of the report.
    :ivar remote_resource:
    :ivar id: An internal ID to identify this report.
    :ivar other_attributes: A placeholder so that content creators can add attributes as desired.
    """

    content: Optional[ReportContent] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    remote_resource: Optional[RemoteResource] = field(
        default=None,
        metadata={
            "name": "remote-resource",
            "type": "Element",
            "namespace": ARF_1_1_NAMESPACE,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class Reports:
    """

    :ivar report: Contains a report, which is composed of zero or more relationships and a content payload.
    """
    report: List[Report] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Asset:
    """

    :ivar person:
    :ivar organization:
    :ivar data:
    :ivar website:
    :ivar system:
    :ivar software:
    :ivar service:
    :ivar network:
    :ivar database:
    :ivar computing_device:
    :ivar circuit:
    :ivar it_asset:
    :ivar asset:
    :ivar remote_resource:
    :ivar id: An internal ID to identify this asset.
    :ivar other_attributes: A placeholder so that content creators can add attributes as desired.
    """
    person: Optional[Person] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/asset-identification/1.1",
        }
    )
    organization: Optional[Organization] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/asset-identification/1.1",
        }
    )
    data: Optional[Data] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/asset-identification/1.1",
        }
    )
    website: Optional[Website] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/asset-identification/1.1",
        }
    )
    system: Optional[System] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/asset-identification/1.1",
        }
    )
    software: Optional[Software] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/asset-identification/1.1",
        }
    )
    service: Optional[Service] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/asset-identification/1.1",
        }
    )
    network: Optional[Network] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/asset-identification/1.1",
        }
    )
    database: Optional[Database] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/asset-identification/1.1",
        }
    )
    computing_device: Optional[ComputingDevice] = field(
        default=None,
        metadata={
            "name": "computing-device",
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/asset-identification/1.1",
        }
    )
    circuit: Optional[Circuit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/asset-identification/1.1",
        }
    )
    it_asset: Optional[ItAsset] = field(
        default=None,
        metadata={
            "name": "it-asset",
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/asset-identification/1.1",
        }
    )
    asset: Optional[AiAsset] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/asset-identification/1.1",
        }
    )
    remote_resource: Optional[RemoteResource] = field(
        default=None,
        metadata={
            "name": "remote-resource",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class Assets:
    asset: List[Asset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ExtendedInfo:
    """
    :ivar other_element:
    :ivar id: An internal ID to identify this object.
    :ivar other_attributes: A placeholder so that content creators can add attributes as desired.
    """
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class ExtendedInfos:
    """
    :ivar extended_info: Contains other information.  Use as an extension point for data that does not fall into the categories defined in asset-report-collection.
    """

    extended_info: List[ExtendedInfo] = field(
        default_factory=list,
        metadata={
            "name": "extended-info",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class AssetReportCollection(RelationshipsContainerType, ParsableElement):
    """

    The top-level report element.

    :ivar report_requests: Contains one or more requests for reports. Each report request must be referenced in a relationship on a report in the same asset-report-collection.
    :ivar assets: Contains the representation of one or more assets represented using the Asset Identification format.
    :ivar reports: Contains one or more reports.
    :ivar extended_infos: Contain other information elements.  Used as an extension point.
    :ivar id: The id for this collection.
    :ivar other_attributes: A placeholder so that content creators can add attributes as desired.
    """

    class Meta:
        name = "asset-report-collection"
        namespace = ARF_1_1_NAMESPACE

    report_requests: Optional[ReportRequests] = field(
        default=None,
        metadata={
            "name": "report-requests",
            "type": "Element",
        }
    )
    assets: Optional[Assets] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    reports: Optional[Reports] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    extended_infos: Optional[ExtendedInfos] = field(
        default=None,
        metadata={
            "name": "extended-infos",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
