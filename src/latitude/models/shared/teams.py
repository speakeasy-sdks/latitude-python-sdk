from __future__ import annotations
import dataclasses
from ..shared import team as shared_team
from dataclasses_json import Undefined, dataclass_json
from latitude import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Teams:
    data: Optional[list[shared_team.Team]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data'), 'exclude': lambda f: f is None }})
    meta: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('meta'), 'exclude': lambda f: f is None }})
    