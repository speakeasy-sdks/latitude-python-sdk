from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import vpn_session_data_with_password as shared_vpn_session_data_with_password
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from latitude import utils
from typing import Any, Optional


@dataclasses.dataclass
class GetVpnSessionsSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    
class GetVpnSessionsFilterSiteEnum(str, Enum):
    MH1 = "MH1"
    SP1 = "SP1"
    SP4 = "SP4"
    SYD = "SYD"
    CH1 = "CH1"
    DAL2 = "DAL2"
    LA2 = "LA2"
    MI1 = "MI1"
    NY2 = "NY2"
    SAN = "SAN"
    TY6 = "TY6"
    TY8 = "TY8"


@dataclasses.dataclass
class GetVpnSessionsRequest:
    filter_site: Optional[GetVpnSessionsFilterSiteEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[site]', 'style': 'form', 'explode': True }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetVpnSessions200ApplicationJSON:
    data: Optional[list[shared_vpn_session_data_with_password.VpnSessionDataWithPassword]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    meta: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('meta'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetVpnSessionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_vpn_sessions_200_application_json_object: Optional[GetVpnSessions200ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    