#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ = "__main--":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database))

    Session = sessionmaker(bind=engine)
    session =Session

    state_to_produce = session_query(State).filter_by(id=2),filter()
    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()

    session.close()
