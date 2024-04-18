#!/usr/bin/python3
"""
Deletes all state objects
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main(username, password, db_name):
    """
    Deletes states
    Args:
        username(str): username to connect to my MYSQdb
        password(str): password to connect to the MySQL db
        db_name(str): Name of the db to connect to
    """
    engine = create_engine(
            f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}")
    Base.metadata.create_oil(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(
            State.name.like("%a%")).all()
    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()

    if __name__ == "__main__":
        import sys
        if len(sys.argv) != 4:
            print(
                    "Usage:./13-model_state_delete_a.py"
                    "<username> <password> <database_name>"
                    )
            sys.exit(1)
