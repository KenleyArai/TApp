from flask import Flask, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

def init_get_roles(app, path, database):

    @app.route(path, methods=['GET'])
    @jwt_required
    def get_roles():
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        tenant, manager, owner = database.get_roles(current_user)
        ret = {'is_tenant': tenant is not None, 'is_manager': manager is not None, 'is_owner': owner is not None}
        return jsonify(ret), 200