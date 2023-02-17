import dataclasses
from ..shared import error_object as shared_error_object
from ..shared import security as shared_security
from ..shared import virtual_network as shared_virtual_network
from dataclasses_json import dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class CreateVirtualNetworkRequestBodyDataAttributes:
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    project: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('project') }})
    site: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('site') }})
    
class CreateVirtualNetworkRequestBodyDataTypeEnum(str, Enum):
    VIRTUAL_NETWORK = "virtual_network"


@dataclass_json
@dataclasses.dataclass
class CreateVirtualNetworkRequestBodyData:
    type: CreateVirtualNetworkRequestBodyDataTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    attributes: Optional[CreateVirtualNetworkRequestBodyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes') }})
    

@dataclass_json
@dataclasses.dataclass
class CreateVirtualNetworkRequestBody:
    data: CreateVirtualNetworkRequestBodyData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class CreateVirtualNetworkSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class CreateVirtualNetworkRequest:
    security: CreateVirtualNetworkSecurity = dataclasses.field()
    request: Optional[CreateVirtualNetworkRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateVirtualNetworkResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    virtual_network: Optional[shared_virtual_network.VirtualNetwork] = dataclasses.field(default=None)
    