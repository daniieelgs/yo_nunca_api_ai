from db import db
from sqlalchemy import JSON

class UserModel(db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(40), unique=False, nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    
    settings = db.Column(JSON, unique=False, nullable=False)
    
    tokens = db.relationship('SessionTokenModel', back_populates='user', lazy='dynamic', cascade="all, delete")