from model import Base, Data, Kalender #, User
import sqlalchemy
import sqlalchemy.orm

class CRUD():
    def save(self, calender, session_factory, current_kalender):
        with session_factory() as session:
            session.query(Data).filter(Data.kalender_id==current_kalender.kalender_id).delete()
            session.commit()
        for dat in calender.data:
            with session_factory() as session:
                new_data = Data(date=dat["date"], text=dat["data"], kalender_id=current_kalender.kalender_id)
                session.add(new_data)
                session.commit()
        calender.draw_week()

    def load_data(self, calender, session_factory, current_kalender):
        with session_factory() as session:
            result = session.query(Data).filter(Data.kalender_id==current_kalender.kalender_id).all()
        calender.data = []
        for i in range(len(result)):
            calender.data.append({"date": result[i].date, "data": result[i].text})
        calender.draw_week()

    def deletele(self, calender, session_factory, current_kalender):
        m_input = input("Delete (a)ll (d)ay: ")
        if m_input == "a":
            with session_factory() as session:
                session.query(Data).filter(Data.kalender_id==current_kalender.kalender_id).delete()
                session.commit()
            self.load_data(calender, session_factory, current_kalender)
        elif m_input == "d":
            d_input = int(input("Which day: "))
            week = calender.make_week()
            for i in range(len(week)):
                if week[i].day == d_input:
                    with session_factory() as session:
                        something = session.query(Data).filter(Data.kalender_id==current_kalender.kalender_id).all()
                        print(something[0].date)
                        for j in range(len(something)):
                            if something[j].date.day == week[i].day and something[j].date.month == week[i].month and something[j].date.year == week[i].year:
                                print(something[j].text)
                                session.delete(something[j])
                        session.commit()
                    pass

    def create(self, database_url):
        db_connection = sqlalchemy.create_engine(database_url)
        Base.metadata.create_all(db_connection)
        session_factory = sqlalchemy.orm.sessionmaker()
        session_factory.configure(bind=db_connection)
        return session_factory

    def add_kalender(self, session_factory, current_user):
        m_input = input("Title for the kalender: ")
        with session_factory() as session:
            new_kalender = Kalender(title=m_input, user_id=current_user.user_id)
            session.add(new_kalender)
            session.commit()

    def delete_kalender(self, session_factory, current_user):
        m_input = input("Name which kalender to destroy: ")
        with session_factory() as session:
            # something = session.query(Data).filter(Data.kalender_id==m_input).all()
            # for i in range(len(something)):
            #     session.delete(something[i])
            something = session.query(Kalender).filter(Kalender.user_id.like(current_user.user_id), Kalender.title.like(m_input)).all()
            result = session.query(Data).filter(Data.kalender_id==something[0].kalender_id).all()
            for i in range(len(result)):
                session.delete(result[i])
            for i in range(len(something)):
                session.delete(something[i])
            session.commit()

    def load_kalender(self, session_factory, current_user):
        with session_factory() as session:
            result = session.query(Kalender).filter(Kalender.user_id==current_user.user_id).all()
        for i in range(len(result)):
            print(f"{i}: {result[i].title}")
        if len(result) < 1:
            print("No kalenders currently available!")
        return result

