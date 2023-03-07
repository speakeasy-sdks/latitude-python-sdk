from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import error_object as shared_error_object
from ..shared import ip_addresses as shared_ip_addresses
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class GetIpsSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    
class GetIpsFilterFamilyEnum(str, Enum):
    I_PV4 = "IPv4"
    I_PV6 = "IPv6"

class GetIpsFilterTypeEnum(str, Enum):
    PRIVATE = "private"
    PUBLIC = "public"


@dataclasses.dataclass
class GetIpsQueryParams:
    extra_fields_ip_addresses: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'extra_fields[ip_addresses]', 'style': 'form', 'explode': True }})
    filter_address: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[address]', 'style': 'form', 'explode': True }})
    filter_family: Optional[GetIpsFilterFamilyEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[family]', 'style': 'form', 'explode': True }})
    filter_location: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[location]', 'style': 'form', 'explode': True }})
    filter_project: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[project]', 'style': 'form', 'explode': True }})
    filter_server: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[server]', 'style': 'form', 'explode': True }})
    filter_type: Optional[GetIpsFilterTypeEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[type]', 'style': 'form', 'explode': True }})
    include: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'include', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetIpsRequest:
    query_params: GetIpsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetIpsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    ip_addresses: Optional[shared_ip_addresses.IPAddresses] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    