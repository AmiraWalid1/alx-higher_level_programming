#!/usr/bin/python3
"""
Module that contains the class definition of a City
and an instance Base = declarative_base().
"""
from sqlalchemy import Foreign_Key, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Represents a city in the states table.
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, Foreign_Key=True)
