import pytest
import datetime
import calendar
from bcolors import bcolors
import os
from my_calender import Calender

def test_init():
    c = Calender()
    assert c.current_week == datetime.datetime.now().isocalendar().week
    assert c.current_date.day == datetime.datetime.now().day
    assert c.monday == c.current_date + datetime.timedelta(days = -c.current_date.weekday())
    assert c.current_monday == c.monday
    assert c.data == []

def test_make_week():
    c = Calender()
    week = c.make_week()
    assert week[0] == c.current_monday
    for i in range(1, 7):
        next_day = c.current_monday + datetime.timedelta(days=i)
        assert week[i] == next_day

def test_draw_week(capfd):
    c = Calender()
    c.draw_week()
    captured = capfd.readouterr()
    assert calendar.month_name[c.make_week()[0].month] in captured.out
    assert calendar.month_name[c.make_week()[6].month] in captured.out

def test_next_week(capfd):
    c = Calender()
    current_week = c.make_week()
    c.next_week()
    captured = capfd.readouterr()
    assert calendar.month_name[current_week[0].month] in captured.out
    assert calendar.month_name[c.make_week()[0].month] in captured.out

def test_previous_week(capfd):
    c = Calender()
    current_week = c.make_week()
    c.next_week()
    c.previos_week()
    captured = capfd.readouterr()
    assert calendar.month_name[current_week[0].month] in captured.out
    assert calendar.month_name[c.make_week()[0].month] in captured.out
 