# 3rd party
from sqlmodel import Field, SQLModel, create_engine

# built-in
from uuid import UUID, uuid4
from typing import Optional
from enum import Enum
from datetime import datetime
from dotenv import load_dotenv
import os


load_dotenv()

# There should be one engine for the entire application
DB_FILE = os.getenv("DB")
# TODO: in production, remove echo=True
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
    total_addresses_claimed: int = Field(default=0, nullable=False)  # le=recipients, error message, not sure why
    activated: Activation = Activation.unactivated
    activated_at: datetime = Field(default=None)
    deactivated_at: datetime = Field(default=None)


class AirdropUpdate(SQLModel):

    gas_token_amount: Optional[int] = None
    airdrop_token_amount: Optional[int] = None
    current_token_balance: Optional[int] = None
    whitelist_created: Optional[bool] = None
    total_addresses_claimed: Optional[int] = None
    activated: Optional[Activation] = None
    activated_at: Optional[datetime] = None
    deactivated_at: Optional[datetime] = None


class Whitelist(SQLModel, table=True):

    __tablename__ = 'whitelists'

    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True, nullable=False)
    airdrop_id: UUID = Field(nullable=False, index=True, foreign_key='airdrops.id')
    address: str = Field(nullable=False)
    amount_received: Optional[int] = Field(default=0, nullable=False)
    status: Optional[Status] = Field(default=Status.unclaimed, nullable=False)
    claimed_at: Optional[datetime] = Field(default=None, nullable=True)


class WhitelistUpdate(SQLModel):

    amount_received: Optional[int] = None
    status: Optional[Status] = None
    claimed_at: Optional[datetime] = None


def create_tables():
    SQLModel.metadata.create_all(engine)


# create tables in the database
if __name__ == '__main__':
    create_tables()
