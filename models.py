from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum
from datetime import datetime


class Airdrop(BaseModel):
    id: Optional[UUID] = uuid4()
    address: str
    created_at: datetime = datetime.now()
    gas_token_amount: int = 0
    airdrop_token_amount: int = 0
    airdrop_token_address: Optional[str] = None
    current_token_balance: int = 0
    creator: str
    message: Optional[str]
    whitelist: dict
    recipients: int
    total_addresses_claimed: int
    activated: bool = False
    activated_at: datetime = None
