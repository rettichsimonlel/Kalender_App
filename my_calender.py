import datetime
from bcolors import bcolors

class Calender():
    def __init__(self):
        self.current_week = datetime.datetime.now().isocalendar().week
        self.current_date = datetime.datetime.now()
        self.monday = self.current_date + datetime.timedelta(days = -self.current_date.weekday())
        self.current_monday = self.monday

    def make_week(self):
        week = []
        week.append(self.current_monday)
        for i in range(1, 7):
            next_day = self.current_monday + datetime.timedelta(days=i)
            week.append(next_day)
        return week

    def draw_week(self):
        week = self.make_week()
        for i in range(7):
            if week[i].day == datetime.datetime.now().day:
                print(f"{bcolors.HEADER}{week[i].day}\t{bcolors.ENDC}", end="")
            else:
                print(f"{week[i].day}\t", end="")
        print()

    def next_week(self):
        self.current_monday = self.current_monday + datetime.timedelta(days=7)
        self.draw_week()

    def previos_week(self):
        self.current_monday = self.current_monday - datetime.timedelta(days=7)
        self.draw_week()

