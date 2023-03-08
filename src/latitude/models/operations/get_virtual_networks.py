from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import virtual_networks as shared_virtual_networks
from typing import Optional


@dataclasses.dataclass
class GetVirtualNetworksSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetVirtualNetworksQueryParams:
    filter_project: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[project]', 'style': 'form', 'explode': True }})
    filter_site: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[site]', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetVirtualNetworksRequest:
    query_params: GetVirtualNetworksQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetVirtualNetworksResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    virtual_networks: Optional[shared_virtual_networks.VirtualNetworks] = dataclasses.field(default=None)
    