#!/usr/bin/python3
"""
script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
Results must be displayed as:
    <state id>: <state name>
    <tabulation><city id>: <city name>
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State


if __name__ == "__main__":
    engine = create_engine(
        f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}",
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in sorted(state.cities, key=lambda city: city.id):
            print(f"\t{city.id}: {city.name}")
