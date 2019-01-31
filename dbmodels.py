from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import inspect, ForeignKey
from app import db

class Movies(db.Model):
    __tablename__ = 'movies'
    id =db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)
    release_date = db.Column(db.DateTime, unique=False, nullable=False)
    rating = db.Column(db.String(5), unique=False, nullable=False)
    poster_url = db.Column(db.Text(), unique=False, nullable=True)
    created_at = db.Column(db.DateTime, unique=False, default=db.func.now(), onupdate=db.func.now())
    # actors = relationship('Actors', secondary = 'MovieActors')

    def __init__(self, name, description, release_date, rating, poster_url):
        self.name = name
        self.description = description
        self.release_date = release_date
        self.rating = rating
        self.poster_url = poster_url

    def createDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    @staticmethod
    def serialize_list(films):
        return [film.createDict() for film in films]

class Actors(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    biography = db.Column(db.Text, unique=False, nullable=False)
    profile_url = db.Column(db.Text, unique=False, nullable=True)
    birth_date = db.Column(db.DateTime, unique=False, nullable=True)
    created_at = db.Column(db.DateTime, unique=False)
    updated_at = db.Column(db.DateTime, unique=False)
    # movies = relationship('Movies', secondary = 'MovieActors')

    def createDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    @staticmethod
    def serialize_list(actors):
        return [actor.createDict() for actor in actors]

class MovieActors(db.Model):
    __tablename__='movie_actors'
    id = db.Column(db.Integer, primary_key=True)
    movies_id = db.Column(db.Integer, db.ForeignKey('movies.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    actors_id = db.Column(db.Integer, db.ForeignKey('actors.id', onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    role = db.Column(db.String(120), nullable=False)
    # movies = relationship("Movies", foreign_keys="movies_id")
    # actors = relationship("Actors", foreign_keys="actors_id")

    def createDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    @staticmethod
    def serialize_list(roles):
        return [actor.toDict() for actor in roles]