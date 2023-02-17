import dataclasses
from ..shared import error_object as shared_error_object
from ..shared import security as shared_security
from ..shared import virtual_network_assignment as shared_virtual_network_assignment
from dataclasses_json import dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class AssignServerVirtualNetworkRequestBodyDataAttributes:
    server_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('server_id') }})
    virtual_network_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('virtual_network_id') }})
    
class AssignServerVirtualNetworkRequestBodyDataTypeEnum(str, Enum):
    VIRTUAL_NETWORK_ASSIGNMENT = "virtual_network_assignment"


@dataclass_json
@dataclasses.dataclass
class AssignServerVirtualNetworkRequestBodyData:
    type: AssignServerVirtualNetworkRequestBodyDataTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    attributes: Optional[AssignServerVirtualNetworkRequestBodyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes') }})
    

@dataclass_json
@dataclasses.dataclass
class AssignServerVirtualNetworkRequestBody:
    data: Optional[AssignServerVirtualNetworkRequestBodyData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class AssignServerVirtualNetworkSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class AssignServerVirtualNetworkRequest:
    security: AssignServerVirtualNetworkSecurity = dataclasses.field()
    request: Optional[AssignServerVirtualNetworkRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class AssignServerVirtualNetworkResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    virtual_network_assignment: Optional[shared_virtual_network_assignment.VirtualNetworkAssignment] = dataclasses.field(default=None)
    