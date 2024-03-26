#!/usr/bin/env python3
"""
Module to list all documents in a collection
"""
def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection.

    Args:
        mongo_collection: PyMongo collection object.

    Returns:
        A list of all documents in the collection.
        If the collection is empty or doesn't exist, an empty list is returned.
    """
    return list(mongo_collection.find({}))
