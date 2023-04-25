#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.review import Review
from sqlalchemy.sql.schema import Table

place_amenity = Table("place_amenity", Base.metadata, Column(
        "place_id", String(60), ForeignKey('places.id')), Column(
        "amenity_id", String(60, collation='latin1_swedish_ci'),
        ForeignKey('amenities.id'))
        )


class Place(BaseModel, Base):
    """ A place to stay """
      __tablename__ = 'places'
      city_id = Column(String(60, collation='latin1_swedish_ci'),
                     ForeignKey("cities.id"), nullable=False)
      user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
      name = Column(String(128), nullable=False)
      description = Column(String(1024))
      number_rooms = Column(Integer(), default=0, nullable=False)
      number_bathrooms = Column(Integer(), default=0, nullable=False)
      max_guest = Column(Integer(), default=0, nullable=False)
      price_by_night = Column(Integer(), default=0, nullable=False)
      latitude = Column(Float())
      longitude = Column(Float())
      reviews = relationship("Review", cascade="all, delete",
                               backref="places")
      amenities = relationship("Amenity",
                                 secondary='place_amenity',
                                 viewonly=False,
                                 backref="place_amenities")
    @property
    def reviews(self):
        """
        Returns the list of Reviews instances with place_id
        equals to the current place.id
        """
        from models import storage
        objs = []
        for _, value in storage.all(Review).items():
            if self.id == value.place_id:
                objs.append(str(value))
        return objs

    @property
    def amenities(self):
        """
        Returns the list of Amenity instances based on the attribute.
        Amenity_ids that contains all Amenity.id linked to the Place.
        """
        from models import storage
        from models.amenity import Amenity

        objs = []
        for _, value in storage.all(Amenity).items():
            if value.id in self.amenity_ids:
                objs.append(str(value))
        return objs

    @amenities.setter
    def amenities(self, obj):
        """
        Add an Amenity.id to the attribute amenity_ids.
        Only Amenity object, otherwise, do nothing.
        """
        from models.amenity import Amenity

        if type(obj) is not Amenity:
            return
        self.amenity_ids.append(obj.id)
