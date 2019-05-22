from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token
from hashlib import sha384

def init_signup(app, path, database):

    @app.route(path, methods=['POST'])
    def signup():
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        firstname = request.json.get('firstname', None)
        lastname = request.json.get('lastname', None)
        password = request.json.get('password', None)
        email = request.json.get('email', None)

        if not firstname:
            return jsonify({"msg": "Missing firstname parameter"}), 400
        if not lastname:
            return jsonify({"msg": "Missing lastname parameter"}), 400
        if not email:
            return jsonify({"msg": "Missing email parameter"}), 400
        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400

        if database.find_user(email) == (None, None, None, None, None):
            database.create_user(firstname, lastname, email, password)
        else:
            return jsonify({"msg": "Email already in use"}), 400

        firstname, lastname, _, _, user_id = database.find_user(email)
        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=email)
        ret = {'access_token': access_token, 'firstname': firstname, 'lastname': lastname, 'user_id': user_id}
        return jsonify(ret), 200
