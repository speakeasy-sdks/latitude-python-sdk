import dataclasses
from ..shared import project as shared_project
from ..shared import security as shared_security
from dataclasses_json import dataclass_json
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class GetProjectPathParams:
    id_or_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id_or_slug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetProjectQueryParams:
    extra_fields_projects_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'extra_fields[projects]', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetProjectSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetProjectRequest:
    path_params: GetProjectPathParams = dataclasses.field()
    query_params: GetProjectQueryParams = dataclasses.field()
    security: GetProjectSecurity = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetProject200ApplicationJSON:
    data: Optional[shared_project.Project] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class GetProjectResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_project_200_application_json_object: Optional[GetProject200ApplicationJSON] = dataclasses.field(default=None)
    