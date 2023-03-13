from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from latitude import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeployConfigDataAttributes:
    hostname: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hostname'), 'exclude': lambda f: f is None }})
    operating_system: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operating_system'), 'exclude': lambda f: f is None }})
    raid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raid'), 'exclude': lambda f: f is None }})
    ssh_keys: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_keys'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeployConfigData:
    attributes: Optional[DeployConfigDataAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attributes'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeployConfig:
    data: Optional[DeployConfigData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    