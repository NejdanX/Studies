import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class User(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    modified_data = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())
    jobs = orm.relation("Jobs", back_populates='user')

    def __str__(self):
        return f'{self.surname} {self.name} {self.age} {self.position} {self.speciality}\n' \
               f'{self.address} {self.email} {self.hashed_password}'

    def __repr__(self):
        return '<Colonist> {} {} {}'.format(self.id, self.surname, self.name)
