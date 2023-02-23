from __future__ import annotations
import dataclasses
from ..shared import error_object as shared_error_object
from ..shared import security as shared_security
from ..shared import server_rescue as shared_server_rescue
from typing import Optional


@dataclasses.dataclass
class ServerStartRescueModePathParams:
    server_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'server_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ServerStartRescueModeSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class ServerStartRescueModeRequest:
    path_params: ServerStartRescueModePathParams = dataclasses.field()
    security: ServerStartRescueModeSecurity = dataclasses.field()
    

@dataclasses.dataclass
class ServerStartRescueModeResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    server_rescue: Optional[shared_server_rescue.ServerRescue] = dataclasses.field(default=None)
    