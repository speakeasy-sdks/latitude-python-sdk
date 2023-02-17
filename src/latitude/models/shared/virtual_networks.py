import dataclasses
from ..shared import virtual_network as shared_virtual_network
from dataclasses_json import dataclass_json
from latitude import utils
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class VirtualNetworks:
    data: Optional[list[shared_virtual_network.VirtualNetwork]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    meta: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('meta') }})
    