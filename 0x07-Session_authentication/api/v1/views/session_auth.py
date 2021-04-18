#!/usr/bin/env python3
"""session auth"""

from flask import request, abort, request, jsonify
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """login

    Returns:
       dict : users
    """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    try:
        user = User.search({'email': email})
        if not user:
            return jsonify({"error": "no user found for this email"}), 404
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    for u in user:
        if not u.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    session_id = auth.create_session(user[0].id)
    Name = os.getenv('SESSION_NAME')
    result = jsonify(user[0].to_json())
    result.set_cookie(Name, session_id)
    return result


@app_views.route('/auth_session/logout',
                 methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """logout

    Returns:
        dict: empty
    """
    from api.v1.app import auth

    if auth.destroy_session(request) is None:
        abort(404)
    else:
        return jsonify({}), 200
