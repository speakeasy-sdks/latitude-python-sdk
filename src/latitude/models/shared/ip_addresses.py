import dataclasses
from ..shared import ip_address as shared_ip_address
from dataclasses_json import dataclass_json
from latitude import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class IPAddresses:
    data: Optional[list[shared_ip_address.IPAddress]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    