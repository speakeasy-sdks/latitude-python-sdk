from __future__ import annotations
import dataclasses
from ..shared import ip_address as shared_ip_address
from dataclasses_json import Undefined, dataclass_json
from latitudeapi import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IPAddresses:
    data: Optional[list[shared_ip_address.IPAddress]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    