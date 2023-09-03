import os, random
from datetime import datetime
from random import choice
from sqlmodel import Session, create_engine, SQLModel
from faker import Faker
from enum import Enum
from db_tables_setup import Airdrop, Activation
from dotenv import load_dotenv

load_dotenv()


# Define a function to generate dummy data
def generate_dummy_data(num_records):
    fake = Faker()
    dummy_data = []

    for _ in range(num_records):
        airdrop = Airdrop(
            dispatch_address="Ox" + fake.sha256(raw_output=False)[:40],
            created_at=datetime.now(),
            gas_token_amount=fake.random_int(min=0, max=1000),
            airdrop_token_amount=fake.random_int(min=0, max=10000),
            airdrop_token_address="Ox" + fake.sha256(raw_output=False)[:40],
            current_token_balance=fake.random_int(min=0, max=100000),
            creator_address="Ox" + fake.sha256(raw_output=False)[:40],
            message=fake.text(),
            whitelist_created=choice([True, False]),
            recipients=fake.random_int(min=1, max=100),
            total_addresses_claimed=fake.random_int(min=0, max=100),
            activated=choice(list(Activation)),
            activated_at=fake.date_time_this_decade(),
            deactivated_at=fake.date_time_this_decade()
        )

        dummy_data.append((airdrop))

    return dummy_data


# Create the database engine and tables
DB_FILE = os.getenv("DB")
engine = create_engine(f"sqlite:///{DB_FILE}", echo=True)
SQLModel.metadata.create_all(engine)

# Generate and insert dummy data into the tables
dummy_data = generate_dummy_data(num_records=10)  # Change the number of records as needed

with Session(engine) as session:

    for airdrop in dummy_data:
        session.add(airdrop)

    session.commit()

print("Dummy data inserted successfully!")
