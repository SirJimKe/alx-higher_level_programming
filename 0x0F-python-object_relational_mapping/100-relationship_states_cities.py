#!/usr/bin/python3
"""Creates a State "California" with the City "San Francisco"
   in the database hbtn_0e_100_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    session.add(california)
    session.commit()
    session.add(san_francisco)
    session.commit()
    session.close()
