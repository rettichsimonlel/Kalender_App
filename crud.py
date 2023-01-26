from my_calender import Calender
from model import Base, Data #, Kalender, User
import sqlalchemy
import sqlalchemy.orm

class CRUD():
    def save(self, calender, session_factory, m_user):
        with session_factory() as session:
            session.query(Data).filter(Data.user_id==m_user.user_id).delete()
            session.commit()
        for dat in calender.data:
            with session_factory() as session:
                new_data = Data(date=dat["date"], text=dat["data"], user_id=m_user.user_id)
                session.add(new_data)
                session.commit()
        calender.draw_week()

    def load(self, calender, session_factory, m_user):
        with session_factory() as session:
            result = session.query(Data).filter(Data.user_id==m_user.user_id).all()
        calender.data = []
        for i in range(len(result)):
            calender.data.append({"date": result[i].date, "data": result[i].text})
        calender.draw_week()


    def deletele(self, calender, session_factory, m_user):
        with session_factory() as session:
            session.query(Data).filter(Data.user_id==m_user.user_id).delete()
            session.commit()
        self.load(calender, session_factory, m_user)

    def create(self, database_url):
        db_connection = sqlalchemy.create_engine(database_url)
        Base.metadata.create_all(db_connection)
        session_factory = sqlalchemy.orm.sessionmaker()
        session_factory.configure(bind=db_connection)
        return session_factory

