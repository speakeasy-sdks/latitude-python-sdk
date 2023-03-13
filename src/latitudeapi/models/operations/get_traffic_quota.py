from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import error_object as shared_error_object
from ..shared import traffic_quota as shared_traffic_quota
from typing import Optional


@dataclasses.dataclass
class GetTrafficQuotaSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetTrafficQuotaQueryParams:
    filter_project: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[project]', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetTrafficQuotaRequest:
    query_params: GetTrafficQuotaQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetTrafficQuotaResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    traffic_quota: Optional[shared_traffic_quota.TrafficQuota] = dataclasses.field(default=None)
    