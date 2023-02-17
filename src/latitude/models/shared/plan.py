import dataclasses
from ..shared import plan_data as shared_plan_data
from dataclasses_json import dataclass_json
from latitude import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class Plan:
    data: Optional[shared_plan_data.PlanData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    