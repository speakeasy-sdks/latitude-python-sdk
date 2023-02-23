from __future__ import annotations
import dataclasses
from ..shared import user_include as shared_user_include
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from latitude import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SSHKeyDataAttributes:
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'exclude': lambda f: f is None }})
    fingerprint: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fingerprint'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    public_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('public_key'), 'exclude': lambda f: f is None }})
    updated_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('updated_at'), 'exclude': lambda f: f is None }})
    user: Optional[shared_user_include.UserInclude] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('user'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SSHKeyDataRelationships:
    projects: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('projects'), 'exclude': lambda f: f is None }})
    user: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('user'), 'exclude': lambda f: f is None }})
    
class SSHKeyDataTypeEnum(str, Enum):
    SSH_KEYS = "ssh_keys"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SSHKeyData:
    type: SSHKeyDataTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    attributes: Optional[SSHKeyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    relationships: Optional[SSHKeyDataRelationships] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('relationships'), 'exclude': lambda f: f is None }})
    