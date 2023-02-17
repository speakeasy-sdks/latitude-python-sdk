import dataclasses
from ..shared import api_key as shared_api_key
from ..shared import create_api_key as shared_create_api_key
from ..shared import error_object as shared_error_object
from ..shared import security as shared_security
from dataclasses_json import dataclass_json
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class PostAPIKeySecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class PostAPIKeyRequest:
    security: PostAPIKeySecurity = dataclasses.field()
    request: Optional[shared_create_api_key.CreateAPIKey] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class PostAPIKey201ApplicationJSON:
    data: Optional[shared_api_key.APIKey] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class PostAPIKeyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    post_api_key_201_application_json_object: Optional[PostAPIKey201ApplicationJSON] = dataclasses.field(default=None)
    