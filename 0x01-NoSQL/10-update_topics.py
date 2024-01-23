#!/usr/bin/env python3
"""Module that contains function that changes all topics of school document
based on name"""

def update_topics(mongo_collection, name, topics):
    """Function to uppdate topics of school document"""
    return mongo_collection.update_many(
            {"name": name},
            {"$set": {"topic": topic}}
    )
