from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from db_factory import DBFactory
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

from endpoints import uninitialized_jwt_endpoints, uninitialzed_endpoints

# Connect to database
db_string = "postgres://docker:docker@localhost:32769"
engine = create_engine(db_string)
database = DBFactory(engine)

# Setup tables
database.drop_all_tables(log_level=1)
database.create_all_tables(log_level=1)

app = Flask(__name__)
api = Api(app)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

# Setup endpoints that require JSON web tokens
for endpoint_initializer, path in uninitialized_jwt_endpoints:
    endpoint_initializer(app, path)

# Setup endpoints that do NOT need json web tokens
for endpoint, path in uninitialzed_endpoints:
    api.add_resource(endpoint, path)

if __name__ == '__main__':
    app.run(debug=True)