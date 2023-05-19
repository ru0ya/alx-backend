#!/usr/bin/env python3
"""
LIFO caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    A caching system
    A class constructor that inherits from BaseCaching
    """
    def __init__(self):
        """
        child constructor
        """
        super().__init__()
        self.last = []

    def put(self, key, item):
        """
        Assigns the dictionary self.cache_data the item
        value for the key 'key'
        if key or items is None, does nothing
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if key not in self.cache_data:
            self.last.append(key)

        if len(self.last) > BaseCaching.MAX_ITEMS:
            first_out = self.last.pop(-1)
            del self.cache_data[first_out]
            print("DISCARD: {:s}".format(first_out))

    def get(self, key):
        """
        Returns value in self.cache_data linked to key
        if key is none or if key does not exist in self.cache_data
        Returns none
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
