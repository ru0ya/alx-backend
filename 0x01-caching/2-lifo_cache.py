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

    def put(self, key, item):
        """
        Assigns the dictionary self.cache_data the item
        value for the key 'key'
        if key or items is None, does nothing
        """
        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_item = list(self.cache_data.keys())[- 1]
            self.cache_data.pop(last_item)
            print("DISCARD: ", key)

        self.cache_data[key] = item

    def get(self, key):
        """
        Returns value in self.cache_data linked to key
        if key is none or if key does not exist in self.cache_data
        Returns none
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
