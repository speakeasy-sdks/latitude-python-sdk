import dataclasses
from ..shared import security as shared_security
from ..shared import virtual_network as shared_virtual_network
from dataclasses_json import dataclass_json
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class GetVirtualNetworkPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetVirtualNetworkSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetVirtualNetworkRequest:
    path_params: GetVirtualNetworkPathParams = dataclasses.field()
    security: GetVirtualNetworkSecurity = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetVirtualNetwork200ApplicationJSON:
    data: Optional[shared_virtual_network.VirtualNetwork] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class GetVirtualNetworkResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_virtual_network_200_application_json_object: Optional[GetVirtualNetwork200ApplicationJSON] = dataclasses.field(default=None)
    