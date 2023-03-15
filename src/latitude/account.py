import requests as requests_http
from . import utils
from latitude.models import operations, shared
from typing import Optional

class Account:
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
        
    def get_user_profile(self, security: operations.GetUserProfileSecurity) -> operations.GetUserProfileResponse:
        r"""Retrieve the User Profile
        Retrieve the current user profile
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/user/profile'
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetUserProfileResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetUserProfile200ApplicationJSON])
                res.get_user_profile_200_application_json_object = out

        return res

    def get_user_teams(self, security: operations.GetUserTeamsSecurity) -> operations.GetUserTeamsResponse:
        r"""List all User Teams
        Returns a list of all teams the user belongs to
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/user/teams'
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetUserTeamsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Teams])
                res.teams = out

        return res

    def patch_user_profile(self, request: operations.PatchUserProfileRequest, security: operations.PatchUserProfileSecurity) -> operations.PatchUserProfileResponse:
        r"""Update the User Profile
        Update the current user profile
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(operations.PatchUserProfileRequest, base_url, '/user/profile/{id}', request)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('PATCH', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PatchUserProfileResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PatchUserProfile200ApplicationJSON])
                res.patch_user_profile_200_application_json_object = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    