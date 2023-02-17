import dataclasses
from ..shared import error_object as shared_error_object
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class DeleteAPIKeyPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteAPIKeySecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class DeleteAPIKeyRequest:
    path_params: DeleteAPIKeyPathParams = dataclasses.field()
    security: DeleteAPIKeySecurity = dataclasses.field()
    

@dataclasses.dataclass
class DeleteAPIKeyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    