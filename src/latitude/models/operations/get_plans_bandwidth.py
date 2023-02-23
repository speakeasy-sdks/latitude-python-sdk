from __future__ import annotations
import dataclasses
from ..shared import plans_bandwidth as shared_plans_bandwidth
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class GetPlansBandwidthSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetPlansBandwidthRequest:
    security: GetPlansBandwidthSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetPlansBandwidthResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    plans_bandwidth: Optional[shared_plans_bandwidth.PlansBandwidth] = dataclasses.field(default=None)
    