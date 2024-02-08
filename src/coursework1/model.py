# Adapted from https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#define-models
from typing import List
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from coursework1 import db

class Dataset(db.Model):
    __tablename__ = "dataset"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    location: Mapped[str] = mapped_column(db.Text, nullable=False)
    ps_enroll_2019: Mapped[int] = mapped_column(db.Integer, nullable=False)
    ps_eligible_2019: Mapped[int] = mapped_column(db.Integer, nullable=False)
    sc_enroll_2019: Mapped[int] = mapped_column(db.Integer, nullable=False)
    sc_eligible_2019: Mapped[int] = mapped_column(db.Integer, nullable=False)
    ps_enroll_2018: Mapped[int] = mapped_column(db.Integer, nullable=False)
    ps_eligible_2018: Mapped[int] = mapped_column(db.Integer, nullable=False)
    sc_enroll_2018: Mapped[int] = mapped_column(db.Integer, nullable=False)
    sc_eligible_2018: Mapped[int] = mapped_column(db.Integer, nullable=False)
    ps_enroll_2017: Mapped[int] = mapped_column(db.Integer, nullable=False)
    ps_eligible_2017: Mapped[int] = mapped_column(db.Integer, nullable=False)
    sc_enroll_2017: Mapped[int] = mapped_column(db.Integer, nullable=False)
    sc_eligible_2017: Mapped[int] = mapped_column(db.Integer, nullable=False)
    ps_enroll_2016: Mapped[int] = mapped_column(db.Integer, nullable=False)
    ps_eligible_2016: Mapped[int] = mapped_column(db.Integer, nullable=False)
    sc_enroll_2016: Mapped[int] = mapped_column(db.Integer, nullable=False)
    sc_eligible_2016: Mapped[int] = mapped_column(db.Integer, nullable=False)
    ps_enroll_2015: Mapped[int] = mapped_column(db.Integer, nullable=False)
    ps_eligible_2015: Mapped[int] = mapped_column(db.Integer, nullable=False)
    sc_enroll_2015: Mapped[int] = mapped_column(db.Integer, nullable=False)
    sc_eligible_2015: Mapped[int] = mapped_column(db.Integer, nullable=False)


    # user_id: Mapped[int] = mapped_column(db.Integer, ForeignKey("user.user_id"))
    #  # add relationship to the parent table, User, which has a relationship called 'dataset'
    # user: Mapped["User"] = relationship("User", back_populates="datasets")

# filtercharts = db.Table('filtercharts',
#     db.Column('filter_id', db.Integer, db.ForeignKey('filter_id'), primary_key=True),
#     db.Column('chart_id', db.Intenger, db.ForeignKey('chart_id'), primary_key=True)
# )

# class Filters(db.Model):
#     __tablename__ = "filters"
#     filter_id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
#     location = db.Column(db.Text, nullable=False)
#     year = db.Column(db.Integer, nullable=False)
#     school_type = db.Column(db.Text)
#     chart_type = db.Column(db.Text)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# class Charts(db.Model):
#     __tablename__ = "charts"
#     chart_id = db.Column(db.Integer, primary_key=True)
#     location = db.Column(db.Text, nullable=False)
#     year = db.Column(db.Integer, nullable=False)
#     school_type = db.Column(db.Text)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
# class User(db.Model):
#     id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
#     username = mapped_column(db.Text, unique=True)
#     email: Mapped[str] = mapped_column(db.Text, unique=True, nullable=False)
#     password: Mapped[str] = mapped_column(db.Text, unique=True, nullable=False)


    # def __init__(self, email: str, password: str):
    #     """
    #     Create a new User object using hashing the plain text password.
    #     :type password_string: str
    #     :type email: str
    #     :returns None
    #     """
    #     self.email = email
    #     self.password = password