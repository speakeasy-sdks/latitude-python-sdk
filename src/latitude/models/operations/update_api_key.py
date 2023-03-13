from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import api_key as shared_api_key
from ..shared import error_object as shared_error_object
from ..shared import update_api_key as shared_update_api_key
from dataclasses_json import Undefined, dataclass_json
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class UpdateAPIKeySecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class UpdateAPIKeyPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateAPIKeyRequest:
    path_params: UpdateAPIKeyPathParams = dataclasses.field()
    request: Optional[shared_update_api_key.UpdateAPIKey] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateAPIKey200ApplicationJSON:
    data: Optional[shared_api_key.APIKey] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class UpdateAPIKeyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    update_api_key_200_application_json_object: Optional[UpdateAPIKey200ApplicationJSON] = dataclasses.field(default=None)
    