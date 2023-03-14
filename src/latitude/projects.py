import requests as requests_http
from . import utils
from latitude.models import operations, shared
from typing import Optional

class Projects:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    def create_project(self, request: operations.CreateProjectRequest, security: operations.CreateProjectSecurity) -> operations.CreateProjectResponse:
        r"""Create a Project
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/projects'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateProjectResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateProject201ApplicationJSON])
                res.create_project_201_application_json_object = out
        elif http_res.status_code in [400, 403, 422]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    def delete_project(self, request: operations.DeleteProjectRequest, security: operations.DeleteProjectSecurity) -> operations.DeleteProjectResponse:
        r"""Delete a Project
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/projects/{id_or_slug}', request.path_params)
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteProjectResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteProject200ApplicationJSON])
                res.delete_project_200_application_json_object = out
        elif http_res.status_code in [403, 406]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    def get_project(self, request: operations.GetProjectRequest, security: operations.GetProjectSecurity) -> operations.GetProjectResponse:
        r"""Retrieve a Project
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/projects/{id_or_slug}', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetProjectResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetProject200ApplicationJSON])
                res.get_project_200_application_json_object = out

        return res

    def get_projects(self, request: operations.GetProjectsRequest, security: operations.GetProjectsSecurity) -> operations.GetProjectsResponse:
        r"""List all Projects
        Returns a list of all projects for the current team
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/projects'
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetProjectsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Projects])
                res.projects = out

        return res

    def update_project(self, request: operations.UpdateProjectRequest, security: operations.UpdateProjectSecurity) -> operations.UpdateProjectResponse:
        r"""Update a Project
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/projects/{id_or_slug}', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateProjectResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateProject200ApplicationJSON])
                res.update_project_200_application_json_object = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    