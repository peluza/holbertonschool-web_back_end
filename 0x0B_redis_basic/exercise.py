#!/usr/bin/env python3
"""exercise"""

import redis
from typing import Union, Optional, Callable
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count_calls

    Args:
        method (typing.Callable):
    Returns:
        typing.Callable:
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """call_history

    Args:
        method (typing.Callable):

    Returns:
        typing.Callable:
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + "outputs", output)

        return output
    return wrapper


def replay(fn: Callable):
    """replay

    Args:
        fn (typing.Callable): display the history of calls
    """
    r = redis.Redis()
    fn_name = fn.__qualname__
    n_calls = r.get(fn_name)
    try:
        n_calls = n_calls.decode("utf-8")
    except Exception:
        n_calls = 0
    print(f'{fn_name} was called {n_calls} times:')

    inputs = r.lrange(fn_name + ":inputs", 0, -1)
    outputs = r.lrange(fn_name + ":outputs", 0, -1)

    for ins, outs in zip(inputs, outputs):
        try:
            ins = ins.decode("utf-8")
        except Exception:
            ins = ""
        try:
            outs = outs.decode("utf-8")
        except Exception:
            outs = ""

        print(f'{fn_name}(*{ins}) -> {outs}')


class Cache:
    """Cache
    """

    def ___init__(self):
        """init
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store

        Args:
            data (typing.Union[str, bytes, int, float]):

        Returns:
            str: uuid
        """
        key_id = str(uuid4())
        self._redis.set(key_id, data)
        return key_id

    def get(self,
            key: str,
            fn: Optional[callable] = None) -> Union[str, bytes, int, float]:
        """get

        Args:
            key (str):
            fn (typing.Optional[callable], optional): Defaults to None.

        Returns:
            typing.Union[str, bytes, int, float]: value
        """
        if fn:
            v = self._redis.get(key)

        return v.decode("utf-8")

    def get_str(self, key: str) -> str:
        """get_str

        Args:
            key (str):

        Returns:
            str: value
        """
        v = self._redis.get(key)
        return v.decode("utf-8")

    def get_int(self, key: str) -> int:
        """get_int

        Args:
            key (str):

        Returns:
            int: value
        """
        v = self._redis.get(key)
        try:
            c = int(v.decode("utf-8"))
        except Exception:
            v = 0
        return v
