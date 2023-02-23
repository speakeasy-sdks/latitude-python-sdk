from __future__ import annotations
import dataclasses
from ..shared import security as shared_security
from ..shared import team_members as shared_team_members
from typing import Optional


@dataclasses.dataclass
class GetTeamMembersSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetTeamMembersRequest:
    security: GetTeamMembersSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetTeamMembersResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    team_members: Optional[shared_team_members.TeamMembers] = dataclasses.field(default=None)
    