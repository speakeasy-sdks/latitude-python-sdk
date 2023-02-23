from __future__ import annotations
import dataclasses
from ..shared import error_object as shared_error_object
from ..shared import project as shared_project
from ..shared import security as shared_security
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional

class CreateProjectRequestBodyDataAttributesEnvironmentEnum(str, Enum):
    DEVELOPMENT = "Development"
    STAGING = "Staging"
    PRODUCTION = "Production"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateProjectRequestBodyDataAttributes:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }})
    environment: Optional[CreateProjectRequestBodyDataAttributesEnvironmentEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('environment'), 'exclude': lambda f: f is None }})
    
class CreateProjectRequestBodyDataTypeEnum(str, Enum):
    PROJECTS = "projects"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateProjectRequestBodyData:
    type: CreateProjectRequestBodyDataTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    attributes: Optional[CreateProjectRequestBodyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateProjectRequestBody:
    data: Optional[CreateProjectRequestBodyData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class CreateProjectSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class CreateProjectRequest:
    security: CreateProjectSecurity = dataclasses.field()
    request: Optional[CreateProjectRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateProject201ApplicationJSON:
    data: Optional[shared_project.Project] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class CreateProjectResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_project_201_application_json_object: Optional[CreateProject201ApplicationJSON] = dataclasses.field(default=None)
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    