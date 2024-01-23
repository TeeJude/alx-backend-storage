#!/usr/bin/env python3
"""This module contains function that inserts documents"""
import pymongo

def insert_school(mongo_collection, **kwargs):
    """Function that inserts a new document"""
    new_doc = mongo_collection.insert_one(kwargs).insert_id
    return new_doc
