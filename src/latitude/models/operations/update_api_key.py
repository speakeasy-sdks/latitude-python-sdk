import dataclasses
from ..shared import api_key as shared_api_key
from ..shared import error_object as shared_error_object
from ..shared import security as shared_security
from ..shared import update_api_key as shared_update_api_key
from dataclasses_json import dataclass_json
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class UpdateAPIKeyPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateAPIKeySecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class UpdateAPIKeyRequest:
    path_params: UpdateAPIKeyPathParams = dataclasses.field()
    security: UpdateAPIKeySecurity = dataclasses.field()
    request: Optional[shared_update_api_key.UpdateAPIKey] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class UpdateAPIKey200ApplicationJSON:
    data: Optional[shared_api_key.APIKey] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class UpdateAPIKeyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    update_api_key_200_application_json_object: Optional[UpdateAPIKey200ApplicationJSON] = dataclasses.field(default=None)
    