#!/usr/bin/python3

from base_caching import BaseCaching


class BsicCache(BaseCaching):
    """A class that represent adding and retrieval of
       objects from a cache via their keys
    """

    def put(self, key, item):
        """Method to add item to the
        """
        if key is None or item not in self.cache_data:
            return
        self.cache_data = item

    def get(self, key):
        """Method to return an item.
        """
        return self.cache_data.get(key, None)
