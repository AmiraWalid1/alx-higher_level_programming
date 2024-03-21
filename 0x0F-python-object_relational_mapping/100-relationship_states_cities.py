#!/usr/bin/python3
"""class definition of a State"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}",
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    session.add(new_state)
    session.commit()
    new_city = City(name="San Francisco", state_id=new_state.id)
    session.add(new_city)
    session.commit()
