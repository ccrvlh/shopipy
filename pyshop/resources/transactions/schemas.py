from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel

class Transactions(BaseModel):

    id: Optional[int]
    order_id: Optional[int]
    kind: Optional[str]
    gateway: Optional[str]
    status: Optional[str]
    message: Optional[str]
    created_at: Optional[datetime]
    test: bool
    authorization: Optional[str]
    location_id: Optional[int]
    user_id: Optional[int]
    parent_id: Optional[int]
    processed_at: Optional[datetime]
    device_id: Optional[int]
    receipt: Optional[Dict[Any, Any]]
    error_code: Optional[str]
    source_name: Optional[str]
    forex_adjustment: Optional[str]
    amount: Optional[str]
    currency: Optional[str]
    admin_graphql_api_id: Optional[str]
