import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

class User(Base):
    __tablename__ = 'user'
    ID=Column(Integer,primary_key=True)
    user_name=Column(String(250))
    first_name=Column(String(250))
    last_name=Column(String(250))
    email=Column(String(250))

class Follower(Base):
    __tablename__ = 'follower'
    ID=Column(Integer,primary_key=True)
    user_from_id=Column(Integer,ForeignKey('user.ID'))
    user_to_id=Column(Integer,ForeignKey('user.ID'))
    user=relationship(User)

class Post(Base):
    __tablename__ = 'post'
    ID=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('user.ID'))
    user=relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    ID=Column(Integer,primary_key=True)
    comment_text=Column(String(250))
    author_id=Column(Integer,ForeignKey('user.ID'))
    post_id=Column(Integer,ForeignKey('post.ID'))
    user=relationship(User)
    post=relationship(Post)

class Media(Base):
    __tablename__ = 'media'
    ID=Column(Integer,primary_key=True)
    type=Column(String(250))
    url=Column(String(250))
    post_id=Column(Integer,ForeignKey('post.ID'))
    post=relationship(Post)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
