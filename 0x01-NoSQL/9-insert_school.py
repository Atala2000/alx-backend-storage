#!/usr/bin/env python3
"""
Module to insert document
"""
def insert_school(mongo_collection, **kwargs):
    for key, value in kwargs.items():
        object_id =  mongo_collection.insert_one(kwargs)
        return object_id.inserted_id