#!/usr/bin/env python3
"""6-sum_mixed_list.py"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """sum_mixed_list

    Args:
        mxd_lst (typing.List[typing.Union[int, float]]): ntegers and floats

    Returns:
        float: their sum as a float.
    """
    return sum(mxd_lst)
