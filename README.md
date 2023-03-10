<div align="center">
        <img src="https://user-images.githubusercontent.com/68016351/223031191-fff87dd7-a3bd-4974-acc2-304b2ee5128e.png" width="500">
   <p>Everything you need to deploy and manage single-tenant, high-performance bare metal servers.</p>
   <a href="https://github.com/speakeasy-sdks/latitude-python-sdk/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/latitude-python-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
   <a href="https://docs.latitude.sh/reference/summary"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000&style=for-the-badge" /></a>
</div>

The Latitude.sh API gives you programmatic access to all resources available on the platform. With full control over the entire Latitude.sh platform, you can build integrations, custom dashboards, and manage your servers from your own clients.

***Please note that the following installation example with pip is illustrative and will not download a package until a publishing token is provided as a github secret. To test out the repo you may clone it locally and run `pip install -e ../path/to/local/clone/` .***

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install openapi
```
<!-- End SDK Installation -->
## Authentication

To create an API token, go to the Settings & Billing → API Keys page on the dashboard.

The key is shown to your only when it's created. If you lose it, you'll have to roll the key or create a new one.

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import latitude
from latitude.models import operations, shared

s = latitude.Latitude()
   
req = operations.DeleteAPIKeyRequest(
    security=operations.DeleteAPIKeySecurity(
        bearer="YOUR_API_KEY_HERE",
    ),
    path_params=operations.DeleteAPIKeyPathParams(
        id="unde",
    ),
)
    
res = s.api_keys.delete_api_key(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## SDK Available Operations


### api_keys

* `delete_api_key` - Delete an API Key
* `get_api_keys` - List all API Keys
* `post_api_key` - Create an API Key
* `update_api_key` - Regenerate an API Key

### api_version

* `get_current_version` - Get current API version
* `update_current_version` - Update current API version

### account

* `get_user_profile` - Retrieve the User Profile
* `get_user_teams` - List all User Teams
* `patch_user_profile` - Update the User Profile

### bandwidth

* `get_traffic_consumption` - Retrieve Traffic consumption
* `get_traffic_quota` - Retrieve Traffic Quota

### bandwidth_packages

* `get_plans_bandwidth` - List all bandwidth packages available
* `update_plans_bandwidth` - Buy or remove bandwidth packages

### deploy_config

* `get_server_deploy_config` - Retrieve the Server Deploy Config
* `update_server_deploy_config` - Update the Server Deploy Config

### ip_addresses

* `get_ip` - Retrieve an IP
* `get_ips` - List IPs

### ipmi_credentials

* `create_ipmi_session` - Generate IPMI credentials

### members

* `destroy_team_member` - Remove a Team Member
* `get_team_members` - List all Team Members
* `post_team_members` - Add a Team Member

### operating_systems

* `get_plans_operating_system` - List all operating systems available

### plans

* `get_plan` - Retrieve a Plan
* `get_plans` - List all Plans

### power_actions

* `create_server_action` - Run Server Action

### projects

* `create_project` - Create a Project
* `delete_project` - Delete a Project
* `get_project` - Retrieve a Project
* `get_projects` - List all Projects
* `update_project` - Update a Project

### regions

* `get_region` - Retrieve a Region
* `get_regions` - List all Regions

### rescue_mode

* `server_exit_rescue_mode` - Exits rescue mode for a Server
* `server_start_rescue_mode` - Puts a Server in rescue mode

### roles

* `get_role_id` - Retrieve a Role
* `get_roles` - List all Roles

### ssh_keys

* `delete_project_ssh_key` - Delete a Project SSH Key
* `get_project_ssh_key` - Retrieve a Project SSH Key
* `get_project_ssh_keys` - List all Project SSH Keys
* `post_project_ssh_key` - Create a Project SSH Key
* `put_project_ssh_key` - Update a Project SSH Key

### server_reinstall

* `create_server_reinstall` - Run Server Reinstall

### servers

* `create_server` - Deploy a new server
* `destroy_server` - Remove a Server
* `get_server` - Retrieve a Server
* `get_servers` - List all Servers
* `update_server` - Update a Server

### teams

* `get_team` - Retrieve the Current Team
* `patch_current_team` - Update a Team
* `post_team` - Create a Team

### user_data

* `delete_project_user_data` - Delete a Project User Data
* `get_project_user_data` - Retrieve a Project User Data
* `get_project_users_data` - List all Project User Data
* `post_project_user_data` - Create a Project User Data
* `put_project_user_data` - Update a Project User Data

### vpn_sessions

* `delete_vpn_session` - Delete a VPN Session
* `get_vpn_sessions` - List all Active VPN Sessions
* `post_vpn_session` - Create a VPN Session
* `put_vpn_session` - Refresh a VPN Session

### virtual_network_assignments

* `assign_server_virtual_network` - Assign a server to a virtual network
* `delete_virtual_networks_assignments` - Delete a Virtual Network Assignment
* `get_virtual_networks_assignments` - List all servers assigned to virtual networks

### virtual_networks

* `create_virtual_network` - Create a Virtual Network
* `destroy_virtual_network` - Delete a Virtual Network
* `get_virtual_network` - Retrieve a Virtual Network
* `get_virtual_networks` - List all Virtual Networks
* `update_virtual_network` - Update a Virtual Network
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
