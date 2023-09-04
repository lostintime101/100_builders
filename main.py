# 3rd party
from fastapi import FastAPI, HTTPException
from sqlmodel import Session, create_engine, SQLModel, select

# built-in
from uuid import UUID
import os
from dotenv import load_dotenv

# local
from db_tables_setup import Airdrop, Activation, Whitelist, Status, AirdropUpdate


load_dotenv()
""" if app loads but can't view in browser, try turning off VPN """
app = FastAPI()

DB_FILE = os.getenv("DB")
# TODO: in production, remove echo=True
connect_args = {"check_same_thread": False}
engine = create_engine(f"sqlite:///{DB_FILE}", echo=True, connect_args=connect_args)


@app.on_event("startup")
def startup_event():
    SQLModel.metadata.create_all(engine)


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
@app.get("/api/v1/drops/{id}")
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
    # db.append(airdrop)
    # return {"id": airdrop.id}
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
