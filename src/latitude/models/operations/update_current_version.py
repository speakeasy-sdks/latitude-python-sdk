import dataclasses
from ..shared import security as shared_security
from dataclasses_json import dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class UpdateCurrentVersionRequestBodyDataAttributes:
    new_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('new_version') }})
    
class UpdateCurrentVersionRequestBodyDataTypeEnum(str, Enum):
    API_VERSION = "api_version"


@dataclass_json
@dataclasses.dataclass
class UpdateCurrentVersionRequestBodyData:
    attributes: Optional[UpdateCurrentVersionRequestBodyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes') }})
    type: Optional[UpdateCurrentVersionRequestBodyDataTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class UpdateCurrentVersionRequestBody:
    data: Optional[UpdateCurrentVersionRequestBodyData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class UpdateCurrentVersionSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class UpdateCurrentVersionRequest:
    security: UpdateCurrentVersionSecurity = dataclasses.field()
    request: Optional[UpdateCurrentVersionRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdateCurrentVersionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    