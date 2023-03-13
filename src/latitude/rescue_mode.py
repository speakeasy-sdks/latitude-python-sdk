import requests as requests_http
from . import utils
from latitude.models import operations, shared
from typing import Optional

class RescueMode:
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
        
    def server_exit_rescue_mode(self, request: operations.ServerExitRescueModeRequest, security: operations.ServerExitRescueModeSecurity) -> operations.ServerExitRescueModeResponse:
        r"""Exits rescue mode for a Server
        Exits rescue mode on a given server.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/servers/{server_id}/exit_rescue_mode', request.path_params)
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ServerExitRescueModeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ServerRescue])
                res.server_rescue = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out
        elif http_res.status_code == 406:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    def server_start_rescue_mode(self, request: operations.ServerStartRescueModeRequest, security: operations.ServerStartRescueModeSecurity) -> operations.ServerStartRescueModeResponse:
        r"""Puts a Server in rescue mode
        Starts rescue mode on a given server.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/servers/{server_id}/rescue_mode', request.path_params)
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ServerStartRescueModeResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ServerRescue])
                res.server_rescue = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out
        elif http_res.status_code == 406:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    