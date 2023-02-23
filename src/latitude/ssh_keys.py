import requests
from . import utils
from latitude.models import operations, shared
from typing import Optional

class SSHKeys:
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

    
    def delete_project_ssh_key(self, request: operations.DeleteProjectSSHKeyRequest) -> operations.DeleteProjectSSHKeyResponse:
        r"""Delete a Project SSH Key
        Allow you remove SSH Keys in a project. Remove a SSH Key from the project won't revoke the SSH Keys access for previously deploy and reinstall actions.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/projects/{project_id_or_slug}/ssh_keys/{ssh_key_id}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteProjectSSHKeyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass
        elif r.status_code == 404:
            pass

        return res

    
    def get_project_ssh_key(self, request: operations.GetProjectSSHKeyRequest) -> operations.GetProjectSSHKeyResponse:
        r"""Retrieve a Project SSH Key
        List all SSH Keys in the project. These keys can be used to access servers after deploy and reinstall actions.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/projects/{project_id_or_slug}/ssh_keys/{ssh_key_id}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetProjectSSHKeyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetProjectSSHKey200ApplicationJSON])
                res.get_project_ssh_key_200_application_json_object = out

        return res

    
    def get_project_ssh_keys(self, request: operations.GetProjectSSHKeysRequest) -> operations.GetProjectSSHKeysResponse:
        r"""List all Project SSH Keys
        List all SSH Keys in the project. These keys can be used to access servers after deploy and reinstall actions.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/projects/{project_id_or_slug}/ssh_keys", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetProjectSSHKeysResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.SSHKey])
                res.ssh_key = out

        return res

    
    def post_project_ssh_key(self, request: operations.PostProjectSSHKeyRequest) -> operations.PostProjectSSHKeyResponse:
        r"""Create a Project SSH Key
        Allow you create SSH Keys in a project. These keys can be used to access servers after deploy and reinstall actions.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/projects/{project_id_or_slug}/ssh_keys", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PostProjectSSHKeyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PostProjectSSHKey201ApplicationJSON])
                res.post_project_ssh_key_201_application_json_object = out
        elif r.status_code == 400:
            pass
        elif r.status_code == 422:
            pass

        return res

    
    def put_project_ssh_key(self, request: operations.PutProjectSSHKeyRequest) -> operations.PutProjectSSHKeyResponse:
        r"""Update a Project SSH Key
        Allow you update SSH Key in a project. These keys can be used to access servers after deploy and reinstall actions.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/projects/{project_id_or_slug}/ssh_keys/{ssh_key_id}", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PutProjectSSHKeyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PutProjectSSHKey200ApplicationJSON])
                res.put_project_ssh_key_200_application_json_object = out
        elif r.status_code == 400:
            pass
        elif r.status_code == 422:
            pass

        return res

    