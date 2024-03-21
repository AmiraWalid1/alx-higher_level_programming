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


if __name__ == "__main__":
    engine = create_engine(
        f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}",
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")
