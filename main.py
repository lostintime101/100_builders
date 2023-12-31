# 3rd party
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, create_engine, SQLModel, select

# built-in
from uuid import UUID
import os, sys, requests, re
from dotenv import load_dotenv
from typing import List

import utils
# local
from db_tables_setup import Airdrop, Activation, Whitelist, Status, AirdropUpdate, WhitelistUpdate
from onchain_logic import *
from utils import *


load_dotenv()
""" if app loads but can't view in browser, try turning off VPN """
app = FastAPI()

allowed_origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_FILE = os.getenv("DB")
# TODO: in production, remove echo=True
connect_args = {"check_same_thread": False}
engine = create_engine(f"sqlite:///{DB_FILE}", echo=True, connect_args=connect_args)


@app.on_event("startup")
def startup_event():
    SQLModel.metadata.create_all(engine)


# TEST
# airdrop_object = get_airdrop_info_by_whitelist_id("f4ffdcbe59974da187977512dc3d5de9", engine)
# print(generate_random_amount(airdrop_object))
# sys.exit()


# root, welcome message
@app.get("/")
async def root():
    return {"message": "Welcome to FrenDrops API"}


# fetch all airdrops
@app.get("/api/v1/drops")
async def fetch_airdrops():
    with Session(engine) as session:
        db_airdrops = session.exec(select(Airdrop)).all()
        return db_airdrops


# fetch airdrop by id
@app.get("/api/v1/drops/{airdrop_id}")
async def fetch_airdrops_by_creator(airdrop_id: UUID):
    with Session(engine) as session:
        db_airdrop = session.exec(select(Airdrop).where(Airdrop.id == airdrop_id)).first()
        return db_airdrop


# fetch airdrops by creator
@app.get("/api/v1/drops/{creator_address}")
async def fetch_airdrops_by_creator(creator_address: str):
    with Session(engine) as session:
        airdrops = session.exec(select(Airdrop).where(Airdrop.creator_address == creator_address)).all()
        return airdrops


# create new airdrop
@app.post("/api/v1/drops")
async def create_airdrop(airdrop: Airdrop):

    new_nonce = get_new_nonce()
    airdrop.dispatch_address = get_new_dispatcher_address(new_nonce)
    airdrop.nonce = new_nonce

    with Session(engine) as session:
        session.add(airdrop)
        session.commit()
        session.refresh(airdrop)
        return airdrop


# update airdrop
@app.patch("/api/v1/drops/update/{airdrop_id}")
async def update_airdrop(airdrop_id: UUID, airdrop: AirdropUpdate):
    with Session(engine) as session:
        db_airdrop = session.get(Airdrop, airdrop_id)
        if not db_airdrop:
            raise HTTPException(status_code=404, detail="Airdrop not found")
        db_data = airdrop.dict(exclude_unset=True)
        for key, value in db_data.items():
            setattr(db_airdrop, key, value)
        session.add(db_airdrop)
        session.commit()
        session.refresh(db_airdrop)
        return db_airdrop


# create whitelist for many addresses
@app.post("/api/v1/whitelists")
async def create_whitelists(whitelists: List[Whitelist]):
    with Session(engine) as session:
        for whitelist in whitelists:
            session.add(whitelist)
        session.commit()
        return whitelists


# fetch whitelist by airdrop id
@app.get("/api/v1/whitelists/{airdrop_id}")
async def fetch_whitelist_by_airdrop_id(airdrop_id: str):
    with Session(engine) as session:
        db_whitelist = session.exec(select(Whitelist).where(Whitelist.airdrop_id == airdrop_id)).all()
        return db_whitelist


# is address whitelisted?
@app.get("/api/v1/whitelists/{airdrop_id}/{address}")
async def is_address_whitelisted_for_this_airdrop(airdrop_id: str, address: str):
    with Session(engine) as session:
        db_whitelist = session.exec(select(Whitelist).where(Whitelist.address == address, Whitelist.airdrop_id == airdrop_id)).first()
        if not db_whitelist:
            raise HTTPException(status_code=404, detail="Address not whitelisted")
        return db_whitelist


# update whitelist
@app.patch("/api/v1/whitelists/{whitelist_id}")
async def update_whitelist(whitelist_id: UUID, whitelist: WhitelistUpdate):

    with Session(engine) as session:

        db_whitelist = session.get(Whitelist, whitelist_id)

        if not db_whitelist:
            raise HTTPException(status_code=404, detail="Whitelist UUID not found")

        db_data = whitelist.dict(exclude_unset=True)

        for key, value in db_data.items():
            setattr(db_whitelist, key, value)

        amount_received = generate_random_amount(whitelist_id)

        session.add(db_whitelist)
        session.commit()
        session.refresh(db_whitelist)

        return db_whitelist


# fetch group by twitter handle
@app.get("/api/v1/group/{twitter_handle}")
async def fetch_group_from_twitter_handle(twitter_handle: str):

    cleaned_username = twitter_handle.strip().lstrip("@")

    if not re.match("^[a-zA-Z0-9_]{1,15}$", cleaned_username):
        return HTTPException(status_code=400, detail="Invalid handle. Please provide a valid Twitter handle.")

    url = "https://prod-api.kosetto.com/search/users"

    headers = {
        "Authorization": os.getenv("JWT"),
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Referer": "https://www.friend.tech/"
    }
    params = {"username": cleaned_username}

    response = requests.get(url, headers=headers, params=params)
    address = None

    if response.status_code == 200:

        data = response.json()
        users = data.get("users", [])

        for user in users:
            if user.get("twitterUsername") == params["username"]:
                address = user.get("address")
                break

        if not address: return HTTPException(status_code=400, detail="No exact matching Twitter handle on Friends.Tech")

    else: return HTTPException(status_code=400, detail="Friends.Tech API not responding correctly")

    # get holder count
    url = f"https://prod-api.kosetto.com/users/{address}/"
    response = requests.get(url, headers=None)
    group_info = response.json()

    user["holderCount"] = group_info["holderCount"]
    print(user)
    if user: return user
    else: return HTTPException(status_code=400, detail="No matching Twitter handle on Friends.Tech")
