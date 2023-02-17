import requests
from . import utils
from latitude.models import operations, shared
from typing import Optional

class Members:
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

    
    def destroy_team_member(self, request: operations.DestroyTeamMemberRequest) -> operations.DestroyTeamMemberResponse:
        r"""Remove a Team Member
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/team/members/{user_id}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DestroyTeamMemberResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass
        elif r.status_code == 403:
            pass
        elif r.status_code == 404:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    
    def get_team_members(self, request: operations.GetTeamMembersRequest) -> operations.GetTeamMembersResponse:
        r"""List all Team Members
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/team/members"
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetTeamMembersResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.TeamMembers])
                res.team_members = out

        return res

    
    def post_team_members(self, request: operations.PostTeamMembersRequest) -> operations.PostTeamMembersResponse:
        r"""Add a Team Member
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/team/members"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PostTeamMembersResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Membership])
                res.membership = out
        elif r.status_code == 403:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ErrorObject])
                res.error_object = out
        elif r.status_code == 422:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    