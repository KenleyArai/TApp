from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token

def init_login(app, path, database):

    @app.route(path, methods=['POST'])
    def login():
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        username = request.json.get('username', None)
        password = request.json.get('password', None)

        if not username:
            return jsonify({"msg": "Missing username parameter"}), 400

        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400

        if username != 'test' or password != 'test':
            return jsonify({"msg": "Bad username or password"}), 401

        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
