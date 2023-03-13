<!-- Start SDK Example Usage -->
```python
import latitudeapi
from latitudeapi.models import operations, shared

s = latitudeapi.Latitudeapi()
   
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