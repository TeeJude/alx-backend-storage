#!/usr/bin/env python3
"""
Module that contains function that returns the list of school
"""
import pymongo

def schools_by_topic(mongo_collection, topic):
    """
    function that returns topic
    """
    return mongo_collection.find({"topics": topic})
