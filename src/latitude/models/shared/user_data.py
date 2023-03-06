from __future__ import annotations
import dataclasses
from ..shared import user_data_properties as shared_user_data_properties
from dataclasses_json import Undefined, dataclass_json
from latitude import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UserData:
    data: Optional[shared_user_data_properties.UserDataProperties] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    