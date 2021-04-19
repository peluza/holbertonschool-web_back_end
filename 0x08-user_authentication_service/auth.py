#!/usr/bin/env python3
"""auth"""

import bcrypt


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
