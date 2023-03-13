from __future__ import annotations
import dataclasses
from ..shared import vpn_session_data_with_password as shared_vpn_session_data_with_password
from dataclasses_json import Undefined, dataclass_json
from latitude import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class VpnSessionWithPassword:
    data: Optional[shared_vpn_session_data_with_password.VpnSessionDataWithPassword] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    