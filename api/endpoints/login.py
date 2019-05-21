from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token
from hashlib import sha384

def init_login(app, path, database):

    @app.route(path, methods=['POST'])
    def login():
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        email = request.json.get('email', None)
        password = request.json.get('password', None)

        if not email:
            return jsonify({"msg": "Missing email parameter"}), 400

        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400

        firstname, lastname, dbemail, dbpassword, user_id = database.find_user(email)

        password = sha384(password.encode()).hexdigest()

        if email !=  dbemail or password != dbpassword:
            return jsonify({"msg": "Bad username or password"}), 401

        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
