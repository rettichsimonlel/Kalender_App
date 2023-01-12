import datetime
from bcolors import bcolors

class Calender():
    def __init__(self):
        self.current_week = datetime.datetime.now().isocalendar().week
        self.current_date = datetime.datetime.now()

    def make_week(self):
        week = []
        monday = self.current_date + datetime.timedelta(days = -self.current_date.weekday())
        week.append(monday)
        for i in range(1, 7):
            next_day = monday + datetime.timedelta(days=i)
            week.append(next_day)
        return week

    def draw_week(self, week):
        for i in range(7):
            if week[i].day == datetime.datetime.now().day:
                print(f"{bcolors.HEADER}{week[i].day}\t{bcolors.ENDC}", end="")
            print(f"{week[i].day}\t", end="")
        print()

