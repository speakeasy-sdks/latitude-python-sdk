import dataclasses
from ..shared import security as shared_security
from ..shared import virtual_networks as shared_virtual_networks
from typing import Optional


@dataclasses.dataclass
class GetVirtualNetworksQueryParams:
    filter_project_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[project]', 'style': 'form', 'explode': True }})
    filter_site_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[site]', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetVirtualNetworksSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetVirtualNetworksRequest:
    query_params: GetVirtualNetworksQueryParams = dataclasses.field()
    security: GetVirtualNetworksSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetVirtualNetworksResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    virtual_networks: Optional[shared_virtual_networks.VirtualNetworks] = dataclasses.field(default=None)
    