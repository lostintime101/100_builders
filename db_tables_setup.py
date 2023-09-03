from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional
from enum import Enum
from datetime import datetime
from sqlmodel import Field, SQLModel, create_engine
from dotenv import load_dotenv
import os

load_dotenv()

# There should be one engine for the entire application
DB_FILE = os.getenv("DB")
engine = create_engine(f"sqlite:///{DB_FILE}", echo=True)


class Status(str, Enum):
    claimed = "claimed"
    unclaimed = "unclaimed"
    late_claim = "late claim"
    error_claiming = "error_claiming"


class Activation(str, Enum):
    unactivated = "unactivated"
    activated = "activated"
    deactivated = "deactivated"


class Airdrop(SQLModel, table=True):

    __tablename__ = 'airdrops'
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True, nullable=False)
    dispatch_address: str = Field(index=True, nullable=False, max_length=42, min_length=42)
    created_at: datetime = Field(nullable=False)
    gas_token_amount: int = Field(default=0, nullable=False)
    airdrop_token_amount: int = Field(default=0, nullable=False)
    airdrop_token_address: Optional[str] = None
    current_token_balance: int = Field(default=0, nullable=False)
    creator_address: str = Field(nullable=False, max_length=42, min_length=42)
    message: Optional[str]
    whitelist_created: bool = Field(default=False, nullable=False)
    recipients: int = Field(gt=0, nullable=False)
    total_addresses_claimed: int = Field(default=0, nullable=False, le=recipients)
    activated: Activation = Activation.unactivated
    activated_at: datetime = Field(default=None)
    deactivated_at: datetime = Field(default=None)


class Whitelist(SQLModel, table=True):

    __tablename__ = 'whitelists'

    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True, nullable=False)
    airdrop_id: UUID = Field(nullable=False, index=True, foreign_key='airdrops.id')
    address: str = Field(nullable=False)
    amount_received: int = Field(default=0, nullable=False)
    status: Status = Status.unclaimed
    claimed_at: datetime = Field(default=None, nullable=True)


def create_tables():
    SQLModel.metadata.create_all(engine)


# create tables in the database
if __name__ == '__main__':
    create_tables()


# class Airdrop(BaseModel):
#     id: Optional[UUID] = uuid4()
#     address: str
#     created_at: datetime = datetime.now()
#     gas_token_amount: int = 0
#     airdrop_token_amount: int = 0
#     airdrop_token_address: Optional[str] = None
#     current_token_balance: int = 0
#     creator: str
#     message: Optional[str]
#     whitelist: dict
#     recipients: int
#     total_addresses_claimed: int
#     activated: Activation = Activation.unactivated
#     activated_at: datetime = None


# OLD
# class Whitelist(BaseModel):
#     id: Optional[UUID] = uuid4()
#     airdrop_id: UUID
#     address: str
#     amount: int = 0
#     status: Status = Status.unclaimed
#     claimed_at: datetime = None
