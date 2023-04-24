#!/usr/bin/python3
"""
Database storage engine using SQLAlchemy with a mysql+mysqldb database
connection.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os


class DBStorage():
    """
    Define attributes and methods of used to store objects
    in the database
    """

    __engine = __session = None

    def __init__(self):
        """Constructor to create instance attributes"""
        self.__user = os.getenv("HBNB_MYSQL_USER")
        self.__pwd = os.getenv("HBNB_MYSQL_PWD")
        self.__host = os.getenv("HBNB_MYSQL_HOST")
        self.__db = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}:3306/{}".format(
                    self.__user, self.__pwd, self.__host, self.__db),
                pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query the database for objects of a particular class
        Return all objects if nothing is passed
        """
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.user import User
        from models.review import Review
        from models.amenity import Amenity
        if not cls:
            objs = self.__session.query(State, City,
                                        Place, User, Amenity, Review).all()
        else:
            objs = self.__session.query(cls)
        final_dict = {}
        [final_dict.update({
            f"{type(item).__name__}.{item.id}": item
            }) for item in objs]
        return final_dict

    def new(self, obj):
        """Add a new object to the session"""
        self.__session.add(obj)

    def save(self):
        """Commit all objects on the session to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and a session"""
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.user import User
        from models.review import Review
        from models.amenity import Amenity
        Base.metadata.create_all(self.__engine)
        sf = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sf)
        self.__session = Session()

    def close(self):
        """Close the current session"""
        self.__session.close()
