from __future__ import annotations
import dataclasses
from ..shared import project_include as shared_project_include
from ..shared import region_resource_data as shared_region_resource_data
from ..shared import team_include as shared_team_include
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional

class ServerDataAttributesIpmiStatusEnum(str, Enum):
    UNAVAILABLE = "Unavailable"
    INTERMITTENT = "Intermittent"
    NORMAL = "Normal"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ServerDataAttributesOperatingSystemDistro:
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    series: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('series'), 'exclude': lambda f: f is None }})
    slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('slug'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ServerDataAttributesOperatingSystemFeatures:
    raid: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('raid'), 'exclude': lambda f: f is None }})
    ssh_keys: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ssh_keys'), 'exclude': lambda f: f is None }})
    user_data: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('user_data'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ServerDataAttributesOperatingSystem:
    distro: Optional[ServerDataAttributesOperatingSystemDistro] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('distro'), 'exclude': lambda f: f is None }})
    features: Optional[ServerDataAttributesOperatingSystemFeatures] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('features'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('slug'), 'exclude': lambda f: f is None }})
    version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('version'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ServerDataAttributesPlan:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ServerDataAttributesSpecs:
    cpu: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('cpu'), 'exclude': lambda f: f is None }})
    disk: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('disk'), 'exclude': lambda f: f is None }})
    ram: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ram'), 'exclude': lambda f: f is None }})
    
class ServerDataAttributesStatusEnum(str, Enum):
    ON = "on"
    OFF = "off"
    UNKNOWN = "unknown"
    READY = "ready"
    DISK_ERASING = "disk_erasing"
    FAILED_DISK_ERASING = "failed_disk_erasing"
    DEPLOYING = "deploying"
    FAILED_DEPLOYMENT = "failed_deployment"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ServerDataAttributes:
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'exclude': lambda f: f is None }})
    hostname: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hostname'), 'exclude': lambda f: f is None }})
    ipmi_status: Optional[ServerDataAttributesIpmiStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ipmi_status'), 'exclude': lambda f: f is None }})
    operating_system: Optional[ServerDataAttributesOperatingSystem] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('operating_system'), 'exclude': lambda f: f is None }})
    plan: Optional[ServerDataAttributesPlan] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('plan'), 'exclude': lambda f: f is None }})
    primary_ipv4: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('primary_ipv4'), 'exclude': lambda f: f is None }})
    project: Optional[shared_project_include.ProjectInclude] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('project'), 'exclude': lambda f: f is None }})
    region: Optional[shared_region_resource_data.RegionResourceData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('region'), 'exclude': lambda f: f is None }})
    role: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('role'), 'exclude': lambda f: f is None }})
    site: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('site'), 'exclude': lambda f: f is None }})
    specs: Optional[ServerDataAttributesSpecs] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('specs'), 'exclude': lambda f: f is None }})
    status: Optional[ServerDataAttributesStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('status'), 'exclude': lambda f: f is None }})
    team: Optional[shared_team_include.TeamInclude] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('team'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ServerData:
    attributes: Optional[ServerDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    