#!/usr/bin/env python3
"""insert school"""


def insert_school(mongo_collection, **kwargs):
    """insert_school

    Args:
        mongo_collection (mb):

    Returns:
        mb:
    """
    doc_id = mongo_collection.insert(kwargs)
    return doc_id
