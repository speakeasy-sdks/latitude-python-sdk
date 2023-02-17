import dataclasses
from dataclasses_json import dataclass_json
from latitude import utils
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class ServerRescue:
    meta: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('meta') }})
    