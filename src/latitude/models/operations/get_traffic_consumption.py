from __future__ import annotations
import dataclasses
from ..shared import security as shared_security
from ..shared import traffic as shared_traffic
from typing import Optional


@dataclasses.dataclass
class GetTrafficConsumptionQueryParams:
    filter_from_date: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[from_date]', 'style': 'form', 'explode': True }})
    filter_project: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[project]', 'style': 'form', 'explode': True }})
    filter_server: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[server]', 'style': 'form', 'explode': True }})
    filter_to_date: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[to_date]', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetTrafficConsumptionSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetTrafficConsumptionRequest:
    query_params: GetTrafficConsumptionQueryParams = dataclasses.field()
    security: GetTrafficConsumptionSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetTrafficConsumptionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    traffic: Optional[shared_traffic.Traffic] = dataclasses.field(default=None)
    