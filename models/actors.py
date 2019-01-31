from dbmodels import *
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

def getAllActors():
    result = Actors.query.all()
    if result is None:
        raise InvalidUsage('Error, Actors Database is Unavailable', status_code = 400)
    else: 
        return Actors.serialize_list(result)

def addActor(star):
    newActor = Actors(star['name'], star['biography'], star['profile_url'], star['birth_date'])
    if newActor is None:
        raise InvalidUsage('Error, new actor missing data', status_code = 400)
    else:
        db.session.add(newActor)
        db.session.commit()
        db.session.refresh()
        return newActor.id

def deleteActor(id):
    result = Actorts.query.get(id)
    if result is None:
        raise InvalidUsage('Error, actor does not exist', status_code=404)
    else:
        db.session.delete(result)
        db.session.commit()
        return Actors.createDict(result)

def getActors(id):
    result = Actors.query.get(id)
    if result is None:
        raise InvalidUsage('Error, Actor Not Found', status_code=404)
    else: 
        return Actors.createDict(result)

