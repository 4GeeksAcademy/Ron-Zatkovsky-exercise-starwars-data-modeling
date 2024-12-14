import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id=Column(Integer,primary_key=True)
    user_name=Column(String(250), nullable=False)
    email=Column(String(250),nullable=False)

    def __ref__(self):
        return f'<User {self.person}>'
    
    def serialize(self):
        return {
            'id':self.id,
            'user_name':self.user_name,
            'email':self.email,
        }
    
class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name=Column(String(250),nullable=False)
    last_name=Column(String(250),nullable=False)
    user_id=Column(Integer,ForeignKey('user.id'),nullable=False)
    user=relationship(User)

    def __ref__(self):
        return f'<Person {self.user}>'
    
    def serialize(self):
        return {
            'id':self.id,
            'first_name':self.first_name,
            'last_name':self.last_name,
        }

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'),nullable=False)
    person = relationship(Person)

    def __ref__(self):
        return f'<Address {self.person}>'
    
    def serialize(self):
        return {
            'id':self.id,
            'street_name':self.street_name,
            'street_number':self.street_number,
            'post_code':self.post_code,
            'person_id':self.person_id,
            'name':self.name,
            'person':self.person,
        }



class Planets(Base):
    __tablename__ = 'planets'
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('user.id'),nullable=False)
    population=Column(Integer,nullable=False)
    climate=Column(String,nullable=False)

    user=relationship(User)

    def __ref__(self):
        return f'<Planets {self.user}>'
    
    def serialize(self):
        return {
            'id':self.id,
            'user_id':self.user_id,
            'population':self.population,
            'climate':self.climate,
        }

class Characters(Base):
    __tablename__ = 'characters'
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('user.id'),nullable=False)
    name=Column(Integer,nullable=False)
    race=Column(String,nullable=False)
    description=Column(String,nullable=False)
    user=relationship(User)

    def __ref__(self):
        return f'<Characters {self.user}>'
    
    def serialize(self):
        return {
            'id':self.id,
            'user_id':self.user_id,
            'name':self.name,
            'race':self.race,
            'description':self.description,
        }

class Favorites(Base):
    __tablename__ = 'favorites'
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('user.id'),nullable=False)
    planet_id=Column(Integer,ForeignKey('planets.id'),nullable=False)
    character_id=Column(Integer,ForeignKey('characters.id'),nullable=False)
    user=relationship(User)
    planets=relationship(Planets)
    characters=relationship(Characters)
    
    def __ref__(self):
        return f'<Favorites {self.user}>'
    
    def serialize(self):
        return {
            'id':self.id,
            'user_id':self.user_id,
            'planet_id':self.planet_id,
            'character_id':self.character_id,
        }

class Comment(Base):
    __tablename__ = 'comment'
    id=Column(Integer,primary_key=True)
    comment_text=Column(String(250))
    author_id=Column(Integer,ForeignKey('user.id'),nullable=False)
    planet_id=Column(Integer,ForeignKey('planets.id'),nullable=False)
    character_id=Column(Integer,ForeignKey('characters.id'),nullable=False)
    user=relationship(User)
    planets=relationship(Planets)
    characters=relationship(Characters)

    def __ref__(self):
        return f'<Comment {self.user}>'
    
    def serialize(self):
        return {
            'id':self.id,
            'author_id':self.author_id,
            'planet_id':self.planet_id,
            'character_id':self.character_id,
            'comment_text':self.comment_text
        }

class Media(Base):
    __tablename__ = 'media'
    id=Column(Integer,primary_key=True)
    type=Column(String(250),nullable=False)
    url=Column(String(250),nullable=False)
    planet_id=Column(Integer,ForeignKey('planets.id'),nullable=False)
    character_id=Column(Integer,ForeignKey('characters.id'),nullable=False)
    planets=relationship(Planets)
    characters=relationship(Characters)

    def __ref__(self):
        return f'<Media {self.id}>'
    
    def serialize(self):
        return {
            'id':self.id,
            'type':self.type,
            'planet_id':self.planet_id,
            'character_id':self.character_id,
            'url':self.url
        }
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
