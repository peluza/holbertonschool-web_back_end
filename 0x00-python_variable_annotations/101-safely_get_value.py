#!/usr/bin/env python3
"""101-safely_get_value.py"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')
unionTNone = Union[T, None]
unionAnyT = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: unionTNone) -> unionAnyT:
    """safely_get_value

    Args:
        dct (Mapping): Mapping
        key (Any): Any
        default (unionTNone): unionTNone

    Returns:
        unionAnyT: unionAnyT
    """
    if key in dct:
        return dct[key]
    else:
        return default
