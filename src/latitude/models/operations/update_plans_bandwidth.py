import dataclasses
from ..shared import error_object as shared_error_object
from ..shared import plans_bandwidth as shared_plans_bandwidth
from ..shared import security as shared_security
from dataclasses_json import dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class UpdatePlansBandwidthRequestBodyDataAttributes:
    project: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('project') }})
    quantity: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('quantity') }})
    region_slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('region_slug') }})
    
class UpdatePlansBandwidthRequestBodyDataTypeEnum(str, Enum):
    BANDWIDTH_PACKAGES = "bandwidth_packages"


@dataclass_json
@dataclasses.dataclass
class UpdatePlansBandwidthRequestBodyData:
    attributes: Optional[UpdatePlansBandwidthRequestBodyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes') }})
    type: Optional[UpdatePlansBandwidthRequestBodyDataTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class UpdatePlansBandwidthRequestBody:
    data: Optional[UpdatePlansBandwidthRequestBodyData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class UpdatePlansBandwidthSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class UpdatePlansBandwidthRequest:
    security: UpdatePlansBandwidthSecurity = dataclasses.field()
    request: Optional[UpdatePlansBandwidthRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdatePlansBandwidthResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    plans_bandwidth: Optional[shared_plans_bandwidth.PlansBandwidth] = dataclasses.field(default=None)
    