#!/usr/bin/env python3
""" Contains the make_multiplier function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Makes a multiplier """
    return lambda x: x * multiplier
