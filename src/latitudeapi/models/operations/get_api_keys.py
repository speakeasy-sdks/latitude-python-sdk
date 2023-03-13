from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import api_key as shared_api_key
from typing import Optional


@dataclasses.dataclass
class GetAPIKeysSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetAPIKeysResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    api_key: Optional[shared_api_key.APIKey] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    