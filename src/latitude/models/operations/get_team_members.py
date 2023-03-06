from __future__ import annotations
import dataclasses
import requests
from ..shared import team_members as shared_team_members
from typing import Optional


@dataclasses.dataclass
class GetTeamMembersSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetTeamMembersResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    team_members: Optional[shared_team_members.TeamMembers] = dataclasses.field(default=None)
    