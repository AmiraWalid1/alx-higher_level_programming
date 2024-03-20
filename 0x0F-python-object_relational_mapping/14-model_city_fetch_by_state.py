#!/usr/bin/python3
""" script that prints all City objects from the database hbtn_0e_14_usa """
from sys import argv
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        f"mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}",
        pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()
    for city in cities:
        print(f"{city.State.name}: ({city.City.id}) {city.City.name}")
