# -*- coding: utf-8 -*-
from app import db

class BaseModel(db.Model):
    """
    Define Base abstract model
    """

    __abstract__ = True

    id           = db.Column(db.BigInteger, primary_key=True)
    created_time = db.Column(db.BigInteger, primary_key=True)
    updated_time = db.Column(db.BigInteger, primary_key=True)

