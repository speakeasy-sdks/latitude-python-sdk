import dataclasses
from ..shared import regions as shared_regions
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class GetRegionsSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetRegionsRequest:
    security: GetRegionsSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetRegionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    regions: Optional[shared_regions.Regions] = dataclasses.field(default=None)
    