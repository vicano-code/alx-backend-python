#!/usr/bin/env python3
"""
Duck typing - first element of a sequence
The following code was annotated with the correct duck-typed annotations
"""
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    returns the first element of a sequence if not empty
    otherwise returns None
    """
    if lst:
        return lst[0]
    else:
        return None
