import requests
from . import utils
from latitude.models import operations, shared
from typing import Optional

class VPNSessions:
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

    
    def delete_vpn_session(self, request: operations.DeleteVpnSessionRequest) -> operations.DeleteVpnSessionResponse:
        r"""Delete a VPN Session
        Deletes an existing VPN Session.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/vpn_sessions/{vpn_session_id}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DeleteVpnSessionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass
        elif r.status_code == 404:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    
    def get_vpn_sessions(self, request: operations.GetVpnSessionsRequest) -> operations.GetVpnSessionsResponse:
        r"""List all Active VPN Sessions
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/vpn_sessions"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetVpnSessionsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetVpnSessions200ApplicationJSON])
                res.get_vpn_sessions_200_application_json_object = out
        elif r.status_code == 422:
            pass

        return res

    
    def post_vpn_session(self, request: operations.PostVpnSessionRequest) -> operations.PostVpnSessionResponse:
        r"""Create a VPN Session
        Creates a new VPN Session.
        `NOTE:` The VPN credentials are only listed ONCE upon creation. They can however be refreshed or deleted.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/vpn_sessions"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PostVpnSessionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.VpnSessionWithPassword])
                res.vpn_session_with_password = out
        elif r.status_code == 422:
            pass

        return res

    
    def put_vpn_session(self, request: operations.PutVpnSessionRequest) -> operations.PutVpnSessionResponse:
        r"""Refresh a VPN Session
        Refreshing an existing VPN Session will create new credentials for that session
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/vpn_sessions/{vpn_session_id}/refresh_password", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("PUT", url)
        content_type = r.headers.get("Content-Type")

        res = operations.PutVpnSessionResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.VpnSessionWithPassword])
                res.vpn_session_with_password = out
        elif r.status_code == 404:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    