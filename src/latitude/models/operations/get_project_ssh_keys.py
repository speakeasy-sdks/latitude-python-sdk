from __future__ import annotations
import dataclasses
from ..shared import security as shared_security
from ..shared import ssh_key as shared_ssh_key
from typing import Optional


@dataclasses.dataclass
class GetProjectSSHKeysPathParams:
    project_id_or_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id_or_slug', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetProjectSSHKeysQueryParams:
    include: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'include', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetProjectSSHKeysSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetProjectSSHKeysRequest:
    path_params: GetProjectSSHKeysPathParams = dataclasses.field()
    query_params: GetProjectSSHKeysQueryParams = dataclasses.field()
    security: GetProjectSSHKeysSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetProjectSSHKeysResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    ssh_key: Optional[shared_ssh_key.SSHKey] = dataclasses.field(default=None)
    