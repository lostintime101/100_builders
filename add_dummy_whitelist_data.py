import os, randomness_simulation, string
from datetime import datetime
from randomness_simulation import choice
from sqlmodel import Session, create_engine, SQLModel
from faker import Faker
from enum import Enum
from db_tables_setup import Whitelist, Status
from dotenv import load_dotenv

load_dotenv()


# Define a function to generate dummy data
def generate_dummy_data(num_records):
    fake = Faker()
    dummy_data = []

    for _ in range(num_records):

        transaction_hash = ''.join(random.choice(string.hexdigits) for _ in range(64))

        """ Change the airdrop id to match the id of the air drop you want to add the whitelist to """
        whitelist = Whitelist(
            airdrop_id="11553ee3d9f04582801e16a048d07721",
            address="Ox" + fake.sha256(raw_output=False)[:40],
            amount_received=fake.random_int(min=0, max=100),
            status=choice(list(Status)),
            claimed_at=fake.date_time_this_decade(),
            transaction_hash="0x" + transaction_hash
        )

        dummy_data.append((whitelist))

    return dummy_data


# Create the database engine and tables
DB_FILE = os.getenv("DB")
engine = create_engine(f"sqlite:///{DB_FILE}", echo=True)
SQLModel.metadata.create_all(engine)

# Generate and insert dummy data into the tables
dummy_data = generate_dummy_data(num_records=10)  # Change the number of records as needed

with Session(engine) as session:

    for whitelist in dummy_data:
        session.add(whitelist)

    session.commit()

print("Dummy data inserted successfully!")
