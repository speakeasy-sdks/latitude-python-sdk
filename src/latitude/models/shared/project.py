from __future__ import annotations
import dataclasses
from ..shared import lazy_sideload as shared_lazy_sideload
from ..shared import team_include as shared_team_include
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProjectAttributesBilling:
    method: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method'), 'exclude': lambda f: f is None }})
    subscription_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subscription_id'), 'exclude': lambda f: f is None }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    
class ProjectAttributesBillingMethodEnum(str, Enum):
    NORMAL = "Normal"
    NINETY_FIVETH_PERCENTILE = "95th percentile"
    NULL = "null"

class ProjectAttributesBillingTypeEnum(str, Enum):
    YEARLY = "Yearly"
    MONTHLY = "Monthly"
    HOURLY = "Hourly"
    NULL = "null"

class ProjectAttributesEnvironmentEnum(str, Enum):
    DEVELOPMENT = "Development"
    STAGING = "Staging"
    PRODUCTION = "Production"
    NULL = "null"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProjectAttributesStats:
    ip_addresses: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ip_addresses'), 'exclude': lambda f: f is None }})
    prefixes: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prefixes'), 'exclude': lambda f: f is None }})
    servers: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('servers'), 'exclude': lambda f: f is None }})
    vlans: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vlans'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProjectAttributes:
    billing: Optional[ProjectAttributesBilling] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing'), 'exclude': lambda f: f is None }})
    billing_method: Optional[ProjectAttributesBillingMethodEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_method'), 'exclude': lambda f: f is None }})
    billing_type: Optional[ProjectAttributesBillingTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_type'), 'exclude': lambda f: f is None }})
    cost: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cost'), 'exclude': lambda f: f is None }})
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    environment: Optional[ProjectAttributesEnvironmentEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug'), 'exclude': lambda f: f is None }})
    stats: Optional[ProjectAttributesStats] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stats'), 'exclude': lambda f: f is None }})
    team: Optional[shared_team_include.TeamInclude] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('team'), 'exclude': lambda f: f is None }})
    updated_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProjectRelationships:
    billing: Optional[shared_lazy_sideload.LazySideload] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing'), 'exclude': lambda f: f is None }})
    team: Optional[shared_lazy_sideload.LazySideload] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('team'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Project:
    attributes: Optional[ProjectAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attributes'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    relationships: Optional[ProjectRelationships] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('relationships'), 'exclude': lambda f: f is None }})
    