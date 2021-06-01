#!/usr/bin/env python3
"""updatre topics"""


def update_topics(mongo_collection, name, topics):
    """update_topics

    Args:
        mongo_collection (object):
        name (string):
        topics (list our string):
    """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_values)
