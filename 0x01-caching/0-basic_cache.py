#!/usr/bin/env python3
""" Basic Module for caching
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """Representing an object that allows you store and
    retrieving items from a dictionary.
    """
    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
