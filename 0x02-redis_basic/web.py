#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""
import requests
from functools import lru_cache
from time import sleep

@lru_cache(maxsize=128, typed=False)
def get_page(url: str) -> str:
    count_key = f"count:{url}"
    count = get_page.cache.get(count_key, 0)
    count += 1
    get_page.cache[count_key] = count
    response = requests.get(url)
    sleep(5)
    get_page.cache[url] = response.text
    get_page.cache.expire(url, 10)
    return response.text

get_page.cache = {}

url_to_fetch = "http://slowwly.robertomurray.co.uk/delay/5000/url/text"
html_content = get_page(url_to_fetch)
print(html_content)
print(f"The URL '{url_to_fetch}' was accessed {get_page.cache[f'count:{url_to_fetch}']} times.")