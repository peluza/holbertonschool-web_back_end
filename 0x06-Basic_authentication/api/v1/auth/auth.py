#!/usr/bin/env python3
"""auth"""

from flask import request
import typing


class Auth():
    """Auth"""

    def require_auth(
            self,
            path: str,
            excluded_paths: typing.List[str]) -> bool:
        """require_auth"""
        if not path:
            return True
        if not excluded_paths or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            path = path + "/"
        if path in excluded_paths:
            return False
        else:
            for p in excluded_paths:
                val = p.find("*")
                if p.endswith("*") and p[:val] == path[:val]:
                    return False
                else:
                    return True

    def authorization_header(self, request=None) -> str:
        """authorization_header"""
        if request is None:
            return None
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None
        else:
            return auth_header

    def current_user(self, request=None) -> typing.TypeVar('User'):
        """current_user"""
        return None
