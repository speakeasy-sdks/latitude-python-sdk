import dataclasses
from ..shared import error_object as shared_error_object
from ..shared import security as shared_security
from ..shared import traffic_quota as shared_traffic_quota
from typing import Optional


@dataclasses.dataclass
class GetTrafficQuotaQueryParams:
    filter_project_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[project]', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetTrafficQuotaSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetTrafficQuotaRequest:
    query_params: GetTrafficQuotaQueryParams = dataclasses.field()
    security: GetTrafficQuotaSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetTrafficQuotaResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    traffic_quota: Optional[shared_traffic_quota.TrafficQuota] = dataclasses.field(default=None)
    