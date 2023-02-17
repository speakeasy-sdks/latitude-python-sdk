import dataclasses
from ..shared import plan_data as shared_plan_data
from ..shared import security as shared_security
from dataclasses_json import dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional

class GetPlansFilterStockLevelEnum(str, Enum):
    UNAVAILABLE = "Unavailable"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    UNIQUE = "Unique"


@dataclasses.dataclass
class GetPlansQueryParams:
    filter_in_stock_: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[in_stock]', 'style': 'form', 'explode': True }})
    filter_location_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[location]', 'style': 'form', 'explode': True }})
    filter_name_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[name]', 'style': 'form', 'explode': True }})
    filter_slug_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[slug]', 'style': 'form', 'explode': True }})
    filter_stock_level_: Optional[GetPlansFilterStockLevelEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[stock_level]', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetPlansSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetPlansRequest:
    query_params: GetPlansQueryParams = dataclasses.field()
    security: GetPlansSecurity = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetPlans200ApplicationJSON:
    data: Optional[list[shared_plan_data.PlanData]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class GetPlansResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_plans_200_application_json_object: Optional[GetPlans200ApplicationJSON] = dataclasses.field(default=None)
    