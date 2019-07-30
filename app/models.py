# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PostSingle(db.Model):
    __tablename__ = 'calculus'
    
    id = db.Column(db.Integer, primary_key = True)
    func = db.Column(db.String, unique=True)
    img = db.Column(db.String, unique=True)
    
    def __init__(self, func, img):
        self.func = func
        self.img = img

class PostMulti(db.Model):
    __tablename__ = 'multi'
    
    id = db.Column(db.Integer, primary_key = True)
    func = db.Column(db.String, unique=True)
    img = db.Column(db.String, unique=True)
    
    def __init__(self, func, img):
        self.func = func
        self.img = img
