<!-- Start SDK Example Usage -->
```python
import latitude
from latitude.models import operations, shared

s = latitude.Latitude()
   
req = operations.GetRegionRequest(
    security=operations.GetRegionSecurity(
        bearer="YOUR_API_KEY_HERE",
    ),
    path_params=operations.GetRegionPathParams(
        id="unde",
    ),
)
    
res = s.regions.get_region(req)

if res.region is not None:
    # handle response
```
<!-- End SDK Example Usage -->