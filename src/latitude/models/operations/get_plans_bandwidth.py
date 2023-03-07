from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import plans_bandwidth as shared_plans_bandwidth
from typing import Optional


@dataclasses.dataclass
class GetPlansBandwidthSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetPlansBandwidthResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    plans_bandwidth: Optional[shared_plans_bandwidth.PlansBandwidth] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    