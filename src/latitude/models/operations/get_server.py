from __future__ import annotations
import dataclasses
from ..shared import security as shared_security
from ..shared import server as shared_server
from typing import Optional


@dataclasses.dataclass
class GetServerPathParams:
    server_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'server_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetServerQueryParams:
    extra_fields_servers: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'extra_fields[servers]', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetServerSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetServerRequest:
    path_params: GetServerPathParams = dataclasses.field()
    query_params: GetServerQueryParams = dataclasses.field()
    security: GetServerSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetServerResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    server: Optional[shared_server.Server] = dataclasses.field(default=None)
    