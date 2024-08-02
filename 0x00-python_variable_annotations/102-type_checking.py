#!/usr/bin/env python3
"""
Use mypy to validate the following piece of code and apply any
necessary changes.
"""
from typing import Tuple, List, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: Tuple = tuple([
      item for item in lst
      for i in range(factor)
    ])
    return list(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
