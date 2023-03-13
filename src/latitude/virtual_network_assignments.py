import requests as requests_http
from . import utils
from latitude.models import operations, shared
from typing import Optional

class VirtualNetworkAssignments:
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
        
    def assign_server_virtual_network(self, request: operations.AssignServerVirtualNetworkRequest, security: operations.AssignServerVirtualNetworkSecurity) -> operations.AssignServerVirtualNetworkResponse:
        r"""Assign a server to a virtual network
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/virtual_networks/assignments'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.AssignServerVirtualNetworkResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.VirtualNetworkAssignment])
                res.virtual_network_assignment = out
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    def delete_virtual_networks_assignments(self, request: operations.DeleteVirtualNetworksAssignmentsRequest, security: operations.DeleteVirtualNetworksAssignmentsSecurity) -> operations.DeleteVirtualNetworksAssignmentsResponse:
        r"""Delete a Virtual Network Assignment
        Allow you to remove a Virtual Network assignment.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, '/virtual_networks/assignments/{assignment_id}', request.path_params)
        
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('DELETE', url)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteVirtualNetworksAssignmentsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            pass
        elif http_res.status_code == 403:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    def get_virtual_networks_assignments(self, request: operations.GetVirtualNetworksAssignmentsRequest, security: operations.GetVirtualNetworksAssignmentsSecurity) -> operations.GetVirtualNetworksAssignmentsResponse:
        r"""List all servers assigned to virtual networks
        Returns a list of all servers assigned to virtual networks.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/virtual_networks/assignments'
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetVirtualNetworksAssignmentsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.VirtualNetworkAssignments])
                res.virtual_network_assignments = out

        return res

    