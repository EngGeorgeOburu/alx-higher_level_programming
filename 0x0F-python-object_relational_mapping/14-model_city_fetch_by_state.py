#!/usr/bin/python3

from model_state importBase, State, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main(username, password, db_name):
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = (
            session.query(City)
            .join(State)
            .order_b(City.id)
            .all()
            )
    for city in cities:
        print(f"city.state.name): ({city.id}) {city.name}")
    session,close()

    if __name__ == "__main__":
        import sys
        if len(sys.argv) != 4:
            print("Usage: ./14-model_city_fetch_by_state.py <username> <password> <database_name>")
            sys.exit(1)

            username, password, db_name = sys.argv[1:]
            main(username, password, db_name)
