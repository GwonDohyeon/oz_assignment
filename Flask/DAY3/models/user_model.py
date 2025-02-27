# creat model -> create table
from db import db
class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False,unique=True)
    boards = db.relationship('Board', back_populates='author', lazy='dynamic')