from __future__ import annotations
import dataclasses
from ..shared import security as shared_security
from ..shared import ssh_key_data as shared_ssh_key_data
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class PostProjectSSHKeyPathParams:
    project_id_or_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id_or_slug', 'style': 'simple', 'explode': False }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostProjectSSHKeyRequestBodyDataAttributes:
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    public_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('public_key'), 'exclude': lambda f: f is None }})
    
class PostProjectSSHKeyRequestBodyDataTypeEnum(str, Enum):
    SSH_KEYS = "ssh_keys"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostProjectSSHKeyRequestBodyData:
    type: PostProjectSSHKeyRequestBodyDataTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    attributes: Optional[PostProjectSSHKeyRequestBodyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostProjectSSHKeyRequestBody:
    data: PostProjectSSHKeyRequestBodyData = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class PostProjectSSHKeySecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class PostProjectSSHKeyRequest:
    path_params: PostProjectSSHKeyPathParams = dataclasses.field()
    security: PostProjectSSHKeySecurity = dataclasses.field()
    request: Optional[PostProjectSSHKeyRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostProjectSSHKey201ApplicationJSON:
    data: Optional[shared_ssh_key_data.SSHKeyData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class PostProjectSSHKeyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    post_project_ssh_key_201_application_json_object: Optional[PostProjectSSHKey201ApplicationJSON] = dataclasses.field(default=None)
    