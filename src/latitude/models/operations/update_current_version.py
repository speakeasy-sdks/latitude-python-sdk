from __future__ import annotations
import dataclasses
from ..shared import security as shared_security
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateCurrentVersionRequestBodyDataAttributes:
    new_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('new_version'), 'exclude': lambda f: f is None }})
    
class UpdateCurrentVersionRequestBodyDataTypeEnum(str, Enum):
    API_VERSION = "api_version"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateCurrentVersionRequestBodyData:
    attributes: Optional[UpdateCurrentVersionRequestBodyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes'), 'exclude': lambda f: f is None }})
    type: Optional[UpdateCurrentVersionRequestBodyDataTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateCurrentVersionRequestBody:
    data: Optional[UpdateCurrentVersionRequestBodyData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data'), 'exclude': lambda f: f is None }})
    

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
    