from __future__ import annotations
import dataclasses
from ..shared import plan_data as shared_plan_data
from dataclasses_json import Undefined, dataclass_json
from latitudeapi import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Plan:
    data: Optional[shared_plan_data.PlanData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    