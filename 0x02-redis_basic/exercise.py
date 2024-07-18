#!/usr/bin/env python3
"""
Cache class to store data in Redis.
"""


import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    Cache class that interacts with Redis.
    """

    def __init__(self):
        """
        Initialize the Redis client and flush the database
        """

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis with a random key and returns the key

        Args:
            data (Union[str, bytes, int, float]): The data to be stored

        Returns:
            str: The key under which the data is stored
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally convert it using a callable

        Args:
            key (str): The key to retrieve data
            fn (Optional[Callable]): The function to convert the data

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data in the
            original format or None if key does not exist
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves a UTF-8 string from Redis

        Args:
            key (str): The key to retrieve data

        Returns:
            Optional[str]: The retrieved string or None if key does not exist
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retriev an integer from Redis

        Args:
            key (str): The key to retrieve data

        Returns:
            Optional[int]: The retrieved integer or None if key does not exist
        """
        return self.get(key, int)
