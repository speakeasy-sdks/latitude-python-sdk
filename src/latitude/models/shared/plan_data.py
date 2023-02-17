import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from latitude import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class PlanDataAttributesAvailableInPricingBRL:
    month: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('month') }})
    

@dataclass_json
@dataclasses.dataclass
class PlanDataAttributesAvailableInPricingUSD:
    month: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('month') }})
    

@dataclass_json
@dataclasses.dataclass
class PlanDataAttributesAvailableInPricing:
    brl: Optional[PlanDataAttributesAvailableInPricingBRL] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('BRL') }})
    usd: Optional[PlanDataAttributesAvailableInPricingUSD] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('USD') }})
    

@dataclass_json
@dataclasses.dataclass
class PlanDataAttributesAvailableInRegion:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('slug') }})
    

@dataclass_json
@dataclasses.dataclass
class PlanDataAttributesAvailableInSites:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    in_stock: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('in_stock') }})
    instant: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('instant') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('slug') }})
    stock_level: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('stock_level') }})
    

@dataclass_json
@dataclasses.dataclass
class PlanDataAttributesAvailableIn:
    pricing: Optional[PlanDataAttributesAvailableInPricing] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('pricing') }})
    region: Optional[PlanDataAttributesAvailableInRegion] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('region') }})
    sites: Optional[list[PlanDataAttributesAvailableInSites]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sites') }})
    

@dataclass_json
@dataclasses.dataclass
class PlanDataAttributesSpecsCpus:
    clock: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('clock') }})
    cores: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('cores') }})
    count: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('count') }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    
class PlanDataAttributesSpecsDrivesTypeEnum(str, Enum):
    SSD = "SSD"
    HDD = "HDD"


@dataclass_json
@dataclasses.dataclass
class PlanDataAttributesSpecsDrives:
    count: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('count') }})
    size: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('size') }})
    type: Optional[PlanDataAttributesSpecsDrivesTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class PlanDataAttributesSpecsFeatures:
    custom_scripts: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('custom_scripts') }})
    raid: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('raid') }})
    ssh: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ssh') }})
    

@dataclass_json
@dataclasses.dataclass
class PlanDataAttributesSpecsMemory:
    total: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('total') }})
    

@dataclass_json
@dataclasses.dataclass
class PlanDataAttributesSpecsNics:
    count: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('count') }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class PlanDataAttributesSpecs:
    cpus: Optional[list[PlanDataAttributesSpecsCpus]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('cpus') }})
    drives: Optional[list[PlanDataAttributesSpecsDrives]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('drives') }})
    features: Optional[PlanDataAttributesSpecsFeatures] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('features') }})
    memory: Optional[PlanDataAttributesSpecsMemory] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('memory') }})
    nics: Optional[list[PlanDataAttributesSpecsNics]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nics') }})
    

@dataclass_json
@dataclasses.dataclass
class PlanDataAttributes:
    available_in: Optional[list[PlanDataAttributesAvailableIn]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('available_in') }})
    line: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('line') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('slug') }})
    specs: Optional[PlanDataAttributesSpecs] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('specs') }})
    
class PlanDataTypeEnum(str, Enum):
    PLANS = "plans"


@dataclass_json
@dataclasses.dataclass
class PlanData:
    attributes: Optional[PlanDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    type: Optional[PlanDataTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    