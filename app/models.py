# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 20:34:36 2019

@author: User
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


    
class Post(db.Model):
    __tablename__ = 'graphs'
    
    id = db.Column(db.Integer, primary_key = True)
    func = db.Column(db.String, unique=True)
    img = db.Column(db.String, unique=True)
    
    def __init__(self, func, img):
        self.func = func
        self.img = img

#print(dir(db))