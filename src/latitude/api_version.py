import requests as requests_http
from . import utils
from latitude.models import operations

class APIVersion:
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
        
    def get_current_version(self, security: operations.GetCurrentVersionSecurity) -> operations.GetCurrentVersionResponse:
        r"""Get current API version
        Returns current Api Version
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/auth/current_version'
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetCurrentVersionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass

        return res

    def update_current_version(self, request: operations.UpdateCurrentVersionRequest, security: operations.UpdateCurrentVersionSecurity) -> operations.UpdateCurrentVersionResponse:
        r"""Update current API version
        Update current Api Version.
                Latest Version: 2022-07-18 Supported Versions: [2022-07-18]
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/auth/update_version'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateCurrentVersionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code in [200, 406]:
            pass

        return res

    