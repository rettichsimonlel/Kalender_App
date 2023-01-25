from my_calender import Calender
import sqlalchemy
import sqlalchemy.orm
from model import Base, User, Data, Kalender

calender = Calender()

def main():
    """Run Main function."""
    db_connection = database_connections("sqlite:///Calender.db")
    session_factory = session_creation(db_connection)

    calender.draw_week()
    while (True):
        print()
        m_input = input("(q)uit, (a)dd, (n)ext, (b)revios, (s)ave, (l)oad: ")
        if m_input == "q":
            break
        if m_input == "n":
            calender.next_week()
        if m_input == "b":
            calender.previos_week()
        if m_input == "a":
            calender.add()
        

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

