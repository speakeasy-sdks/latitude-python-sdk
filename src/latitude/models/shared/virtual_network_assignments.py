import dataclasses
from ..shared import virtual_network_assignment as shared_virtual_network_assignment
from dataclasses_json import dataclass_json
from latitude import utils
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class VirtualNetworkAssignments:
    data: Optional[list[shared_virtual_network_assignment.VirtualNetworkAssignment]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    meta: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('meta') }})
    