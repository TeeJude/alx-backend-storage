#!/usr/bin/env python3
"""
Module contains function to implement get_page. 
Use request module to obtain HTML content of a URL and returns it
and track the number of times a particular URL was accessed
"""
import requests
import redis
from functools import wraps

store = redis.Redis()

def count_url_access(method):
    """
    Counting how many times a URL is accessed
    """
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        store.incr(count_key)
        store.set(cached_key, html)
        store.expire(cached_key, 10)
        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """
    Returns HTML content of a URL
    """
    res = requests.get(url)
    return res.text
