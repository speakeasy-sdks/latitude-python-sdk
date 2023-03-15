import requests as requests_http
from . import utils
from latitude.models import operations, shared
from typing import Optional

class Roles:
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
        
    def get_role_id(self, request: operations.GetRoleIDRequest, security: operations.GetRoleIDSecurity) -> operations.GetRoleIDResponse:
        r"""Retrieve a Role
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetRoleIDRequest, base_url, '/roles/{id}', request)
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetRoleIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Role])
                res.role = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    def get_roles(self, security: operations.GetRolesSecurity) -> operations.GetRolesResponse:
        r"""List all Roles
        Returns a list of all roles that can be assigned to users
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/roles'
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetRolesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetRoles200ApplicationJSON])
                res.get_roles_200_application_json_object = out

        return res

    