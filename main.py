from my_calender import Calender
from crud import CRUD
from model import User
import os

calender = Calender()

def main():
    """Run Main function."""
    crudid = CRUD()
    session_factory = crudid.create("sqlite:///Calender.db")

    while (True):
        current_user = None
        user_name = input("Username (q)uit, (r)egister: ")
        if user_name == "q":
            break
        elif user_name == "r":
            i_user_name = input("Username: ")
            i_password = input("Password: ")
            with session_factory() as session:
                new_user = User(user_name=i_user_name, password=i_password)
                session.add(new_user)
                session.commit()
        else:
            with session_factory() as session:
                result = session.query(User).all()
            for i in range(len(result)):
                if result[i].user_name == user_name:
                    password = input("Password: ")
                    if result[i].password == password:
                        current_user = result[i]
            if current_user == None:
                print("No succies")

        if current_user != None:
            os.system("clear")
            calender.draw_week()
            crudid.load(calender, session_factory, current_user)
        while (current_user != None):
            print()
            m_input = input("(q)uit, (a)dd, (n)ext, (b)revios, (s)ave, (l)oad, (d)elete: ")
            if m_input == "q":
                current_user = None
                calender.data = []
                os.system("clear")
                break
            if m_input == "n":
                calender.next_week()
            if m_input == "b":
                calender.previos_week()
            if m_input == "a":
                calender.add()
            if m_input == "s":
                crudid.save(calender, session_factory, current_user)
            if m_input == "l":
                crudid.load(calender, session_factory, current_user)
            if m_input == "d":
                crudid.deletele(calender, session_factory, current_user)

if __name__ == "__main__":
    main()

