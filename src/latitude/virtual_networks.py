import requests
from . import utils
from latitude.models import operations, shared
from typing import Optional

class VirtualNetworks:
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

    
    def create_virtual_network(self, request: operations.CreateVirtualNetworkRequest) -> operations.CreateVirtualNetworkResponse:
        r"""Create a Virtual Network
        Creates a new Virtual Network.
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/virtual_networks"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateVirtualNetworkResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.VirtualNetwork])
                res.virtual_network = out
        elif r.status_code == 422:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    
    def destroy_virtual_network(self, request: operations.DestroyVirtualNetworkRequest) -> operations.DestroyVirtualNetworkResponse:
        r"""Delete a Virtual Network
        Delete virtual network
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/virtual_networks/{id}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DestroyVirtualNetworkResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.VirtualNetwork])
                res.virtual_network = out
        elif r.status_code == 406:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ErrorObject])
                res.error_object = out

        return res

    
    def get_virtual_network(self, request: operations.GetVirtualNetworkRequest) -> operations.GetVirtualNetworkResponse:
        r"""Retrieve a Virtual Network
        Retrieve a Virtual Network.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/virtual_networks/{id}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.GetVirtualNetworkResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[operations.GetVirtualNetwork200ApplicationJSON])
                res.get_virtual_network_200_application_json_object = out

        return res

    
    def get_virtual_networks(self, request: operations.GetVirtualNetworksRequest) -> operations.GetVirtualNetworksResponse:
        r"""List all Virtual Networks
        Lists virtual networks assigned to a project
        
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/virtual_networks"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetVirtualNetworksResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.VirtualNetworks])
                res.virtual_networks = out

        return res

    
    def update_virtual_network(self, request: operations.UpdateVirtualNetworkRequest) -> operations.UpdateVirtualNetworkResponse:
        r"""Update a Virtual Network
        Update a Virtual Network.
        
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/virtual_networks/{id}", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("PATCH", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UpdateVirtualNetworkResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.VirtualNetwork])
                res.virtual_network = out
        elif r.status_code == 403:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.VirtualNetwork])
                res.virtual_network = out

        return res

    