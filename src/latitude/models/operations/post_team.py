import dataclasses
from ..shared import error_object as shared_error_object
from ..shared import security as shared_security
from ..shared import team as shared_team
from dataclasses_json import dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional

class PostTeamRequestBodyDataAttributesCurrencyEnum(str, Enum):
    USD = "USD"
    BRL = "BRL"


@dataclass_json
@dataclasses.dataclass
class PostTeamRequestBodyDataAttributes:
    currency: PostTeamRequestBodyDataAttributesCurrencyEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('currency') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    address: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('address') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    
class PostTeamRequestBodyDataTypeEnum(str, Enum):
    TEAMS = "teams"


@dataclass_json
@dataclasses.dataclass
class PostTeamRequestBodyData:
    type: PostTeamRequestBodyDataTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    attributes: Optional[PostTeamRequestBodyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes') }})
    

@dataclass_json
@dataclasses.dataclass
class PostTeamRequestBody:
    data: PostTeamRequestBodyData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class PostTeamSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class PostTeamRequest:
    security: PostTeamSecurity = dataclasses.field()
    request: Optional[PostTeamRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class PostTeam201ApplicationJSON:
    data: Optional[shared_team.Team] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class PostTeamResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    post_team_201_application_json_object: Optional[PostTeam201ApplicationJSON] = dataclasses.field(default=None)
    