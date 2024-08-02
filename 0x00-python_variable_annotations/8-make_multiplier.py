#!/usr/bin/env python3
"""
Complex types - functions
A type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that multiplies a float by multiplier """
    def multiplier_func(n: float) -> float:
        return n * multiplier
    return multiplier_func
