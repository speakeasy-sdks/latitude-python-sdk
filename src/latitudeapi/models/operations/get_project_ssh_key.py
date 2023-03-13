from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import ssh_key_data as shared_ssh_key_data
from dataclasses_json import Undefined, dataclass_json
from latitudeapi import utils
from typing import Optional


@dataclasses.dataclass
class GetProjectSSHKeySecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetProjectSSHKeyPathParams:
    project_id_or_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id_or_slug', 'style': 'simple', 'explode': False }})
    ssh_key_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ssh_key_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetProjectSSHKeyQueryParams:
    include: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'include', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetProjectSSHKeyRequest:
    path_params: GetProjectSSHKeyPathParams = dataclasses.field()
    query_params: GetProjectSSHKeyQueryParams = dataclasses.field()
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProjectSSHKey200ApplicationJSON:
    data: Optional[shared_ssh_key_data.SSHKeyData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    

@dataclasses.dataclass
class GetProjectSSHKeyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_project_ssh_key_200_application_json_object: Optional[GetProjectSSHKey200ApplicationJSON] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    