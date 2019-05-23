from flask import Flask, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

def init_create_tenant(app, path, database):

    @app.route(path, methods=['GET'])
    @jwt_required
    def create_tenant():
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        database.create_tenant(current_user)
        return jsonify(logged_in_as=current_user), 200