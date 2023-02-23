from __future__ import annotations
import dataclasses
from ..shared import security as shared_security
from ..shared import user_data as shared_user_data
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class PostProjectUserDataPathParams:
    project_id_or_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id_or_slug', 'style': 'simple', 'explode': False }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostProjectUserDataRequestBodyDataAttributes:
    content: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('content') }})
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    
class PostProjectUserDataRequestBodyDataTypeEnum(str, Enum):
    USER_DATA = "user_data"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostProjectUserDataRequestBodyData:
    type: PostProjectUserDataRequestBodyDataTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    attributes: Optional[PostProjectUserDataRequestBodyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostProjectUserDataRequestBody:
    data: PostProjectUserDataRequestBodyData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class PostProjectUserDataSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class PostProjectUserDataRequest:
    path_params: PostProjectUserDataPathParams = dataclasses.field()
    security: PostProjectUserDataSecurity = dataclasses.field()
    request: Optional[PostProjectUserDataRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class PostProjectUserDataResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    user_data: Optional[shared_user_data.UserData] = dataclasses.field(default=None)
    