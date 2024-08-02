#!/usr/bin/env python3
"""
Basic Type-Annotations: floor
A type-annotated function floor which takes a float n as
argument and returns the floor of the float
"""
import math


def floor(n: float) -> int:
    """ rounds down a float """
    return math.floor(n)
