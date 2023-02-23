from __future__ import annotations
import dataclasses
from ..shared import operating_systems as shared_operating_systems
from ..shared import security as shared_security
from dataclasses_json import Undefined, dataclass_json
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class GetPlansOperatingSystemSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetPlansOperatingSystemRequest:
    security: GetPlansOperatingSystemSecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetPlansOperatingSystem200ApplicationJSON:
    data: Optional[list[shared_operating_systems.OperatingSystems]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetPlansOperatingSystemResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_plans_operating_system_200_application_json_object: Optional[GetPlansOperatingSystem200ApplicationJSON] = dataclasses.field(default=None)
    