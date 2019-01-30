
import models.movies as model

def getAll():
    return model.getAll()

def GetMovie(id):
    if id is None:
        raise InvalidUsage('Call requires valid Movie ID')
    else:
        return model.GetMovie(id)

def CreateMovie(data):
    if data.name is not None and data.description is not None and data.release_date is not None and data.rating is not None:
        movieData = {}
        return model.create(movieData)
    else:
        raise InvalidUsage('POST movie is missing data')

def DropMovie(id):
    if id is None:
        raise InvalidUsage('Call requires valid Movie ID')
    else:
        return model.DropMovie(id)