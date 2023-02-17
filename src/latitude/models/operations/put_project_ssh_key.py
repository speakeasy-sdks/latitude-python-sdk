import dataclasses
from ..shared import security as shared_security
from ..shared import ssh_key_data as shared_ssh_key_data
from dataclasses_json import dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class PutProjectSSHKeyPathParams:
    project_id_or_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id_or_slug', 'style': 'simple', 'explode': False }})
    ssh_key_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ssh_key_id', 'style': 'simple', 'explode': False }})
    

@dataclass_json
@dataclasses.dataclass
class PutProjectSSHKeyRequestBodyDataAttributes:
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    
class PutProjectSSHKeyRequestBodyDataTypeEnum(str, Enum):
    SSH_KEYS = "ssh_keys"


@dataclass_json
@dataclasses.dataclass
class PutProjectSSHKeyRequestBodyData:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    type: PutProjectSSHKeyRequestBodyDataTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    attributes: Optional[PutProjectSSHKeyRequestBodyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes') }})
    

@dataclass_json
@dataclasses.dataclass
class PutProjectSSHKeyRequestBody:
    data: PutProjectSSHKeyRequestBodyData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class PutProjectSSHKeySecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class PutProjectSSHKeyRequest:
    path_params: PutProjectSSHKeyPathParams = dataclasses.field()
    security: PutProjectSSHKeySecurity = dataclasses.field()
    request: Optional[PutProjectSSHKeyRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json
@dataclasses.dataclass
class PutProjectSSHKey200ApplicationJSON:
    data: Optional[shared_ssh_key_data.SSHKeyData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class PutProjectSSHKeyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    put_project_ssh_key_200_application_json_object: Optional[PutProjectSSHKey200ApplicationJSON] = dataclasses.field(default=None)
    