from flask import Flask, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

def init_create_owner(app, path, database):

    @app.route(path, methods=['GET'])
    @jwt_required
    def create_owner():
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        database.create_owner(current_user)
        return jsonify(logged_in_as=current_user), 200