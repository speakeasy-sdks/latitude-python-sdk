import requests
from . import utils
from latitude.models import operations
from typing import Optional

class OperatingSystems:
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

    
    def get_plans_operating_system(self, request: operations.GetPlansOperatingSystemRequest) -> operations.GetPlansOperatingSystemResponse:
        r"""List all operating systems available
        Lists all operating systems available to deploy and reinstall.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/plans/operating_systems"
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetPlansOperatingSystemResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetPlansOperatingSystem200ApplicationJSON])
                res.get_plans_operating_system_200_application_json_object = out

        return res

    