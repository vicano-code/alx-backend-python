#!/usr/bin/env python3
"""
duck type an iterable object
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Takes an iterable list and returns a list of tuples """
    return [(i, len(i)) for i in lst]
