from flask import Flask, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

def init_protected(app, path):

    @app.route(path, methods=['GET'])
    @jwt_required
    def protected():
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200