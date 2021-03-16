#!/usr/bin/env python3
"""7-to_kv.py"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """to_kv

    Args:
        k (str): string
        v (typing.Union[int, float]):  int OR floa

    Returns:
        typing.Tuple[str, float]: he first element of the tuple is the \
            string k. The second element is the square of the int/float v
    """
    return (k, v * v)
