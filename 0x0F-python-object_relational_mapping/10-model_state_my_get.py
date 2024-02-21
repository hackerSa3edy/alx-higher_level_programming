#!/usr/bin/python3
"""Fetch state from the DBStorage
"""

def main():
    """Retrieve all states ordered by its id where the state name
    matches the specified keyword from the states table
    """
    data = session.query(State.id).\
        where(State.name == SEARCH_ITEM).\
        order_by(State.id).all()

    if data:
        for id in data:
            print(id.id)
    else:
        print('Not found')


if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

    MYSQL_USERNAME = sys.argv[1]
    MYSQL_PASSWD = sys.argv[2]
    DB_NAME = sys.argv[3]
    SEARCH_ITEM = sys.argv[4]

    engine = create_engine(
        f"mysql+mysqldb://{MYSQL_USERNAME}:{MYSQL_PASSWD}"
        f"@localhost:3306/{DB_NAME}",
        pool_pre_ping=True
        )
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    main()
