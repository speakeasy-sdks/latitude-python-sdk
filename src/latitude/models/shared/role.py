import dataclasses
from ..shared import role_data as shared_role_data
from dataclasses_json import dataclass_json
from latitude import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class Role:
    data: Optional[shared_role_data.RoleData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    