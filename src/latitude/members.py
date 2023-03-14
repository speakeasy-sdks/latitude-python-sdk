import requests as requests_http
from . import utils
from latitude.models import operations, shared
from typing import Optional

class Members:
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
        
    def destroy_team_member(self, request: operations.DestroyTeamMemberRequest, security: operations.DestroyTeamMemberSecurity) -> operations.DestroyTeamMemberResponse:
        r"""Remove a Team Member
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/team/members/{user_id}', request.path_params)
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DestroyTeamMemberResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code in [200, 403]:
            pass
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    def get_team_members(self, security: operations.GetTeamMembersSecurity) -> operations.GetTeamMembersResponse:
        r"""List all Team Members
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/team/members'
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetTeamMembersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TeamMembers])
                res.team_members = out

        return res

    def post_team_members(self, request: operations.PostTeamMembersRequest, security: operations.PostTeamMembersSecurity) -> operations.PostTeamMembersResponse:
        r"""Add a Team Member
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/team/members'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostTeamMembersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.Membership])
                res.membership = out
        elif http_res.status_code in [403, 422]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    