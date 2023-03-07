from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import vpn_session_with_password as shared_vpn_session_with_password
from dataclasses_json import Undefined, dataclass_json
from latitude import utils
from typing import Any, Optional


@dataclasses.dataclass
class PostVpnSessionSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostVpnSessionRequestBody:
    data: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PostVpnSessionRequest:
    request: Optional[PostVpnSessionRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class PostVpnSessionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    vpn_session_with_password: Optional[shared_vpn_session_with_password.VpnSessionWithPassword] = dataclasses.field(default=None)
    