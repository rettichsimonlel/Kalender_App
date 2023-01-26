import sqlalchemy
import sqlalchemy.ext.declarative
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey

Base = sqlalchemy.ext.declarative.declarative_base()


class User(Base):
    """User representation."""

    __tablename__ = "user"
    user_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    user_name = sqlalchemy.Column(sqlalchemy.String, unique=True)
    password = sqlalchemy.Column(sqlalchemy.String)
    data = relationship("Data")

    def __repr__(self):
        """Get representation."""
        return "<User: %s>" % (self.user_name)


class Data(Base):
    """Data representation."""

    __tablename__ = "data"
    data_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    date = sqlalchemy.Column(sqlalchemy.DateTime)
    text = sqlalchemy.Column(sqlalchemy.String)
    user_id = Column(Integer, ForeignKey("user.user_id"))

#
# class Kalender(Base):
#     """Kalender representation."""
#
#     __tablename__ = "kalender"
#     kalender_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
#     title = sqlalchemy.Column(sqlalchemy.String)
#     data = relationship("Data", backref="data_kalender")

