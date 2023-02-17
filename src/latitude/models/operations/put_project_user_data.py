import dataclasses
from ..shared import security as shared_security
from ..shared import user_data as shared_user_data
from dataclasses_json import dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class PutProjectUserDataPathParams:
    project_id_or_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id_or_slug', 'style': 'simple', 'explode': False }})
    user_data_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'user_data_id', 'style': 'simple', 'explode': False }})
    

@dataclass_json
@dataclasses.dataclass
class PutProjectUserDataRequestBodyDataAttributes:
    content: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('content') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    
class PutProjectUserDataRequestBodyDataTypeEnum(str, Enum):
    USER_DATA = "user_data"


@dataclass_json
@dataclasses.dataclass
class PutProjectUserDataRequestBodyData:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    type: PutProjectUserDataRequestBodyDataTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    attributes: Optional[PutProjectUserDataRequestBodyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes') }})
    

@dataclass_json
@dataclasses.dataclass
class PutProjectUserDataRequestBody:
    data: PutProjectUserDataRequestBodyData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class PutProjectUserDataSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class PutProjectUserDataRequest:
    path_params: PutProjectUserDataPathParams = dataclasses.field()
    security: PutProjectUserDataSecurity = dataclasses.field()
    request: Optional[PutProjectUserDataRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class PutProjectUserDataResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    user_data: Optional[shared_user_data.UserData] = dataclasses.field(default=None)
    