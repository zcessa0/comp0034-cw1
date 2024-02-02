# Adapted from https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#define-models
from typing import List
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src import db


class User(db.Model):
    __tablename__ = "user"
    user_id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    email: Mapped[str] = mapped_column(db.Text, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.Text, unique=True, nullable=False)
    # one-to-many relationship with Dataset, the relationship in Dataset is called 'user'
    datasets: Mapped[List["Dataset"]] = relationship(back_populates="user")

    def __init__(self, email: str, password: str):
        """
        Create a new User object using hashing the plain text password.
        :type password_string: str
        :type email: str
        :returns None
        """
        self.email = email
        self.password = password

class Dataset(db.Model):
    __tablename__ = "dataset"
    dataset_id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    location: Mapped[str] = mapped_column(db.Text, nullable=False)
    school_type: Mapped[str] = mapped_column(db.Text, nullable=False)
    year: Mapped[int] = mapped_column(db.Integer, nullable=False)
    total_enrollment: Mapped[int] = mapped_column(db.Integer, nullable=False)
    total_eligible: Mapped[int] = mapped_column(db.Integer, nullable=False)
    user_id: Mapped[int] = mapped_column(db.Integer, ForeignKey("user.id"))
     # add relationship to the parent table, User, which has a relationship called 'dataset'
    user: Mapped["User"] = relationship("User", back_populates="datasets")

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