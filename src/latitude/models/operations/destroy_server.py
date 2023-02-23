from __future__ import annotations
import dataclasses
from ..shared import error_object as shared_error_object
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class DestroyServerPathParams:
    server_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'server_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DestroyServerSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class DestroyServerRequest:
    path_params: DestroyServerPathParams = dataclasses.field()
    security: DestroyServerSecurity = dataclasses.field()
    

@dataclasses.dataclass
class DestroyServerResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    