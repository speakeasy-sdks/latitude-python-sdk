import dataclasses
from ..shared import project_include as shared_project_include
from ..shared import region_resource_data as shared_region_resource_data
from ..shared import team_include as shared_team_include
from dataclasses_json import dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional

class ServerDataAttributesIpmiStatusEnum(str, Enum):
    UNAVAILABLE = "Unavailable"
    INTERMITTENT = "Intermittent"
    NORMAL = "Normal"


@dataclass_json
@dataclasses.dataclass
class ServerDataAttributesOperatingSystemDistro:
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    series: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('series') }})
    slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('slug') }})
    

@dataclass_json
@dataclasses.dataclass
class ServerDataAttributesOperatingSystemFeatures:
    raid: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('raid') }})
    ssh_keys: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ssh_keys') }})
    user_data: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('user_data') }})
    

@dataclass_json
@dataclasses.dataclass
class ServerDataAttributesOperatingSystem:
    distro: Optional[ServerDataAttributesOperatingSystemDistro] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('distro') }})
    features: Optional[ServerDataAttributesOperatingSystemFeatures] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('features') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('slug') }})
    version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('version') }})
    

@dataclass_json
@dataclasses.dataclass
class ServerDataAttributesPlan:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    

@dataclass_json
@dataclasses.dataclass
class ServerDataAttributesSpecs:
    cpu: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('cpu') }})
    disk: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('disk') }})
    ram: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ram') }})
    
class ServerDataAttributesStatusEnum(str, Enum):
    ON = "on"
    OFF = "off"
    UNKNOWN = "unknown"
    READY = "ready"
    DISK_ERASING = "disk_erasing"
    FAILED_DISK_ERASING = "failed_disk_erasing"
    DEPLOYING = "deploying"
    FAILED_DEPLOYMENT = "failed_deployment"


@dataclass_json
@dataclasses.dataclass
class ServerDataAttributes:
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at') }})
    hostname: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hostname') }})
    ipmi_status: Optional[ServerDataAttributesIpmiStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ipmi_status') }})
    operating_system: Optional[ServerDataAttributesOperatingSystem] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('operating_system') }})
    plan: Optional[ServerDataAttributesPlan] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('plan') }})
    primary_ipv4: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('primary_ipv4') }})
    project: Optional[shared_project_include.ProjectInclude] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('project') }})
    region: Optional[shared_region_resource_data.RegionResourceData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('region') }})
    role: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('role') }})
    site: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('site') }})
    specs: Optional[ServerDataAttributesSpecs] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('specs') }})
    status: Optional[ServerDataAttributesStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status') }})
    team: Optional[shared_team_include.TeamInclude] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('team') }})
    

@dataclass_json
@dataclasses.dataclass
class ServerData:
    attributes: Optional[ServerDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    