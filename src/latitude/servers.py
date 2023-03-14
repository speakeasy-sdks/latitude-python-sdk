import requests as requests_http
from . import utils
from latitude.models import operations, shared
from typing import Optional

class Servers:
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
        
    def create_server(self, request: operations.CreateServerRequest, security: operations.CreateServerSecurity) -> operations.CreateServerResponse:
        r"""Deploy a new server
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/servers'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateServerResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Server])
                res.server = out
        elif http_res.status_code in [400, 422]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    def destroy_server(self, request: operations.DestroyServerRequest, security: operations.DestroyServerSecurity) -> operations.DestroyServerResponse:
        r"""Remove a Server
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/servers/{server_id}', request.path_params)
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DestroyServerResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        elif http_res.status_code in [403, 406, 422]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    def get_server(self, request: operations.GetServerRequest, security: operations.GetServerSecurity) -> operations.GetServerResponse:
        r"""Retrieve a Server
        Returns a server that belongs to the team.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/servers/{server_id}', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetServerResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Server])
                res.server = out

        return res

    def get_servers(self, request: operations.GetServersRequest, security: operations.GetServersSecurity) -> operations.GetServersResponse:
        r"""List all Servers
        Returns a list of all servers belonging to the team.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/servers'
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetServersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Servers])
                res.servers = out

        return res

    def update_server(self, request: operations.UpdateServerRequest, security: operations.UpdateServerSecurity) -> operations.UpdateServerResponse:
        r"""Update a Server
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/servers/{server_id}', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateServerResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code in [200, 400]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Server])
                res.server = out

        return res

    