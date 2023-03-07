from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import plan_data as shared_plan_data
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class GetPlansSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    
class GetPlansFilterStockLevelEnum(str, Enum):
    UNAVAILABLE = "Unavailable"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    UNIQUE = "Unique"


@dataclasses.dataclass
class GetPlansQueryParams:
    filter_in_stock: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[in_stock]', 'style': 'form', 'explode': True }})
    filter_location: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[location]', 'style': 'form', 'explode': True }})
    filter_name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[name]', 'style': 'form', 'explode': True }})
    filter_slug: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[slug]', 'style': 'form', 'explode': True }})
    filter_stock_level: Optional[GetPlansFilterStockLevelEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[stock_level]', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetPlansRequest:
    query_params: GetPlansQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPlans200ApplicationJSON:
    data: Optional[list[shared_plan_data.PlanData]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetPlansResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_plans_200_application_json_object: Optional[GetPlans200ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    