from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

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
    release_date = Column(String(15))
    IMDB = Column(String(140), nullable = True)

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
