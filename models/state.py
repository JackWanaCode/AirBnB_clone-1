#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete-orphan',
                          backref='state')

    @property
    def cities(self):
        """ returns City instances
        """
        all_cities = models.file_storage.all(models.City)
        select_cities = []
        for v in all_cities.values():
            if v.state_id == self.id:
                list.append(v)
        return select_cities
