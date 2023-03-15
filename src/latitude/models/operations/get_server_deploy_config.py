from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import deploy_config as shared_deploy_config
from typing import Optional


@dataclasses.dataclass
class GetServerDeployConfigSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetServerDeployConfigRequest:
    server_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'server_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetServerDeployConfigResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    deploy_config: Optional[shared_deploy_config.DeployConfig] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    