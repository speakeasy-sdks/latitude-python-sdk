<!-- Start SDK Example Usage -->
```python
import latitude
from latitude.models import operations, shared

s = latitude.Latitude()


req = operations.GetRegionRequest(
    id="89bd9d8d-69a6-474e-8f46-7cc8796ed151",
)
    
res = s.regions.get_region(req, operations.GetRegionSecurity(
    bearer="YOUR_API_KEY_HERE",
))

if res.region is not None:
    # handle response
```
<!-- End SDK Example Usage -->