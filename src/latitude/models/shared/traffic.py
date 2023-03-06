from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TrafficDataAttributesRegionsData:
    avg_inbound_speed_mbps: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('avg_inbound_speed_mbps'), 'exclude': lambda f: f is None }})
    avg_outbound_speed_mbps: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('avg_outbound_speed_mbps'), 'exclude': lambda f: f is None }})
    date_: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('date'), 'exclude': lambda f: f is None }})
    inbound_gb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('inbound_gb'), 'exclude': lambda f: f is None }})
    outbound_gb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('outbound_gb'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TrafficDataAttributesRegions:
    data: Optional[list[TrafficDataAttributesRegionsData]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    region_slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region_slug'), 'exclude': lambda f: f is None }})
    total_inbound_95th_percentile_mbps: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_inbound_95th_percentile_mbps'), 'exclude': lambda f: f is None }})
    total_inbound_gb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_inbound_gb'), 'exclude': lambda f: f is None }})
    total_outbound_95th_percentile_mbps: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_outbound_95th_percentile_mbps'), 'exclude': lambda f: f is None }})
    total_outbound_gb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_outbound_gb'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TrafficDataAttributes:
    from_date: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from_date'), 'exclude': lambda f: f is None }})
    regions: Optional[list[TrafficDataAttributesRegions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('regions'), 'exclude': lambda f: f is None }})
    to_date: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('to_date'), 'exclude': lambda f: f is None }})
    total_inbound_95th_percentile_mbps: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_inbound_95th_percentile_mbps'), 'exclude': lambda f: f is None }})
    total_inbound_gb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_inbound_gb'), 'exclude': lambda f: f is None }})
    total_outbound_95th_percentile_mbps: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_outbound_95th_percentile_mbps'), 'exclude': lambda f: f is None }})
    total_outbound_gb: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_outbound_gb'), 'exclude': lambda f: f is None }})
    
class TrafficDataTypeEnum(str, Enum):
    TRAFFIC = "traffic"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TrafficData:
    attributes: Optional[TrafficDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attributes'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    type: Optional[TrafficDataTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Traffic:
    data: Optional[TrafficData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    