import dataclasses
from ..shared import error_object as shared_error_object
from ..shared import project as shared_project
from ..shared import security as shared_security
from dataclasses_json import dataclass_json
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class DeleteProjectPathParams:
    id_or_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id_or_slug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteProjectSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class DeleteProjectRequest:
    path_params: DeleteProjectPathParams = dataclasses.field()
    security: DeleteProjectSecurity = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class DeleteProject200ApplicationJSON:
    data: Optional[shared_project.Project] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class DeleteProjectResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_project_200_application_json_object: Optional[DeleteProject200ApplicationJSON] = dataclasses.field(default=None)
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    