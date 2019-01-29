from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dbcon

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = dbcon.DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
db.init_app(app)


@app.route('/')

def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()