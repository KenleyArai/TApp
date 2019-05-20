from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from db import DB


db_string = "postgres://docker:docker@localhost:32769"
engine = create_engine(db_string)
database = DB(engine)

database.drop_all_tables()
database.create_all_tables()

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)