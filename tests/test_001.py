from model import User
from my_calender import Calender

def test_yes():
    assert True


def test_user():
    user = User(user_name="Simon",password="Kennwort1")
    assert user.user_name=="Simon" and user.password=="Kennwort1"

def test_make_week():
    assert Calender != None

