#!/usr/bin/python3
"""app"""

from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def message() -> str:
    """message

    Returns:
        str: message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """users

    Returns:
        str: message
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": "<registered email>",
                        "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """login

    Returns:
        str: cookie
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if not AUTH.valid_login(email, password):
        abort(401)
    else:
        session_id = AUTH.create_session(email)
        res = jsonify({"email": "<user email>", "message": "logged in"})
        res.set_cookie("session_id", session_id)
        return res

@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """logout

    Returns:
        str : path = /
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return "/"
    else:
        abort(403)

@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": "<user email>"})
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
