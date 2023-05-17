#!/usr/bin/env python3
"""
class FIFOCache that inherits from BaseCaching
and is a caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    a caching system
    """
    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data
        the item value for the key 'key'
        if key or item is none returns nothing
        """
        if item is None or key is None:
            return
        self.cache_data[key] = item

        if key not in self.keys:
            self.keys.append(key)

        last_key = list(self.cache_data)[0]

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(last_key)
            print("DISCARD: ", last_key)

    def get(self, key):
        """
        Returns value in self.cache_data linked to key
        if key is None or doesnt exist in self.cache_data
        Returns None
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data.get(key)
