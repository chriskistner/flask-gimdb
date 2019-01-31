
from models.movies import *

def getAllMovies():
    return GetAll()

def getMovie(id):
    if id is None:
        raise InvalidUsage('Call requires valid Movie ID')
    else:
        return getMovie(id)

def createMovie(data):
    if data['name'] is not None and data['description'] is not None and data['release_date'] is not None and data['rating'] is not None:
        return addMovie(data)
    else:
        raise InvalidUsage('POST movie is missing data')

def updateMovie(id, data):
    movie = getMovie(id)

    if movie is None:
        raise InvalidUsage('Error, Canot find Movie to update')
    else:
        if data['name']:
            movie['name'] = data['name']
        if data['description']:
            movie['description'] = data['description']
        if data['release_date']:
            movie['release_date'] = data['release_date']
        if data['rating']:
            movie['rating'] = data['rating']
        if data['poster_url']:
            movie['poster_url'] = data['poster_url']  
        return updateMovie(id, movie)

def dropMovie(movieId):
    print(movieId)
    if id is None:
        raise InvalidUsage('Call requires valid Movie ID')
    else:
        return deleteMovie(movieId)