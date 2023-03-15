from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import error_object as shared_error_object
from typing import Optional


@dataclasses.dataclass
class DeleteVirtualNetworksAssignmentsSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class DeleteVirtualNetworksAssignmentsRequest:
    assignment_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'assignment_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteVirtualNetworksAssignmentsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    