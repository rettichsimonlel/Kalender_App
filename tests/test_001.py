from model import User, Data, Kalender
import datetime

def test_yes():
    assert True

def test_user():
    user = User(user_name="Simon",password="Kennwort1")
    assert user.user_name=="Simon" and user.password=="Kennwort1"

def test_data():
    _data = Data(date=datetime.datetime.now(), text="Test data")
    assert _data.date.day==datetime.datetime.now().day and _data.text=="Test data"

def test_kalender():
    kalender = Kalender(title="Test title")
    assert kalender.title=="Test title"

