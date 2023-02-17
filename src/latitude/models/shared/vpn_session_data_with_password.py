import dataclasses
from ..shared import region_resource_data as shared_region_resource_data
from dataclasses_json import dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional

class VpnSessionDataWithPasswordAttributesStatusEnum(str, Enum):
    ENABLE = "enable"
    DISABLE = "disable"


@dataclass_json
@dataclasses.dataclass
class VpnSessionDataWithPasswordAttributes:
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at') }})
    expires_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('expires_at') }})
    host: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('host') }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('password') }})
    port: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('port') }})
    region: Optional[shared_region_resource_data.RegionResourceData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('region') }})
    status: Optional[VpnSessionDataWithPasswordAttributesStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    updated_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('updated_at') }})
    user_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('user_name') }})
    
class VpnSessionDataWithPasswordTypeEnum(str, Enum):
    VPN_SESSIONS = "vpn_sessions"


@dataclass_json
@dataclasses.dataclass
class VpnSessionDataWithPassword:
    attributes: Optional[VpnSessionDataWithPasswordAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    type: Optional[VpnSessionDataWithPasswordTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    