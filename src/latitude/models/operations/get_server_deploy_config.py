import dataclasses
from ..shared import deploy_config as shared_deploy_config
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class GetServerDeployConfigPathParams:
    server_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'server_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetServerDeployConfigSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetServerDeployConfigRequest:
    path_params: GetServerDeployConfigPathParams = dataclasses.field()
    security: GetServerDeployConfigSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetServerDeployConfigResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    deploy_config: Optional[shared_deploy_config.DeployConfig] = dataclasses.field(default=None)
    