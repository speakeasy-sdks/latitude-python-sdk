import dataclasses
from ..shared import security as shared_security


@dataclasses.dataclass
class GetCurrentVersionSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetCurrentVersionRequest:
    security: GetCurrentVersionSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetCurrentVersionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    