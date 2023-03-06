from __future__ import annotations
import dataclasses
import requests
from ..shared import user_data as shared_user_data
from typing import Optional


@dataclasses.dataclass
class GetProjectUserDataSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetProjectUserDataPathParams:
    project_id_or_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id_or_slug', 'style': 'simple', 'explode': False }})
    user_data_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'user_data_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetProjectUserDataQueryParams:
    extra_fields_user_data: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'extra_fields[user_data]', 'style': 'form', 'explode': True }})
    include: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'include', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetProjectUserDataRequest:
    path_params: GetProjectUserDataPathParams = dataclasses.field()
    query_params: GetProjectUserDataQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetProjectUserDataResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    user_data: Optional[shared_user_data.UserData] = dataclasses.field(default=None)
    