#!/usr/bin/env python3

"""
This module illustrates how to do simple caching
in python
"""

BaseCaching = __import__("base_caching").BaseCaching

class BasicCache(BaseCaching):
    """BasicCache class that inherits from BaseCaching.
    This class represents a basic caching system with no limit.
    """

    def __init__(self):
        """Initialize BasicCache."""
        super().__init__()

    def put(self, key, item):
        """Store the item in cache_data using key as the identifier.
        
        Args:
            key: Key identifying the item.
            item: Item to be stored in cache.

        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from cache_data using key as the identifier.
        
        Args:
            key: Key identifying the item.

        Returns:
            The item identified by key if it exists in cache_data, None otherwise.
            If key is None, this method returns None.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None