#!/usr/bin/env python3
"""auth"""

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
from typing import TypeVar


def _hash_password(password: str) -> str:
    """_hash_password

    Args:
        password (str):

    Returns:
        str: hashed Password
    """
    salt = bcrypt.gensalt()
    code_password = password.encode('utf-8')
    hashedPassword = bcrypt.hashpw(code_password, salt)
    return hashedPassword


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> str:
        """register_user

        Args:
            email (str):
            password (str):

        Raises:
            ValueError: User <user's email> already exists

        Returns:
            str: user
        """
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hash_password = _hash_password(password)
            user = self._db.add_user(
                email=email, hashed_password=hash_password)
            return user
