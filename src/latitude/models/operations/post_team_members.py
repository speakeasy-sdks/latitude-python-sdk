from __future__ import annotations
import dataclasses
from ..shared import error_object as shared_error_object
from ..shared import membership as shared_membership
from ..shared import security as shared_security
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional

class PostTeamMembersRequestBodyDataAttributesRoleEnum(str, Enum):
    OWNER = "owner"
    ADMINISTRATOR = "administrator"
    COLLABORATOR = "collaborator"
    BILLING = "billing"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostTeamMembersRequestBodyDataAttributes:
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('email') }})
    role: PostTeamMembersRequestBodyDataAttributesRoleEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('role') }})
    first_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('first_name'), 'exclude': lambda f: f is None }})
    last_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('last_name'), 'exclude': lambda f: f is None }})
    
class PostTeamMembersRequestBodyDataTypeEnum(str, Enum):
    MEMBERSHIPS = "memberships"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostTeamMembersRequestBodyData:
    type: PostTeamMembersRequestBodyDataTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    attributes: Optional[PostTeamMembersRequestBodyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostTeamMembersRequestBody:
    data: PostTeamMembersRequestBodyData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class PostTeamMembersSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class PostTeamMembersRequest:
    security: PostTeamMembersSecurity = dataclasses.field()
    request: Optional[PostTeamMembersRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class PostTeamMembersResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    membership: Optional[shared_membership.Membership] = dataclasses.field(default=None)
    