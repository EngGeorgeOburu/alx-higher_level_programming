#!/usr/bin/python3
"""
This script printing city objects from db
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqla;chemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Accessing the db to get the cities
    """

    db_uri = 'mysql+mysqldb://{}:@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    cal_state = State(name='California')
    sfr_city = City(name='San Francisco')
    cla_state.cities.append(sfr_city)

    session.add(cal_state)
    session.commit()
    session.close()
