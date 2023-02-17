import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class RoleDataAttributes:
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    
class RoleDataTypeEnum(str, Enum):
    ROLES = "roles"


@dataclass_json
@dataclasses.dataclass
class RoleData:
    attributes: Optional[RoleDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    type: Optional[RoleDataTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    