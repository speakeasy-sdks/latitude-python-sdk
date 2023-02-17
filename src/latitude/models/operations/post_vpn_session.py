import dataclasses
from ..shared import security as shared_security
from ..shared import vpn_session_with_password as shared_vpn_session_with_password
from dataclasses_json import dataclass_json
from latitude import utils
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class PostVpnSessionRequestBody:
    data: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class PostVpnSessionSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class PostVpnSessionRequest:
    security: PostVpnSessionSecurity = dataclasses.field()
    request: Optional[PostVpnSessionRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class PostVpnSessionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    vpn_session_with_password: Optional[shared_vpn_session_with_password.VpnSessionWithPassword] = dataclasses.field(default=None)
    