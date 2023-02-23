from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class SchemeBearer:
    api_key: str = dataclasses.field(metadata={'security': { 'field_name': 'Authorization' }})
    