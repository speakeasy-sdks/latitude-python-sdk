import dataclasses
from ..shared import error_object as shared_error_object
from ..shared import project as shared_project
from ..shared import security as shared_security
from dataclasses_json import dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class UpdateProjectPathParams:
    id_or_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id_or_slug', 'style': 'simple', 'explode': False }})
    
class UpdateProjectRequestBodyDataAttributesEnvironmentEnum(str, Enum):
    DEVELOPMENT = "Development"
    STAGING = "Staging"
    PRODUCTION = "Production"


@dataclass_json
@dataclasses.dataclass
class UpdateProjectRequestBodyDataAttributes:
    bandwidth_alert: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('bandwidth_alert') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    environment: Optional[UpdateProjectRequestBodyDataAttributesEnvironmentEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('environment') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    
class UpdateProjectRequestBodyDataTypeEnum(str, Enum):
    PROJECTS = "projects"


@dataclass_json
@dataclasses.dataclass
class UpdateProjectRequestBodyData:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    type: UpdateProjectRequestBodyDataTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    attributes: Optional[UpdateProjectRequestBodyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes') }})
    

@dataclass_json
@dataclasses.dataclass
class UpdateProjectRequestBody:
    data: UpdateProjectRequestBodyData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class UpdateProjectSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class UpdateProjectRequest:
    path_params: UpdateProjectPathParams = dataclasses.field()
    security: UpdateProjectSecurity = dataclasses.field()
    request: Optional[UpdateProjectRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class UpdateProject200ApplicationJSON:
    data: Optional[shared_project.Project] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class UpdateProjectResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    update_project_200_application_json_object: Optional[UpdateProject200ApplicationJSON] = dataclasses.field(default=None)
    