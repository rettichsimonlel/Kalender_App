from my_calender import Calender
import sqlalchemy
from model import Base, User, Data

calender = Calender()
week = calender.make_week()
calender.draw_week(week)

def main():
    """Run Main function."""
    db_connection = database_connections("sqlite:///Calender.db")
    session_factory = session_creation(db_connection)


def database_connections(database_url):
    """Connect to database."""
    return sqlalchemy.create_engine(database_url)


def session_creation(db_connection):
    """Create session factory."""
    Base.metadata.create_all(db_connection)
    session_factory = sqlalchemy.orm.sessionmaker()
    session_factory.configure(bind=db_connection)
    return session_factory


if __name__ == "__main__":
    main()

