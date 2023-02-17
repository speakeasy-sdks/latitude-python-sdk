import dataclasses
from ..shared import project as shared_project
from dataclasses_json import dataclass_json
from latitude import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class Projects:
    data: Optional[list[shared_project.Project]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    