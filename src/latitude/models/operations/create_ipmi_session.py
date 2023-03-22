"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import error_object as shared_error_object
from ..shared import ipmi_session as shared_ipmi_session
from typing import Optional


@dataclasses.dataclass
class CreateIpmiSessionSecurity:
    
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header', 'field_name': 'Authorization' }})  
    

@dataclasses.dataclass
class CreateIpmiSessionRequest:
    
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})  
    

@dataclasses.dataclass
class CreateIpmiSessionResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    error_object: Optional[shared_error_object.ErrorObject] = dataclasses.field(default=None)
    r"""Forbidden"""  
    ipmi_session: Optional[shared_ipmi_session.IpmiSession] = dataclasses.field(default=None)
    r"""Created"""  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    