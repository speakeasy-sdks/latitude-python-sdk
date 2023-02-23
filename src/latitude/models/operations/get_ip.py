from __future__ import annotations
import dataclasses
from ..shared import error_object as shared_error_object
from ..shared import ip_address as shared_ip_address
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class GetIPPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetIPQueryParams:
    extra_fields_ip_addresses: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'extra_fields[ip_addresses]', 'style': 'form', 'explode': True }})
    include: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'include', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetIPSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetIPRequest:
    path_params: GetIPPathParams = dataclasses.field()
    query_params: GetIPQueryParams = dataclasses.field()
    security: GetIPSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetIPResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    ip_address: Optional[shared_ip_address.IPAddress] = dataclasses.field(default=None)
    