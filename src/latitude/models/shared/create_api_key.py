import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class CreateAPIKeyDataAttributes:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    
class CreateAPIKeyDataTypeEnum(str, Enum):
    API_KEYS = "api_keys"


@dataclass_json
@dataclasses.dataclass
class CreateAPIKeyData:
    type: CreateAPIKeyDataTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    attributes: Optional[CreateAPIKeyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class CreateAPIKey:
    data: Optional[CreateAPIKeyData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    