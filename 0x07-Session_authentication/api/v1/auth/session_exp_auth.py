#!/usr/bin/env python3
"""session exp auth"""

from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta

class SessionExpAuth(SessionAuth):
    """SessionExpAuth"""
    def __init__(self):
        """__init__
        """
        try:
            self.session_duration = int(getenv('SESSION_DURATION', 0))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """create_session

        Args:
            user_id (str, optional): Defaults to None.

        Returns:
          Session ID created
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        SessionExpAuth.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """user_id_for_session_id

        Args:
            session_id (, optional): Defaults to None.

        Returns:
           dict: from the session dictionary
        """
        if session_id is None:
            return None

        SessionDict = SessionExpAuth.user_id_by_session_id.get(
            session_id, None)
        if SessionDict is None:
            return None
        if 'created_at' not in SessionDict:
            return None

        if self.session_duration <= 0:
            return SessionDict.get('user_id')

        CreateTime = SessionDict.get('created_at')
        Session = timedelta(seconds=self.session_duration)
        ExpTime= CreateTime + Session

        if ExpTime< datetime.now():
            return None
        return SessionDict.get('user_id')
