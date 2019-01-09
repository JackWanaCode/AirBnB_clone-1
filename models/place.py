#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey

class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey
                      ('cities.id', ondelete="CASCADE"),
                      nullable=False)
    user_id = Column(String(60), ForeignKey
                      ('users.id', ondelete="CASCADE"),
                      nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    reviews = relationship("Review", cascade='all, delete-orphan',
                          backref='place')

    @property
    def reviews(self):
        """ returns Review instances
        """
        all_reviews = models.file_storage.all(models.Review)
        select_reviews = []
        for v in all_reviews.values():
            if v.place_id == self.id:
                list.append(v)
        return select_reviews

    place_amenities = relationship("Amenity", secondary=place_amenity)

    place_amenity = Table('IDK', metadata = Base.metadata,
            Column('place_id', String(60), ForeignKey=('places.id', ondelete="CASCADE"),
            primary_key=True, nullable=False),
            Column('amenity_id', String(60), ForeignKey=('amenities.id', ondelete="CASCADE"),
            primary_key=True, nullable=False)
        )
