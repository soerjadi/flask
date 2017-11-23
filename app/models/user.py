# -*- coding: utf-8 -*-
from app import db
from base_model import BaseModel


class User(BaseModel):
    """
    Define user table 
    """

    __tablename__ = "users"

    name = db.Column(db.String(32), nullable=False)
    full_name = db.Column(db.String(155), nullable=False)
    email = db.Column(db.String(155), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.SmallInteger, nullable=False, default=0)

    def __init__(self, name, full_name, email, password, role):
        self.name = name
        self.full_name = full_name
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return "<User %r>" % self.name
