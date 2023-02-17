import dataclasses
from ..shared import security as shared_security
from ..shared import ssh_key_data as shared_ssh_key_data
from dataclasses_json import dataclass_json
from latitude import utils
from typing import Optional


@dataclasses.dataclass
class GetProjectSSHKeyPathParams:
    project_id_or_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id_or_slug', 'style': 'simple', 'explode': False }})
    ssh_key_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ssh_key_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetProjectSSHKeyQueryParams:
    include: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'include', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetProjectSSHKeySecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetProjectSSHKeyRequest:
    path_params: GetProjectSSHKeyPathParams = dataclasses.field()
    query_params: GetProjectSSHKeyQueryParams = dataclasses.field()
    security: GetProjectSSHKeySecurity = dataclasses.field()
    

@dataclass_json
@dataclasses.dataclass
class GetProjectSSHKey200ApplicationJSON:
    data: Optional[shared_ssh_key_data.SSHKeyData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclasses.dataclass
class GetProjectSSHKeyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_project_ssh_key_200_application_json_object: Optional[GetProjectSSHKey200ApplicationJSON] = dataclasses.field(default=None)
    