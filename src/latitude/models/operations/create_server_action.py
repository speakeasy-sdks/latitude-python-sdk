from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import error_object as shared_error_object
from ..shared import server_action as shared_server_action
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class CreateServerActionSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class CreateServerActionPathParams:
    server_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'server_id', 'style': 'simple', 'explode': False }})
    
class CreateServerActionRequestBodyDataAttributesActionEnum(str, Enum):
    POWER_ON = "power_on"
    POWER_OFF = "power_off"
    REBOOT = "reboot"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateServerActionRequestBodyDataAttributes:
    action: Optional[CreateServerActionRequestBodyDataAttributesActionEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action'), 'exclude': lambda f: f is None }})
    
class CreateServerActionRequestBodyDataTypeEnum(str, Enum):
    ACTIONS = "actions"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateServerActionRequestBodyData:
    type: CreateServerActionRequestBodyDataTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    attributes: Optional[CreateServerActionRequestBodyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attributes'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateServerActionRequestBody:
    data: CreateServerActionRequestBodyData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})
    

@dataclasses.dataclass
class CreateServerActionRequest:
    path_params: CreateServerActionPathParams = dataclasses.field()
    request: Optional[CreateServerActionRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateServerActionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    server_action: Optional[shared_server_action.ServerAction] = dataclasses.field(default=None)
    