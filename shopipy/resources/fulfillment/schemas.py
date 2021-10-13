from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class Fulfillments(BaseModel):

    created_at: Optional[str]
    id: Optional[str]
    order_id: Optional[str]
    status: Optional[str]
    tracking_company: Optional[str]
    tracking_number: Optional[str]
    updated_at: Optional[str]
