import requests
from . import utils
from latitude.models import operations, shared
from typing import Optional

class Account:
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

    
    def get_user_profile(self, request: operations.GetUserProfileRequest) -> operations.GetUserProfileResponse:
        r"""Retrieve the User Profile
        Retrieve the current user profile
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/user/profile"
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetUserProfileResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetUserProfile200ApplicationJSON])
                res.get_user_profile_200_application_json_object = out

        return res

    
    def get_user_teams(self, request: operations.GetUserTeamsRequest) -> operations.GetUserTeamsResponse:
        r"""List all User Teams
        Returns a list of all teams the user belongs to
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/user/teams"
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetUserTeamsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Teams])
                res.teams = out

        return res

    
    def patch_user_profile(self, request: operations.PatchUserProfileRequest) -> operations.PatchUserProfileResponse:
        r"""Update the User Profile
        Update the current user profile
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/user/profile/{id}", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("PATCH", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PatchUserProfileResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.PatchUserProfile200ApplicationJSON])
                res.patch_user_profile_200_application_json_object = out
        elif r.status_code == 403:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    