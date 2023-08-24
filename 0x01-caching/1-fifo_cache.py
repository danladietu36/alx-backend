#!/usr/bin/env python3
"""First-In First-Out caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A class of an  object that allows you store and
    retrieve items from a dictionary with a FIFO
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """Initializes the class.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item into the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves an item by key from the cache.
        """
        return self.cache_data.get(key, None)
