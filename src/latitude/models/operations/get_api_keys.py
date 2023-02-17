import dataclasses
from ..shared import api_key as shared_api_key
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class GetAPIKeysSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetAPIKeysRequest:
    security: GetAPIKeysSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetAPIKeysResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    api_key: Optional[shared_api_key.APIKey] = dataclasses.field(default=None)
    