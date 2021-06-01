#!/usr/bin/env python3
""" List all documents in Python mandatory """


def list_all(mongo_collection):
    """list_all

    Args:
        mongo_collection (database): [description]

    Returns:
        list: lists all documents
    """
    documents = mongo_collection.find()
    if documents.count() == 0:
        return []
    return documents
