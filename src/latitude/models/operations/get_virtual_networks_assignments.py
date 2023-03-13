from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import virtual_network_assignments as shared_virtual_network_assignments
from typing import Optional


@dataclasses.dataclass
class GetVirtualNetworksAssignmentsSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetVirtualNetworksAssignmentsQueryParams:
    filter_server: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[server]', 'style': 'form', 'explode': True }})
    filter_vid: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[vid]', 'style': 'form', 'explode': True }})
    filter_virtual_network_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[virtual_network_id]', 'style': 'form', 'explode': True }})
    include: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'include', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetVirtualNetworksAssignmentsRequest:
    query_params: GetVirtualNetworksAssignmentsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetVirtualNetworksAssignmentsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    virtual_network_assignments: Optional[shared_virtual_network_assignments.VirtualNetworkAssignments] = dataclasses.field(default=None)
    