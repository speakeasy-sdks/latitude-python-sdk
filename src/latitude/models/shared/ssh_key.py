import dataclasses
from ..shared import ssh_key_data as shared_ssh_key_data
from dataclasses_json import dataclass_json
from latitude import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class SSHKey:
    data: Optional[list[shared_ssh_key_data.SSHKeyData]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    