#!/usr/bin/env python3
"""school by topic"""


def schools_by_topic(mongo_collection, topic):
    """schools_by_topic

    Args:
        mongo_collection (object):
        topic (string):

    Returns:
        list:
    """
    documents = mongo_collection.find({"topics": topic})
    list_docs = [i for i in documents]
    return list_docs
