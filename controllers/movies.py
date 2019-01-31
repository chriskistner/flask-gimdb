
from models.movies import *

def getAll():
    return GetAll()

def getMovie(id):
    if id is None:
        raise InvalidUsage('Call requires valid Movie ID')
    else:
        return GetMovie(id)

def createMovie(data):
    if data['name'] is not None and data['description'] is not None and data['release_date'] is not None and data['rating'] is not None:
        return addMovie(data)
    else:
        raise InvalidUsage('POST movie is missing data')

def dropMovie(movieId):
    print(movieId)
    if id is None:
        raise InvalidUsage('Call requires valid Movie ID')
    else:
        return deleteMovie(movieId)