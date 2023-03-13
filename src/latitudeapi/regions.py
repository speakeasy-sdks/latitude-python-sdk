import requests as requests_http
from . import utils
from latitudeapi.models import operations, shared
from typing import Optional

class Regions:
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
        
    def get_region(self, request: operations.GetRegionRequest, security: operations.GetRegionSecurity) -> operations.GetRegionResponse:
        r"""Retrieve a Region
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/regions/{id}', request.path_params)
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetRegionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Region])
                res.region = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    def get_regions(self, security: operations.GetRegionsSecurity) -> operations.GetRegionsResponse:
        r"""List all Regions
        Lists all [available locations](https://latitude.sh/locations). For server availability by location, please see the [Plans API](/reference/get-plans).
        
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/regions'
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetRegionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Regions])
                res.regions = out

        return res

    