
from models.movies import *

def GetAll():
    return GetAll()

def GetMovie(id):
    if id is None:
        raise InvalidUsage('Call requires valid Movie ID')
    else:
        return GetMovie(id)

def CreateMovie(data):
    if data.name is not None and data.description is not None and data.release_date is not None and data.rating is not None:
        movieData = {}
        return CreateMovie(movieData)
    else:
        raise InvalidUsage('POST movie is missing data')

def DropMovie(id):
    if id is None:
        raise InvalidUsage('Call requires valid Movie ID')
    else:
        return DropMovie(id)