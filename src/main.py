from getpass import getpass
from my_calender import Calender
from crud import CRUD
from model import User #, Kalender
import os

calender = Calender()

def main():
    """Run Main function."""
    crudid = CRUD()
    session_factory = crudid.create("sqlite:///Calender.db")
    current_kalender = None
    goto = False
    current_user = None

    while (True):
        if goto == False:
            user_name = input("Username (q)uit, (r)egister (s)how: ")
            if user_name == "q":
                break
            elif user_name == "r":
                i_user_name = input("Username: ")
                i_password = input("Password: ")
                with session_factory() as session:
                    new_user = User(user_name=i_user_name, password=i_password)
                    session.add(new_user)
                    session.commit()
            elif user_name == "s":
                with session_factory() as session:
                    all_users = session.query(User).all()
                for i in range(len(all_users)):
                    print(all_users[i].user_name)
            else:
                with session_factory() as session:
                    result = session.query(User).all()
                for i in range(len(result)):
                    if result[i].user_name == user_name:
                        password = getpass("Password: ")
                        if result[i].password == password:
                            current_user = result[i]
                if current_user == None:
                    print("No succies")

        if current_user != None:
            os.system("clear")
            while (True):
                kalender_result = crudid.load_kalender(session_factory, current_user)
                k_input = input("Kalender (q)uit (a)dd, (d)elete: ")
                if k_input == "a":
                    crudid.add_kalender(session_factory, current_user)
                elif k_input == "d":
                    crudid.delete_kalender(session_factory, current_user)
                elif k_input == "q":
                    os.system("clear")
                    current_kalender = None
                    current_user = None
                    goto = False
                    break
                else:
                    try:
                        current_kalender = kalender_result[int(k_input)]
                    except:
                        goto = True
                    break


        if current_kalender != None:
            os.system("clear")
            crudid.load_data(calender, session_factory, current_kalender)

        while (current_kalender != None):
            print()
            m_input = input("(q)uit, (a)dd, (n)ext, (b)revios, (s)ave, (l)oad, (d)elete (u)pdate: ")
            if m_input == "q":
                calender.data = []
                os.system("clear")
                current_kalender = None
                goto = True
                break
            elif m_input == "n":
                calender.next_week()
            elif m_input == "b":
                calender.previos_week()
            elif m_input == "a":
                calender.add()
            elif m_input == "s":
                crudid.save(calender, session_factory, current_kalender)
            elif m_input == "l":
                crudid.load_data(calender, session_factory, current_kalender)
            elif m_input == "d":
                crudid.deletele(calender, session_factory, current_kalender)
                crudid.load_data(calender, session_factory, current_kalender)
                calender.draw_week()
            elif m_input == "u":
                calender.update()
            else:
                os.system("clear")
                calender.draw_week()

if __name__ == "__main__":
    main()

