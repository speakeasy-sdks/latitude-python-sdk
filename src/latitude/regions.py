import requests
from . import utils
from latitude.models import operations, shared
from typing import Optional

class Regions:
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

    
    def get_region(self, request: operations.GetRegionRequest) -> operations.GetRegionResponse:
        r"""Retrieve a Region
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/regions/{id}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetRegionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Region])
                res.region = out
        elif r.status_code == 404:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    
    def get_regions(self, request: operations.GetRegionsRequest) -> operations.GetRegionsResponse:
        r"""List all Regions
        Lists all [available locations](https://latitude.sh/locations). For server availability by location, please see the [Plans API](/reference/get-plans).
        
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/regions"
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetRegionsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Regions])
                res.regions = out

        return res

    