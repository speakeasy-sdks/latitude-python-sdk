import requests
from . import utils
from latitude.models import operations, shared
from typing import Optional

class Bandwidth:
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

    
    def get_traffic_consumption(self, request: operations.GetTrafficConsumptionRequest) -> operations.GetTrafficConsumptionResponse:
        r"""Retrieve Traffic consumption
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/traffic"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetTrafficConsumptionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Traffic])
                res.traffic = out

        return res

    
    def get_traffic_quota(self, request: operations.GetTrafficQuotaRequest) -> operations.GetTrafficQuotaResponse:
        r"""Retrieve Traffic Quota
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/traffic/quota"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetTrafficQuotaResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.TrafficQuota])
                res.traffic_quota = out
        elif r.status_code == 503:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    