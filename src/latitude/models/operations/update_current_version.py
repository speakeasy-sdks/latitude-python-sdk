from __future__ import annotations
import dataclasses
import requests
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class UpdateCurrentVersionSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateCurrentVersionRequestBodyDataAttributes:
    new_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('new_version'), 'exclude': lambda f: f is None }})
    
class UpdateCurrentVersionRequestBodyDataTypeEnum(str, Enum):
    API_VERSION = "api_version"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateCurrentVersionRequestBodyData:
    attributes: Optional[UpdateCurrentVersionRequestBodyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attributes'), 'exclude': lambda f: f is None }})
    type: Optional[UpdateCurrentVersionRequestBodyDataTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateCurrentVersionRequestBody:
    data: Optional[UpdateCurrentVersionRequestBodyData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class UpdateCurrentVersionRequest:
    request: Optional[UpdateCurrentVersionRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdateCurrentVersionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    