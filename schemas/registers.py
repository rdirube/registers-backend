from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Register(BaseModel):
    id: Optional[str]
    adress:str
    amount:str
    operation:str
    creation_time:str 