from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import error_object as shared_error_object
from ..shared import server as shared_server
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from latitudeapi import utils
from typing import Optional


@dataclasses.dataclass
class CreateServerSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    
class CreateServerRequestBodyDataAttributesOperatingSystemEnum(str, Enum):
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

class CreateServerRequestBodyDataAttributesPlanEnum(str, Enum):
    C1_LARGE_X86 = "c1-large-x86"
    C1_MEDIUM_X86 = "c1-medium-x86"
    C1_SMALL_X86 = "c1-small-x86"
    C1_TINY_X86 = "c1-tiny-x86"
    C2_LARGE_ARM = "c2-large-arm"
    C2_LARGE_X86 = "c2-large-x86"
    C2_MEDIUM_X86 = "c2-medium-x86"
    C2_SMALL_X86 = "c2-small-x86"
    T1_SPOT1 = "t1-spot1"

class CreateServerRequestBodyDataAttributesRaidEnum(str, Enum):
    RAID_0 = "raid-0"
    RAID_1 = "raid-1"
    NULL = "null"

class CreateServerRequestBodyDataAttributesSiteEnum(str, Enum):
    CH1 = "CH1"
    BGT = "BGT"
    BUE = "BUE"
    ASH = "ASH"
    DAL2 = "DAL2"
    LA2 = "LA2"
    MH1 = "MH1"
    MI1 = "MI1"
    NY2 = "NY2"
    SAN = "SAN"
    SP1 = "SP1"
    SP2 = "SP2"
    SYD = "SYD"
    TY6 = "TY6"
    TY8 = "TY8"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateServerRequestBodyDataAttributes:
    hostname: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hostname'), 'exclude': lambda f: f is None }})
    operating_system: Optional[CreateServerRequestBodyDataAttributesOperatingSystemEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operating_system'), 'exclude': lambda f: f is None }})
    plan: Optional[CreateServerRequestBodyDataAttributesPlanEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plan'), 'exclude': lambda f: f is None }})
    project: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project'), 'exclude': lambda f: f is None }})
    raid: Optional[CreateServerRequestBodyDataAttributesRaidEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raid'), 'exclude': lambda f: f is None }})
    site: Optional[CreateServerRequestBodyDataAttributesSiteEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('site'), 'exclude': lambda f: f is None }})
    ssh_keys: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_keys'), 'exclude': lambda f: f is None }})
    user_data: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_data'), 'exclude': lambda f: f is None }})
    
class CreateServerRequestBodyDataTypeEnum(str, Enum):
    SERVERS = "servers"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateServerRequestBodyData:
    type: CreateServerRequestBodyDataTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    attributes: Optional[CreateServerRequestBodyDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attributes'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateServerRequestBody:
    data: Optional[CreateServerRequestBodyData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class CreateServerRequest:
    request: Optional[CreateServerRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateServerResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    server: Optional[shared_server.Server] = dataclasses.field(default=None)
    