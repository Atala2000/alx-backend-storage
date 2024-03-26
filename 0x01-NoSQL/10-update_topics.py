#!/usr/bin/env python3
"""
Module to update topics
"""


def update_topics(mongo_collection: object, name: str, topics: list):
    """
    Changes many documents
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
