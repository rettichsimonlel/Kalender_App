from my_calender import Calender
from crud import CRUD

calender = Calender()

def main():
    """Run Main function."""
    crudid = CRUD()
    session_factory = crudid.create("sqlite:///Calender.db")

    calender.draw_week()
    while (True):
        print()
        m_input = input("(q)uit, (a)dd, (n)ext, (b)revios, (s)ave, (l)oad, (d)elete: ")
        if m_input == "q":
            break
        if m_input == "n":
            calender.next_week()
        if m_input == "b":
            calender.previos_week()
        if m_input == "a":
            calender.add()
        if m_input == "s":
            crudid.save(calender, session_factory)
        if m_input == "l":
            crudid.load(calender, session_factory)
        if m_input == "d":
            crudid.deletele(calender, session_factory)

if __name__ == "__main__":
    main()

