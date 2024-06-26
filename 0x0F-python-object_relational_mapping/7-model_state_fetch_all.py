#!/usr/bin/python3
"""
List all state objects from the database
"""
import sys
from sqlalchemy import create_engine
from sqlachemy.rom import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Accessing db toget states
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = creatw_engine('mysql+mysqldb://{}:{}@localhost: 3306/{}'.format(
        username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(state.name)
