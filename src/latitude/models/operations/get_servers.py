from __future__ import annotations
import dataclasses
import requests
from ..shared import servers as shared_servers
from typing import Optional


@dataclasses.dataclass
class GetServersSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetServersQueryParams:
    extra_fields_servers: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'extra_fields[servers]', 'style': 'form', 'explode': True }})
    filter_created_at_gte: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[created_at_gte]', 'style': 'form', 'explode': True }})
    filter_created_at_lte: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[created_at_lte]', 'style': 'form', 'explode': True }})
    filter_hostname: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[hostname]', 'style': 'form', 'explode': True }})
    filter_label: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[label]', 'style': 'form', 'explode': True }})
    filter_operating_system: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[operating_system]', 'style': 'form', 'explode': True }})
    filter_plan: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[plan]', 'style': 'form', 'explode': True }})
    filter_project: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[project]', 'style': 'form', 'explode': True }})
    filter_region: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[region]', 'style': 'form', 'explode': True }})
    filter_status: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[status]', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetServersRequest:
    query_params: GetServersQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetServersResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    servers: Optional[shared_servers.Servers] = dataclasses.field(default=None)
    