import requests as requests_http
from . import utils
from latitudeapi.models import operations, shared
from typing import Optional

class BandwidthPackages:
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
        
    def get_plans_bandwidth(self, security: operations.GetPlansBandwidthSecurity) -> operations.GetPlansBandwidthResponse:
        r"""List all bandwidth packages available
        Lists all bandwidth packages offered to your current team.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/plans/bandwidth'
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetPlansBandwidthResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PlansBandwidth])
                res.plans_bandwidth = out

        return res

    def update_plans_bandwidth(self, request: operations.UpdatePlansBandwidthRequest, security: operations.UpdatePlansBandwidthSecurity) -> operations.UpdatePlansBandwidthResponse:
        r"""Buy or remove bandwidth packages
        Allow to increase or decrease bandwidth packages. Only admins and owners can request.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/plans/bandwidth'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdatePlansBandwidthResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PlansBandwidth])
                res.plans_bandwidth = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    