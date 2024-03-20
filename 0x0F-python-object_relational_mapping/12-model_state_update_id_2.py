#!/usr/bin/python3
""" script that changes the name of a State object from
the database hbtn_0e_6_usa """
from sys import argv
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

    record = session.query(State).filter(State.id == 2).first()
    record.name = "New Mexico"
    session.commit()
