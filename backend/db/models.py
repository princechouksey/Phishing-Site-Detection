from pydantic import BaseModel
from typing import Any
from datetime import datetime

class URLRequest(BaseModel):
    url: str

class ResultModel(BaseModel):
    url: str
    result: Any  # Use Dict[str, Any] if you want to be more specific
    timestamp: datetime
