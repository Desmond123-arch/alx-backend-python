#!/usr/bin/python3
""" Contains the type-annotated function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a float (k, v)"""
    v = v ** 2
    return (k, v)
