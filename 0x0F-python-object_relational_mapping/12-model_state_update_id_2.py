#!/usr/bin/python3
"""Update a row name column
"""


def main():
    """Update the value of the name column in the state table
    """
    session.query(State).filter_by(id=2).update({State.name: 'New Mexico'})
    session.commit()


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
