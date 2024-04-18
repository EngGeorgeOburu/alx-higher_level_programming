#!/usr/bin/python3
"""
Lists all state obj and corresponding City
objects from the db
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    """
    Accessing the db to get states and cities
    """

    username, password, database = sys.argv[1:4]
    db_uri = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"

    engine = create_engine(db_uri)
    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    session.close()
