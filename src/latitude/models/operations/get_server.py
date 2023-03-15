from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import server as shared_server
from typing import Optional


@dataclasses.dataclass
class GetServerSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetServerRequest:
    server_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'server_id', 'style': 'simple', 'explode': False }})
    extra_fields_servers: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'extra_fields[servers]', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetServerResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    server: Optional[shared_server.Server] = dataclasses.field(default=None)
    