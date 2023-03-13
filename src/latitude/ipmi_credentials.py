import requests as requests_http
from . import utils
from latitude.models import operations, shared
from typing import Optional

class IPMICredentials:
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
        
    def create_ipmi_session(self, request: operations.CreateIpmiSessionRequest, security: operations.CreateIpmiSessionSecurity) -> operations.CreateIpmiSessionResponse:
        r"""Generate IPMI credentials
        Generates IPMI credentials for a given server. Remote access creates a VPN connection to the internal network of your server so you can connect to its IPMI.
        You will have to use a VPN client such as https://openvpn.net to connect. See `VPN Sessions` API to create a VPN connection.
        
        Related guide: https://docs.latitude.sh/docs/ipmi
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/servers/{id}/remote_access', request.path_params)
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateIpmiSessionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.IpmiSession])
                res.ipmi_session = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    