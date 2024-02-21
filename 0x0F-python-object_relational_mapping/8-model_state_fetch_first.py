#!/usr/bin/python3
"""Fetch state from the DBStorage
"""


def main():
    """Retrieve the first state from the states table
    """
    obj = session.query(State).order_by(State.id).first()

    if obj:
        print(f"{obj.id}: {obj.name}")
    else:
        print('Nothing')


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
