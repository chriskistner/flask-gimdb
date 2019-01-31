from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import dbcon

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = dbcon.DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
db.init_app(app)

from controllers.movies import *
from models.movies import *

@app.route('/')

def hello_world():
    return 'Hello, World!'

# Movie Routes
@app.route('/movies', methods=['GET', 'POST'])
def moviesRoutes():
    if request.method == 'GET':
        result = getAll()
        return jsonify(result)
    elif request.method == 'POST':
        data= request.get_json()
        result = createMovie(data)
        return jsonify(result)

@app.route('/movies/<movieId>', methods=['GET', 'DELETE'])
def movieRoutes(movieId):
    if request.method == 'GET':
        result = getMovie(movieId)
        return jsonify(result)
    elif request.method == 'DELETE':
        result = dropMovie(movieId)
        return jsonify(result)

# Error Handler Route
# @app.errorhandler(InvalidUsage)
# def handle_invalid_usage(error):
#     response = jsonify(error.to_dict())
#     response.status_code = error.status_code
#     return response

if __name__ == '__main__':
    app.run()
