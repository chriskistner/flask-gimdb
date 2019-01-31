from dbmodels import Movies, Actors, MovieActors
from app import db

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        result = dict(self.payload or ())
        result['message'] = self.message
        return result

def getAllMovies():
    result = Movies.query.all()
    if result is None:
        raise InvalidUsage('Error, No Movies in the Database', status_code= 400)
    else: 
        return Movies.serialize_list(result)

def getMovie(id):
    result = Movies.query.get(id)
    if result is None:
        raise InvalidUsage('Error, Movie not found', status_code= 404)
    else:
        return Movies.createDict(result)

def addMovie(film):
    newFilm = Movies(film['name'], film['description'], film['release_date'], film['rating'], film['poster_url'])
    if film is None:
        raise InvalidUsage('Error, Movie cannot be created', status_code =404)
    else: 
        db.session.add(newFilm)
        db.session.commit()
        db.session.refresh(newFilm)
        return newFilm.id

def updateMovie(id, data):
    movie = Movies.query.filter_by(id = id).update({'name': data['name'], 'description': data['description'], 'release_date': data['release_date'], 'rating': data['rating'], 'poster_url': data['poster_url']})
    db.session.commit()
    db.session.flush()
    result = getMovie(id)
    return result

def deleteMovie(id):
    result = Movies.query.get(id)
    if result is None:
        raise InvalidUsage('Error, Movie does not exist', status_code = 404)
    else: 
        db.session.delete(result)
        db.session.commit()
        return Movies.createDict(result)


