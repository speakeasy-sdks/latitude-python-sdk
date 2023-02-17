import dataclasses
from ..shared import security as shared_security
from ..shared import virtual_network_assignments as shared_virtual_network_assignments
from typing import Optional


@dataclasses.dataclass
class GetVirtualNetworksAssignmentsQueryParams:
    filter_server_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[server]', 'style': 'form', 'explode': True }})
    filter_vid_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[vid]', 'style': 'form', 'explode': True }})
    filter_virtual_network_id_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[virtual_network_id]', 'style': 'form', 'explode': True }})
    include: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'include', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetVirtualNetworksAssignmentsSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetVirtualNetworksAssignmentsRequest:
    query_params: GetVirtualNetworksAssignmentsQueryParams = dataclasses.field()
    security: GetVirtualNetworksAssignmentsSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetVirtualNetworksAssignmentsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    virtual_network_assignments: Optional[shared_virtual_network_assignments.VirtualNetworkAssignments] = dataclasses.field(default=None)
    