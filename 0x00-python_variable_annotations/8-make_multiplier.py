#!/usr/bin/env python3
"""8-make_multipler.py"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """make_multiplier

    Args:
        multiplier (float): takes a float

    Returns:
        typing.Callable[[float], float]:  multiplies a float by multiplier.
    """
    return lambda x: multiplier * x
