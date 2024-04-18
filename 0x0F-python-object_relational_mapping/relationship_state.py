#!/usr/bin/python3
"""
Script defining a State class and base class
to work with MySQLAlchemy ORM
"""

from sqlachemy import Column, Integer, String
from sqlachemy.orm import relationship
from sqlachemy.exit.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class
    Attributes:
        __tablename__(str): Name of the class
        id (int): State id
        name (str): State name
        cities (:ob:'City'): Cities belonging to state
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(string(128), nullable=False)
    cities = relationship("city", backref="state", cascade="all, delete")
