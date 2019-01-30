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

def GetAll():
    result = Movies.query.all()
    if result is None:
        raise InvalidUsage('Error, No Movies in the Database', status_code= 400)
    else: 
        return Movies.serialize_list(result)

def GetMovie(id):
    result = Movies.query.get(id)
    if result is None:
        raise InvalidUsage('Error, Movie not found', status_code= 404)
    else:
        return Movies.serialize_list(result)


def CreateMovie(film):
    result = Movies.createDict(film)
    if result is None:
        raise InvalidUsage('Error, Movie cannot be created', status_code =404)
    else: 
        db.session.add(result)
        db.session.commit()
        return Movies.serialize_list(result)

def dropMovie(id):
    result = Movies.query.filter_by(id=id).first()
    if result is None:
        raise InvalidUsage('Error, Movie does not exist', status_code = 404)
    else: 
        db.sessions.delete(result)
        db.sessions.commit()
        return Movies.serialize_list(result)


