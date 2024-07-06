#!/usr/bin/env python3
""" Contains the make_multiplier function """
from typing import Callable


def make_multiplier(factor: float) -> Callable[[float], float]:
    """ Makes a multiplier """
    def multiplier(x: float) -> float:
        """ Generate multiplier"""
        return x * factor
    return multiplier
