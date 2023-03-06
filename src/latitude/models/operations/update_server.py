from __future__ import annotations
import dataclasses
import requests
from ..shared import server as shared_server
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class UpdateServerSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class UpdateServerPathParams:
    server_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'server_id', 'style': 'simple', 'explode': False }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateServerRequestBodyAttributes:
    hostname: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hostname'), 'exclude': lambda f: f is None }})
    
class UpdateServerRequestBodyTypeEnum(str, Enum):
    SERVERS = "servers"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateServerRequestBody:
    attributes: Optional[UpdateServerRequestBodyAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attributes'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    type: Optional[UpdateServerRequestBodyTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class UpdateServerRequest:
    path_params: UpdateServerPathParams = dataclasses.field()
    request: Optional[UpdateServerRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdateServerResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    server: Optional[shared_server.Server] = dataclasses.field(default=None)
    