from __future__ import annotations
import dataclasses
from ..shared import error_object as shared_error_object
from ..shared import role as shared_role
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class GetRoleIDPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetRoleIDSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetRoleIDRequest:
    path_params: GetRoleIDPathParams = dataclasses.field()
    security: GetRoleIDSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetRoleIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    role: Optional[shared_role.Role] = dataclasses.field(default=None)
    