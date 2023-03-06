from __future__ import annotations
import dataclasses
import requests
from ..shared import teams as shared_teams
from typing import Optional


@dataclasses.dataclass
class GetTeamSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetTeamResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    teams: Optional[shared_teams.Teams] = dataclasses.field(default=None)
    