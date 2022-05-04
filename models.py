import datetime as dt
import sqlalchemy as sql
import database as _db

class Question(_db.base):
    __tablename__ = 'Questions'
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    question_text = sql.Column(sql.String, index=True, unique=True)
    answer_text = sql.Column(sql.String, index=True)
    datetime_create = sql.Column(sql.DateTime, default=dt.datetime.utcnow)
