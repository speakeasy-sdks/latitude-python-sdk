from __future__ import annotations
import dataclasses
from ..shared import security as shared_security
from ..shared import user as shared_user
from dataclasses_json import Undefined, dataclass_json
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class GetUserProfileSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetUserProfileRequest:
    security: GetUserProfileSecurity = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetUserProfile200ApplicationJSON:
    data: Optional[shared_user.User] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetUserProfileResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_user_profile_200_application_json_object: Optional[GetUserProfile200ApplicationJSON] = dataclasses.field(default=None)
    