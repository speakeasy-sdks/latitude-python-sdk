from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import deploy_config as shared_deploy_config
from ..shared import error_object as shared_error_object
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from latitudeapi import utils
from typing import Optional


@dataclasses.dataclass
class UpdateServerDeployConfigSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class UpdateServerDeployConfigPathParams:
    server_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'server_id', 'style': 'simple', 'explode': False }})
    
class UpdateServerDeployConfigRequestBodyAttributesOperatingSystemEnum(str, Enum):
    WINDOWS_SERVER_2019_STD_V1 = "windows_server_2019_std_v1"
    WINDOWS_SERVER_2019_DC_V1 = "windows_server_2019_dc_v1"
    WINDOWS_SERVER_2016_STD_V1 = "windows_server_2016_std_v1"
    WINDOWS_SERVER_2016_DC_V1 = "windows_server_2016_dc_v1"
    UBUNTU_22_04_X64_LTS = "ubuntu_22_04_x64_lts"
    DEBIAN_11 = "debian_11"
    ROCKYLINUX_8 = "rockylinux_8"
    DEBIAN_10 = "debian_10"
    FLATCAR_STABLE = "flatcar_stable"
    RHEL8 = "rhel8"
    CENTOS_7_4_X64 = "centos_7_4_x64"
    CENTOS_8_X64 = "centos_8_x64"
    UBUNTU_18_04_X64_LTS = "ubuntu_18_04_x64_lts"
    UBUNTU_20_04_X64_LTS = "ubuntu_20_04_x64_lts"
    NULL = "null"

class UpdateServerDeployConfigRequestBodyAttributesRaidEnum(str, Enum):
    RAID_0 = "raid-0"
    RAID_1 = "raid-1"
    NULL = "null"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateServerDeployConfigRequestBodyAttributes:
    hostname: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hostname'), 'exclude': lambda f: f is None }})
    operating_system: Optional[UpdateServerDeployConfigRequestBodyAttributesOperatingSystemEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operating_system'), 'exclude': lambda f: f is None }})
    raid: Optional[UpdateServerDeployConfigRequestBodyAttributesRaidEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raid'), 'exclude': lambda f: f is None }})
    ssh_keys: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_keys'), 'exclude': lambda f: f is None }})
    user_data: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_data'), 'exclude': lambda f: f is None }})
    
class UpdateServerDeployConfigRequestBodyTypeEnum(str, Enum):
    DEPLOY_CONFIG = "deploy_config"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateServerDeployConfigRequestBody:
    type: UpdateServerDeployConfigRequestBodyTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    attributes: Optional[UpdateServerDeployConfigRequestBodyAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attributes'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class UpdateServerDeployConfigRequest:
    path_params: UpdateServerDeployConfigPathParams = dataclasses.field()
    request: Optional[UpdateServerDeployConfigRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdateServerDeployConfigResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    deploy_config: Optional[shared_deploy_config.DeployConfig] = dataclasses.field(default=None)
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    