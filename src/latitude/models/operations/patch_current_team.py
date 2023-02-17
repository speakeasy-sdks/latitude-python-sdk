import dataclasses
from ..shared import error_object as shared_error_object
from ..shared import security as shared_security
from ..shared import team as shared_team
from dataclasses_json import dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class PatchCurrentTeamPathParams:
    team_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'team_id', 'style': 'simple', 'explode': False }})
    

@dataclass_json
@dataclasses.dataclass
class PatchCurrentTeamRequestBodyDataAttributes:
    address: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('address') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    
class PatchCurrentTeamRequestBodyDataTypeEnum(str, Enum):
    TEAMS = "teams"


@dataclass_json
@dataclasses.dataclass
class PatchCurrentTeamRequestBodyData:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    type: PatchCurrentTeamRequestBodyDataTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    attributes: Optional[PatchCurrentTeamRequestBodyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes') }})
    

@dataclass_json
@dataclasses.dataclass
class PatchCurrentTeamRequestBody:
    data: PatchCurrentTeamRequestBodyData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class PatchCurrentTeamSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class PatchCurrentTeamRequest:
    path_params: PatchCurrentTeamPathParams = dataclasses.field()
    security: PatchCurrentTeamSecurity = dataclasses.field()
    request: Optional[PatchCurrentTeamRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class PatchCurrentTeam200ApplicationJSON:
    data: Optional[shared_team.Team] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class PatchCurrentTeamResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    patch_current_team_200_application_json_object: Optional[PatchCurrentTeam200ApplicationJSON] = dataclasses.field(default=None)
    