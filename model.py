from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from datetime import datetime

### Code for creating the database
# python -i model.py
# engine = create_engine("sqlite:///ratings.db", echo=True)
# Base.metadata.create_all(engine)


ENGINE = None
Session = None

Base = declarative_base()

### Class declarations go here
class User(Base):
    """ from u.user info """  
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable = True)
    password = Column(String(64), nullable = True)
    age = Column(Integer, nullable = True)
    zipcode = Column(String(15), nullable = True)
    gender = Column(String(10), nullable = True)

class Movie(Base):
    """ from u.items info """
    __tablename__ = "movies"

    id = Column(Integer, primary_key = True)
    movie_title = Column(String(120))
    release_date = Column(DateTime)
    IMDB = Column(String(140), nullable = True)

    def __repr__(self):
        return "Id: %r Movie Title: %r Release Date: %s IMDB: %r" % (self.id, self.movie_title,
                                                                 datetime.strftime(self.release_date, "%d-%b-%Y"), self.IMDB)

class Rating(Base):
    """ from u.data info """
    __tablename__ = "ratings"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer)
    movie_id = Column(Integer)
    rating = Column(Integer)

### End class declarations

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()

