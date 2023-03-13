from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import user_data as shared_user_data
from dataclasses_json import Undefined, dataclass_json
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class GetProjectUsersDataSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetProjectUsersDataPathParams:
    project_id_or_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id_or_slug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetProjectUsersDataQueryParams:
    extra_fields_user_data: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'extra_fields[user_data]', 'style': 'form', 'explode': True }})
    include: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'include', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetProjectUsersDataRequest:
    path_params: GetProjectUsersDataPathParams = dataclasses.field()
    query_params: GetProjectUsersDataQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProjectUsersData200ApplicationJSON:
    data: Optional[list[shared_user_data.UserData]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetProjectUsersDataResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_project_users_data_200_application_json_object: Optional[GetProjectUsersData200ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    