#!/usr/bin/env python3
"""
class that inherits from BaseCaching and
is a caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic cache
    Inherits from classBaseCaching
    Attributes: put, get
    """
    def put(self, key, item):
        """
        Assigns the dictionary self.cache_data the item
        value for the key 'key'
        if item and key is None returns nothing
        """
        if item is None or key is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns value in self.cache_data linked to key
        if key is None or if key doesnt exist in self.cache_data
        Return None
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)
