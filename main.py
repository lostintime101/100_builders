from fastapi import FastAPI, HTTPException
from typing import List
from uuid import UUID
from models import Airdrop


app = FastAPI()

db: List[Airdrop] = [
    Airdrop(
        id=UUID("f4e63a55-22e8-4aa1-b3d6-bcb6b4a8dc1c", version=4),
        address="0x123",
        created_at="2023-09-02 13:58:47.064663",
        gas_token_amount=0,
        airdrop_token_amount=0,
        airdrop_token_address=None,
        current_token_balance=0,
        creator="0x134",
        message="",
        whitelist={},
        recipients=0,
        total_addresses_claimed=0,
        activated=False,
        activated_at=None
    ),
    Airdrop(
        id=UUID("675b7979-32df-47a6-beaf-19641eee0728", version=4),
        address="Ox124",
        created_at="2023-09-02 13:59:47.064663",
        gas_token_amount=1,
        airdrop_token_amount=3,
        airdrop_token_address=None,
        current_token_balance=1,
        creator="Ox125",
        message="Happy Birthday!",
        whitelist={"0x127": False, "0x128": 1, "0x129": 1},
        recipients=3,
        total_addresses_claimed=2,
        activated=True,
        activated_at="2023-09-02 14:00:47.064665"
    ),
]


# root, welcome message
@app.get("/")
async def root():
    return {"message": "Welcome to FrenDrops API"}


# fetch all airdrops
@app.get("/api/v1/drops")
async def fetch_airdrops():
    return db


# fetch airdrop by address
@app.get("/api/drops/{creator}")
async def fetch_airdrops_by_creator(creator: str):
    for airdrop in db:
        if airdrop.creator == creator:
            return airdrop
    raise HTTPException(
        status_code=404,
        detail=f"Airdrop with creator {creator} not found"
    )


# deactivate airdrop
@app.put("/api/drops/{address}")
async def deactivate_airdrop(address: str):
    for airdrop in db:
        if airdrop.address == address:
            airdrop.activated = False
            return {"message": "airdrop deactivated"}
    raise HTTPException(
        status_code=404,
        detail=f"Airdrop under {address} not found"
    )


# create new airdrop
@app.post("/api/v1/users")
async def create_airdrop(airdrop: Airdrop):
    db.append(airdrop)
    return {"id": airdrop.id}
