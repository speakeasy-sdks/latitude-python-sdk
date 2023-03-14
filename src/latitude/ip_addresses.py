import requests as requests_http
from . import utils
from latitude.models import operations, shared
from typing import Optional

class IPAddresses:
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
        
    def get_ip(self, request: operations.GetIPRequest, security: operations.GetIPSecurity) -> operations.GetIPResponse:
        r"""Retrieve an IP
        Retrieve an IP Address
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/ips/{id}', request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetIPResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.IPAddress])
                res.ip_address = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    def get_ips(self, request: operations.GetIpsRequest, security: operations.GetIpsSecurity) -> operations.GetIpsResponse:
        r"""List IPs
        List all Management and Additional IP Addresses.
         • Management IPs are IPs that are used for the management IP of a device.
           This is a public IP address that a device is born and dies with. It never changes during the lifecycle of the device.
         • Additional IPs are individual IPs that can be added to a device as an additional IP that can be used.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/ips'
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetIpsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.IPAddresses])
                res.ip_addresses = out
        elif http_res.status_code in [404, 422]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    