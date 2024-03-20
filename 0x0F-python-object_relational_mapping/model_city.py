#!/usr/bin/python3
"""
Module that contains the class definition of a City
and an instance Base = declarative_base().
"""
from model_state import Base
from sqlalchemy import ForeignKey, Column, String, Integer


class City(Base):
    """
    Represents a city in the states table.
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
