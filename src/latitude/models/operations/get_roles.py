from __future__ import annotations
import dataclasses
import requests
from ..shared import role_data as shared_role_data
from dataclasses_json import Undefined, dataclass_json
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class GetRolesSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetRoles200ApplicationJSON:
    data: Optional[list[shared_role_data.RoleData]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetRolesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_roles_200_application_json_object: Optional[GetRoles200ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    