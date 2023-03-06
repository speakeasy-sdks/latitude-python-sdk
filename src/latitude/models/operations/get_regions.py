from __future__ import annotations
import dataclasses
import requests
from ..shared import regions as shared_regions
from typing import Optional


@dataclasses.dataclass
class GetRegionsSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetRegionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    regions: Optional[shared_regions.Regions] = dataclasses.field(default=None)
    