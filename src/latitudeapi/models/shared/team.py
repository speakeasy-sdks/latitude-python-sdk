from __future__ import annotations
import dataclasses
from ..shared import lazy_sideload as shared_lazy_sideload
from ..shared import project_include as shared_project_include
from ..shared import user_include as shared_user_include
from dataclasses_json import Undefined, dataclass_json
from latitudeapi import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TeamAttributesBilling:
    customer_billing_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_billing_id'), 'exclude': lambda f: f is None }})
    id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TeamAttributes:
    address: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address'), 'exclude': lambda f: f is None }})
    billing: Optional[TeamAttributesBilling] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing'), 'exclude': lambda f: f is None }})
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'exclude': lambda f: f is None }})
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    owner: Optional[shared_user_include.UserInclude] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('owner'), 'exclude': lambda f: f is None }})
    projects: Optional[list[shared_project_include.ProjectInclude]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projects'), 'exclude': lambda f: f is None }})
    slug: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug'), 'exclude': lambda f: f is None }})
    updated_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updated_at'), 'exclude': lambda f: f is None }})
    users: Optional[list[shared_user_include.UserInclude]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('users'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TeamRelationships:
    billing: Optional[shared_lazy_sideload.LazySideload] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing'), 'exclude': lambda f: f is None }})
    owner: Optional[shared_lazy_sideload.LazySideload] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('owner'), 'exclude': lambda f: f is None }})
    projects: Optional[shared_lazy_sideload.LazySideload] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projects'), 'exclude': lambda f: f is None }})
    users: Optional[shared_lazy_sideload.LazySideload] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('users'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Team:
    attributes: Optional[TeamAttributes] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attributes'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    relationships: Optional[TeamRelationships] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('relationships'), 'exclude': lambda f: f is None }})
    