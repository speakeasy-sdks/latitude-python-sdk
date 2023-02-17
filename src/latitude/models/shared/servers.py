import dataclasses
from ..shared import server_data as shared_server_data
from dataclasses_json import dataclass_json
from latitude import utils
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class Servers:
    data: Optional[list[shared_server_data.ServerData]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    meta: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('meta') }})
    