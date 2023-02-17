import dataclasses
from ..shared import error_object as shared_error_object
from ..shared import security as shared_security
from ..shared import vpn_session_with_password as shared_vpn_session_with_password
from typing import Optional


@dataclasses.dataclass
class PutVpnSessionPathParams:
    vpn_session_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'vpn_session_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PutVpnSessionSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class PutVpnSessionRequest:
    path_params: PutVpnSessionPathParams = dataclasses.field()
    security: PutVpnSessionSecurity = dataclasses.field()
    

@dataclasses.dataclass
class PutVpnSessionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    vpn_session_with_password: Optional[shared_vpn_session_with_password.VpnSessionWithPassword] = dataclasses.field(default=None)
    