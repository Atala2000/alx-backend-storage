#!/usr/bin/env python3
"""
Module to insert document
"""
def insert_school(mongo_collection: object, **kwargs) -> int:
        """"
        Function that inserts document with arguments
        Args:
            mongo_collection (object): Object containing query
        Returns:
            Inserted id
        """
        object_id =  mongo_collection.insert_one(kwargs)
        return object_id.inserted_id