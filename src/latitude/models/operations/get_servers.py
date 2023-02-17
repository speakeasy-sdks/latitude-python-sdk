import dataclasses
from ..shared import security as shared_security
from ..shared import servers as shared_servers
from typing import Optional


@dataclasses.dataclass
class GetServersQueryParams:
    extra_fields_servers_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'extra_fields[servers]', 'style': 'form', 'explode': True }})
    filter_created_at_gte_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[created_at_gte]', 'style': 'form', 'explode': True }})
    filter_created_at_lte_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[created_at_lte]', 'style': 'form', 'explode': True }})
    filter_hostname_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[hostname]', 'style': 'form', 'explode': True }})
    filter_label_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[label]', 'style': 'form', 'explode': True }})
    filter_operating_system_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[operating_system]', 'style': 'form', 'explode': True }})
    filter_plan_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[plan]', 'style': 'form', 'explode': True }})
    filter_project_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[project]', 'style': 'form', 'explode': True }})
    filter_region_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[region]', 'style': 'form', 'explode': True }})
    filter_status_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[status]', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetServersSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetServersRequest:
    query_params: GetServersQueryParams = dataclasses.field()
    security: GetServersSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetServersResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    servers: Optional[shared_servers.Servers] = dataclasses.field(default=None)
    