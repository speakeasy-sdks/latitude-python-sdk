import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class TrafficQuotaDataAttributesQuotaPerProjectQuotaPerRegionQuotaInMbps:
    additional: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additional') }})
    granted: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('granted') }})
    total: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('total') }})
    

@dataclass_json
@dataclasses.dataclass
class TrafficQuotaDataAttributesQuotaPerProjectQuotaPerRegionQuotaInTb:
    additional: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('additional') }})
    granted: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('granted') }})
    total: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('total') }})
    

@dataclass_json
@dataclasses.dataclass
class TrafficQuotaDataAttributesQuotaPerProjectQuotaPerRegion:
    quota_in_mbps: Optional[TrafficQuotaDataAttributesQuotaPerProjectQuotaPerRegionQuotaInMbps] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('quota_in_mbps') }})
    quota_in_tb: Optional[TrafficQuotaDataAttributesQuotaPerProjectQuotaPerRegionQuotaInTb] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('quota_in_tb') }})
    region_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('region_id') }})
    region_slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('region_slug') }})
    

@dataclass_json
@dataclasses.dataclass
class TrafficQuotaDataAttributesQuotaPerProject:
    billing_method: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('billing_method') }})
    project_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('project_id') }})
    project_slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('project_slug') }})
    quota_per_region: Optional[list[TrafficQuotaDataAttributesQuotaPerProjectQuotaPerRegion]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('quota_per_region') }})
    

@dataclass_json
@dataclasses.dataclass
class TrafficQuotaDataAttributes:
    quota_per_project: Optional[list[TrafficQuotaDataAttributesQuotaPerProject]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('quota_per_project') }})
    
class TrafficQuotaDataTypeEnum(str, Enum):
    TRAFFIC_QUOTA = "traffic_quota"


@dataclass_json
@dataclasses.dataclass
class TrafficQuotaData:
    attributes: Optional[TrafficQuotaDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    type: Optional[TrafficQuotaDataTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class TrafficQuota:
    data: Optional[TrafficQuotaData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    