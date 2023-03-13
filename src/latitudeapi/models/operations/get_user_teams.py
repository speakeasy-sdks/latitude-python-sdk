from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import teams as shared_teams
from typing import Optional


@dataclasses.dataclass
class GetUserTeamsSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetUserTeamsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    teams: Optional[shared_teams.Teams] = dataclasses.field(default=None)
    