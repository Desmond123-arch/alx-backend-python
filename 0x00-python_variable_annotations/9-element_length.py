#!/usr/bin/env python3
""" Contains the function element_length """
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns the list of a lent fo sequences """
    return [(i, len(i)) for i in lst]
