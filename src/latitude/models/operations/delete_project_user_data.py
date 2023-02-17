import dataclasses
from ..shared import security as shared_security


@dataclasses.dataclass
class DeleteProjectUserDataPathParams:
    project_id_or_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id_or_slug', 'style': 'simple', 'explode': False }})
    user_data_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'user_data_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteProjectUserDataSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class DeleteProjectUserDataRequest:
    path_params: DeleteProjectUserDataPathParams = dataclasses.field()
    security: DeleteProjectUserDataSecurity = dataclasses.field()
    

@dataclasses.dataclass
class DeleteProjectUserDataResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    