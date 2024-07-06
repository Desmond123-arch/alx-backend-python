#!/usr/bin/env python3
""" Contains the function element_length """
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
