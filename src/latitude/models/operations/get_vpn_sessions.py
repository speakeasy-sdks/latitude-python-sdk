import dataclasses
from ..shared import security as shared_security
from ..shared import vpn_session_data_with_password as shared_vpn_session_data_with_password
from dataclasses_json import dataclass_json
from enum import Enum
from latitude import utils
from typing import Any, Optional

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
class GetVpnSessionsQueryParams:
    filter_site_: Optional[GetVpnSessionsFilterSiteEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[site]', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetVpnSessionsSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetVpnSessionsRequest:
    query_params: GetVpnSessionsQueryParams = dataclasses.field()
    security: GetVpnSessionsSecurity = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetVpnSessions200ApplicationJSON:
    data: Optional[list[shared_vpn_session_data_with_password.VpnSessionDataWithPassword]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    meta: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('meta') }})
    

@dataclasses.dataclass
class GetVpnSessionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_vpn_sessions_200_application_json_object: Optional[GetVpnSessions200ApplicationJSON] = dataclasses.field(default=None)
    