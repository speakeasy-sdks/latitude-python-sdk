import dataclasses
from ..shared import security as shared_security
from ..shared import teams as shared_teams
from typing import Optional


@dataclasses.dataclass
class GetTeamSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetTeamRequest:
    security: GetTeamSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetTeamResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    teams: Optional[shared_teams.Teams] = dataclasses.field(default=None)
    