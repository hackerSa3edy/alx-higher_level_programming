#!/usr/bin/python3
"""Fetch state from the DBStorage
"""


def main():
    """Retrieve all states ordered by its id where the state name
    contains 'a' from the states table
    """
    data = session.query(State).where(State.name.contains('a'))\
        .order_by(State.id).all()

    for obj in data:
        print(f"{obj.id}: {obj.name}")


if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

    MYSQL_USERNAME = sys.argv[1]
    MYSQL_PASSWD = sys.argv[2]
    DB_NAME = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{MYSQL_USERNAME}:{MYSQL_PASSWD}"
        f"@localhost:3306/{DB_NAME}",
        pool_pre_ping=True
        )
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    main()
