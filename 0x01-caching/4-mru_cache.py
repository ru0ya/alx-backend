#!/usr/bin/env python3
"""
MRU Caching: Most Recently Used
"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    A caching system
    Child class that inherits from parent class BaseCaching
    """
    def __init__(self):
        """
        constructor method
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data the item
        value for the key 'key'

        Arguments: self.key, self.item

        if key or item is None: returns
        If the number of items in self.cache_data is higher that 
        BaseCaching.MAX_ITEMS:
        you must discard the most recently used item
        you must print DISCARD: with the
            key discarded and following by a new line
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:


