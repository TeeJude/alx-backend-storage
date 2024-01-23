#!/usr/bin/env python3
"""This module contains function that list all document"""
import pymongo

def list_all(mongo_collection):
    """lists all collections"""
    if not mongo_collection:
        return[]
    return list(mongo_collection.find())
