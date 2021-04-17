#!/usr/bin/env python3
"""session auth"""

from api.v1.auth.auth import Auth
from uuid import uuid4

class SessionAuth(Auth):
    user_id_by_session_id = {}
    def create_session(self, user_id: str = None) -> str:
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

