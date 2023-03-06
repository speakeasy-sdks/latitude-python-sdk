from __future__ import annotations
import dataclasses
import requests
from ..shared import project as shared_project
from dataclasses_json import Undefined, dataclass_json
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class GetProjectSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetProjectPathParams:
    id_or_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id_or_slug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetProjectQueryParams:
    extra_fields_projects: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'extra_fields[projects]', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetProjectRequest:
    path_params: GetProjectPathParams = dataclasses.field()
    query_params: GetProjectQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProject200ApplicationJSON:
    data: Optional[shared_project.Project] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetProjectResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_project_200_application_json_object: Optional[GetProject200ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    