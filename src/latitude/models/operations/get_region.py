from __future__ import annotations
import dataclasses
import requests
from ..shared import error_object as shared_error_object
from ..shared import region as shared_region
from typing import Optional


@dataclasses.dataclass
class GetRegionSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetRegionPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetRegionRequest:
    path_params: GetRegionPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetRegionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    region: Optional[shared_region.Region] = dataclasses.field(default=None)
    