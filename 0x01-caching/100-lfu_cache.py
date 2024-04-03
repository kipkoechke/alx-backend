#!/usr/bin/env python3


"""
This module illustrates how to do simple caching
in python. This time, we will do FIFO caching.
If the cache is at maximum capacity, we will discard
the first item in and add the new one (FIFO)
"""

from collections import OrderedDict
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class that inherits from BaseCaching.
    This class represents a caching system using the LFU algorithm.
    """

    def __init__(self):
        """Initialize LFUCache."""
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = Counter()

    def put(self, key, item):
        """Store the item in cache_data using key as the identifier.
        
        Args:
            key: Key identifying the item.
            item: Item to be stored in cache.

        If key or item is None, this method does nothing.
        If the number of items in self.cache_data is higher than BaseCaching.MAX_ITEMS,
        it discards the least frequency used item (LFU algorithm).
        If there is more than 1 item to discard, it uses the LRU algorithm to discard only the least recently used.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
                self.frequency[key] -= 1
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_freq = min(self.frequency.values())
                least_freq_keys = [k for k, v in self.frequency.items() if v == least_freq]
                if len(least_freq_keys) > 1:
                    for k in list(self.cache_data):
                        if k in least_freq_keys:
                            discarded_key = k
                            break
                else:
                    discarded_key = least_freq_keys[0]
                del self.cache_data[discarded_key]
                del self.frequency[discarded_key]
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            self.frequency[key] += 1

    def get(self, key):
        """Retrieve an item from cache_data using key as the identifier.
        
        Args:
            key: Key identifying the item.

        Returns:
            The item identified by key if it exists in cache_data, None otherwise.
            If key is None, this method returns None.
        """
        if key is not None and key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            self.cache_data.move_to_end(key)
            self.frequency[key] += 1
            return value
        return None