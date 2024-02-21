#!/usr/bin/python3
"""Fetch connected city and states
"""


def main():
    """Retrieve the connected cities and states
    """
    data = session.query(
        State.name.label('state_name'),
        City.id.label('city_id'),
        City.name.label('city_name')).join(
            City,
            State.id == City.state_id
            ).order_by('city_id').all()

    for row in data:
        print(f"{row.state_name}: ({row.city_id}) {row.city_name}")


if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base
    from model_city import City

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
