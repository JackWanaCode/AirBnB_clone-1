#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import os
import json
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __engine:
        __session:
    """
    # __file_path = "file.json"
    # __objects = {}
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(os.environ['HBNB_MYSQL_USER'],
                                             os.environ['HBNB_MYSQL_PWD'],
                                             os.environ['HBNB_MYSQL_HOST'],
                                             os.environ['HBNB_MYSQL_DB'],
                                             pool_pre_ping=True))

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
            if cls is None, return all objects, else return class's
        """
        all_objects = {}
        Base.metadata.create_all(self.__engine, checkfirst=True)
        session_fac = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fac)
        self.__session = Session()
        if cls is None:
            for st in ['State', 'City']:
                for obj in self.__session.query(eval(st)).all():
                    key = str(obj.__class__.__name__) + "." + str(obj.id)
                    all_objects[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                key = str(obj.name) + "." + str(obj.id)
                all_objects[key] = obj
        self.__session.close()
        return all_objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            Base.metadata.create_all(self.__engine, checkfirst=True)
            Session = sessionmaker(bind=self.__engine)
            self.__session = Session()
            self.__session.add(obj)
            self.__session.commit()
            self.__session.close()

    def save(self):
        """serialize the file path to JSON file path
        """
        self.__session.commit()
        self.__session.close()

    def reload(self):
        """serialize the file path to JSON file path
        """
        Base.metadata.create_all(self.__engine)
        session_fac = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fac)
        self.__session = Session()

    def delete(self, obj=None):
        """1 - delete obj from __objects and write to JSON filename
        """
        my_dict = {}
        Base.metadata.create_all(self.__engine, checkfirst=True)
        session_fac = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fac)
        self.__session = Session()
        self.__session.delete(obj)
        self.__session.commit()
        self.__session.close()


        # for k, v in self.__objects.items():
        #     if v is obj:
        #         del self.__objects[k]
        #         break
        # with open(self.__file_path, 'w', encoding="UTF-8") as f:
        #     json.dump(my_dict, f)
