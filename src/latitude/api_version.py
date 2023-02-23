import requests
from . import utils
from latitude.models import operations

class APIVersion:
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

    
    def get_current_version(self, request: operations.GetCurrentVersionRequest) -> operations.GetCurrentVersionResponse:
        r"""Get current API version
        Returns current Api Version
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/auth/current_version"
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetCurrentVersionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def update_current_version(self, request: operations.UpdateCurrentVersionRequest) -> operations.UpdateCurrentVersionResponse:
        r"""Update current API version
        Update current Api Version.
                Latest Version: 2022-07-18 Supported Versions: [2022-07-18]
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/auth/update_version"
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("PATCH", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateCurrentVersionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass
        elif r.status_code == 406:
            pass

        return res

    