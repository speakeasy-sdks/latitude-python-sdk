from __future__ import annotations
import dataclasses
from ..shared import error_object as shared_error_object
from ..shared import security as shared_security
from ..shared import virtual_network as shared_virtual_network
from typing import Optional


@dataclasses.dataclass
class DestroyVirtualNetworkPathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DestroyVirtualNetworkSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class DestroyVirtualNetworkRequest:
    path_params: DestroyVirtualNetworkPathParams = dataclasses.field()
    security: DestroyVirtualNetworkSecurity = dataclasses.field()
    

@dataclasses.dataclass
class DestroyVirtualNetworkResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    virtual_network: Optional[shared_virtual_network.VirtualNetwork] = dataclasses.field(default=None)
    