import requests as requests_http
from . import utils
from latitude.models import operations, shared
from typing import Optional

class APIKeys:
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
        
    def delete_api_key(self, request: operations.DeleteAPIKeyRequest, security: operations.DeleteAPIKeySecurity) -> operations.DeleteAPIKeyResponse:
        r"""Delete an API Key
        Delete an existing API Key. Once deleted, the API Key can no longer be used to access the API.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/auth/api_keys/{id}', request.path_params)
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteAPIKeyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    def get_api_keys(self, security: operations.GetAPIKeysSecurity) -> operations.GetAPIKeysResponse:
        r"""List all API Keys
        Returns a list of all API keys for the current user
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/auth/api_keys'
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAPIKeysResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIKey])
                res.api_key = out

        return res

    def post_api_key(self, request: operations.PostAPIKeyRequest, security: operations.PostAPIKeySecurity) -> operations.PostAPIKeyResponse:
        r"""Create an API Key
        Create a new API Key that is tied to the current user account. The created API key is only listed ONCE upon creation. It can however be regenerated or deleted.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/auth/api_keys'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostAPIKeyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostAPIKey201ApplicationJSON])
                res.post_api_key_201_application_json_object = out
        elif http_res.status_code in [400, 422]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    def update_api_key(self, request: operations.UpdateAPIKeyRequest, security: operations.UpdateAPIKeySecurity) -> operations.UpdateAPIKeyResponse:
        r"""Regenerate an API Key
        Regenerate an existing API Key that is tied to the current user. This overrides the previous key.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/auth/api_keys/{id}', request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateAPIKeyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateAPIKey200ApplicationJSON])
                res.update_api_key_200_application_json_object = out
        elif http_res.status_code in [400, 404, 422]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    