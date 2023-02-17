import dataclasses
from ..shared import security as shared_security


@dataclasses.dataclass
class DeleteProjectSSHKeyPathParams:
    project_id_or_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id_or_slug', 'style': 'simple', 'explode': False }})
    ssh_key_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ssh_key_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteProjectSSHKeySecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class DeleteProjectSSHKeyRequest:
    path_params: DeleteProjectSSHKeyPathParams = dataclasses.field()
    security: DeleteProjectSSHKeySecurity = dataclasses.field()
    

@dataclasses.dataclass
class DeleteProjectSSHKeyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    