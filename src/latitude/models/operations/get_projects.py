from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import projects as shared_projects
from typing import Optional


@dataclasses.dataclass
class GetProjectsSecurity:
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetProjectsQueryParams:
    extra_fields_projects: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'extra_fields[projects]', 'style': 'form', 'explode': True }})
    filter_billing_type: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[billing_type]', 'style': 'form', 'explode': True }})
    filter_description: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[description]', 'style': 'form', 'explode': True }})
    filter_environment: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[environment]', 'style': 'form', 'explode': True }})
    filter_name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[name]', 'style': 'form', 'explode': True }})
    filter_slug: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[slug]', 'style': 'form', 'explode': True }})
    include: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'include', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetProjectsRequest:
    query_params: GetProjectsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetProjectsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    projects: Optional[shared_projects.Projects] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    