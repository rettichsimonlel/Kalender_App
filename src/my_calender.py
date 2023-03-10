import datetime
import calendar
from bcolors import bcolors
import os

class Calender():
    def __init__(self):
        self.current_week = datetime.datetime.now().isocalendar().week
        self.current_date = datetime.datetime.now()
        self.monday = self.current_date + datetime.timedelta(days = -self.current_date.weekday())
        self.current_monday = self.monday
        self.data = []

    def make_week(self):
        week = []
        week.append(self.current_monday)
        for i in range(1, 7):
            next_day = self.current_monday + datetime.timedelta(days=i)
            week.append(next_day)
        return week

    def draw_week(self):
        os.system("clear")
        week = self.make_week()
        print(calendar.month_name[week[0].month])
        for i in range(7):
            output = f""
            if week[i].day == datetime.datetime.now().day:
                output += f"{bcolors.HEADER}{week[i].day}: " 
                for data in self.data:
                    if week[i].day == data["date"].day:
                        output += data["data"] + "; "
                output += f"{bcolors.ENDC}"
                print(output)
            else:
                output += f"{week[i].day}: "
                for data in self.data:
                    if week[i].day == data["date"].day:
                        output += data["data"] + "; "
                print(output)
        print(calendar.month_name[week[6].month])
        print()

    def next_week(self):
        self.current_monday = self.current_monday + datetime.timedelta(days=7)
        self.draw_week()

    def previos_week(self):
        self.current_monday = self.current_monday - datetime.timedelta(days=7)
        self.draw_week()
    
    def add(self):
        week = self.make_week()
        choice = input("To what day would you like to add an event: ")
        for i in range(7):
            if str(week[i].day) == choice:
                data = input("Write your event: ")
                self.data.append({"date": week[i], "data": data})
                break
        self.draw_week()

    def update(self):
        week = self.make_week()
        choice = input("What day to change: ")
        for i in range(7):
            if str(week[i].day) == choice:
                fuck_me = []
                for j in range(len(self.data)):
                    if self.data[j]["date"].day == week[i].day and self.data[j]["date"].month == week[i].month and self.data[j]["date"].year == week[i].year:
                        fuck_me.append(self.data[j])
                for j in range(len(fuck_me)):
                    self.data.remove(fuck_me[j])
                data = input("Write your event: ")
                self.data.append({"date": week[i], "data": data})
                break
        self.draw_week()

