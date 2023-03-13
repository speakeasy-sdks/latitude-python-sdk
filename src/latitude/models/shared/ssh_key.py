from __future__ import annotations
import dataclasses
from ..shared import ssh_key_data as shared_ssh_key_data
from dataclasses_json import Undefined, dataclass_json
from latitude import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SSHKey:
    data: Optional[list[shared_ssh_key_data.SSHKeyData]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    