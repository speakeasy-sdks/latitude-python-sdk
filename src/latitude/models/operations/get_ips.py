import dataclasses
from ..shared import error_object as shared_error_object
from ..shared import ip_addresses as shared_ip_addresses
from ..shared import security as shared_security
from enum import Enum
from typing import Optional

class GetIpsFilterFamilyEnum(str, Enum):
    I_PV4 = "IPv4"
    I_PV6 = "IPv6"

class GetIpsFilterTypeEnum(str, Enum):
    PRIVATE = "private"
    PUBLIC = "public"


@dataclasses.dataclass
class GetIpsQueryParams:
    extra_fields_ip_addresses_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'extra_fields[ip_addresses]', 'style': 'form', 'explode': True }})
    filter_address_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[address]', 'style': 'form', 'explode': True }})
    filter_family_: Optional[GetIpsFilterFamilyEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[family]', 'style': 'form', 'explode': True }})
    filter_location_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[location]', 'style': 'form', 'explode': True }})
    filter_project_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[project]', 'style': 'form', 'explode': True }})
    filter_server_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[server]', 'style': 'form', 'explode': True }})
    filter_type_: Optional[GetIpsFilterTypeEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[type]', 'style': 'form', 'explode': True }})
    include: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'include', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetIpsSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetIpsRequest:
    query_params: GetIpsQueryParams = dataclasses.field()
    security: GetIpsSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetIpsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    ip_addresses: Optional[shared_ip_addresses.IPAddresses] = dataclasses.field(default=None)
    