#!/usr/bin/bashpython3
"""
Contains class BaseModel1
"""
from datetime import datetime
from os import getenv
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"

if models.storage_t == "db":
        Base = declarative_base()
    else:
            Base = object

class Site(db.Model):
        Id = db.Column(db.Interger, primary key=True)
        name = db.Column(db.String(100), unique=True)
        availability = db.Column(db.boolean)
        panels_cells = db.Column(db.Integer)
        coordinates = db.Column(Float)
        tecnhnolgy = db.Column(db.String(20), unique=true
                                        
    def __init__(self, name, availability, panels_cells, coordinates, technology):
            self.name = name,
            self.availability = availability,
            self. panels_cells = panels_cells,
            self.technology = technology,
