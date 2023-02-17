import dataclasses
from ..shared import projects as shared_projects
from ..shared import security as shared_security
from typing import Optional


@dataclasses.dataclass
class GetProjectsQueryParams:
    extra_fields_projects_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'extra_fields[projects]', 'style': 'form', 'explode': True }})
    filter_billing_type_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[billing_type]', 'style': 'form', 'explode': True }})
    filter_description_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[description]', 'style': 'form', 'explode': True }})
    filter_environment_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[environment]', 'style': 'form', 'explode': True }})
    filter_name_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[name]', 'style': 'form', 'explode': True }})
    filter_slug_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter[slug]', 'style': 'form', 'explode': True }})
    include: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'include', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetProjectsSecurity:
    bearer: shared_security.SchemeBearer = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    

@dataclasses.dataclass
class GetProjectsRequest:
    query_params: GetProjectsQueryParams = dataclasses.field()
    security: GetProjectsSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetProjectsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    projects: Optional[shared_projects.Projects] = dataclasses.field(default=None)
    