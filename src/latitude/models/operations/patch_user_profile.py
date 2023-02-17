import dataclasses
from ..shared import error_object as shared_error_object
from ..shared import security as shared_security
from ..shared import user_update as shared_user_update
from dataclasses_json import dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class PatchUserProfilePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    
class PatchUserProfileRequestBodyDataAttributesRoleEnum(str, Enum):
    ADMINISTRATOR = "administrator"
    BILLING = "billing"
    COLLABORATOR = "collaborator"
    OWNER = "owner"


@dataclass_json
@dataclasses.dataclass
class PatchUserProfileRequestBodyDataAttributes:
    authentication_factor_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('authentication_factor_id') }})
    first_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('first_name') }})
    last_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('last_name') }})
    role: Optional[PatchUserProfileRequestBodyDataAttributesRoleEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('role') }})
    
class PatchUserProfileRequestBodyDataTypeEnum(str, Enum):
    USERS = "users"


@dataclass_json
@dataclasses.dataclass
class PatchUserProfileRequestBodyData:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    type: PatchUserProfileRequestBodyDataTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    attributes: Optional[PatchUserProfileRequestBodyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes') }})
    

@dataclass_json
@dataclasses.dataclass
class PatchUserProfileRequestBody:
    data: PatchUserProfileRequestBodyData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class PatchUserProfileSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class PatchUserProfileRequest:
    path_params: PatchUserProfilePathParams = dataclasses.field()
    security: PatchUserProfileSecurity = dataclasses.field()
    request: Optional[PatchUserProfileRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class PatchUserProfile200ApplicationJSON:
    data: Optional[shared_user_update.UserUpdate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class PatchUserProfileResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    patch_user_profile_200_application_json_object: Optional[PatchUserProfile200ApplicationJSON] = dataclasses.field(default=None)
    