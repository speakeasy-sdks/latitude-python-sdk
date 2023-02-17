import requests
from . import utils
from latitude.models import operations, shared
from typing import Optional

class UserData:
    _client: requests.Session
    _security_client: requests.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests.Session, security_client: requests.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version

    
    def delete_project_user_data(self, request: operations.DeleteProjectUserDataRequest) -> operations.DeleteProjectUserDataResponse:
        r"""Delete a Project User Data
        Allow you remove User Data in a project.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/projects/{project_id_or_slug}/user_data/{user_data_id}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteProjectUserDataResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass
        elif r.status_code == 404:
            pass

        return res

    
    def get_project_user_data(self, request: operations.GetProjectUserDataRequest) -> operations.GetProjectUserDataResponse:
        r"""Retrieve a Project User Data
        Get User Data in the project. These scripts can be used to configure servers with user data.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/projects/{project_id_or_slug}/user_data/{user_data_id}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetProjectUserDataResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.UserData])
                res.user_data = out

        return res

    
    def get_project_users_data(self, request: operations.GetProjectUsersDataRequest) -> operations.GetProjectUsersDataResponse:
        r"""List all Project User Data
        List all Users Data in the project. These scripts can be used to configure servers with user data.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/projects/{project_id_or_slug}/user_data", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetProjectUsersDataResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetProjectUsersData200ApplicationJSON])
                res.get_project_users_data_200_application_json_object = out

        return res

    
    def post_project_user_data(self, request: operations.PostProjectUserDataRequest) -> operations.PostProjectUserDataResponse:
        r"""Create a Project User Data
        Allows you to create User Data in a project, which can be used to perform custom setup on your servers after deploy and reinstall.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/projects/{project_id_or_slug}/user_data", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PostProjectUserDataResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.UserData])
                res.user_data = out
        elif r.status_code == 400:
            pass
        elif r.status_code == 422:
            pass

        return res

    
    def put_project_user_data(self, request: operations.PutProjectUserDataRequest) -> operations.PutProjectUserDataResponse:
        r"""Update a Project User Data
        Allow you update User Data in a project.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/projects/{project_id_or_slug}/user_data/{user_data_id}", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("PUT", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PutProjectUserDataResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.UserData])
                res.user_data = out
        elif r.status_code == 400:
            pass
        elif r.status_code == 422:
            pass

        return res

    