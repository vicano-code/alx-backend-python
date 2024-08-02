#!/usr/bin/env python3
"""
More involved type annotations
The correct type annotations were added to the function code below
"""
from typing import Mapping, Any, TypeVar, Union, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None]) -> Union[Any, T]:
    """
    return the value associated with a specified key from a dictionary
    (or any mapping type). If the key is not present in the dictionary, the
    function returns a default value provided by the caller. If no default
    value is provided, it returns None. This approach helps to avoid KeyError
    exceptions when accessing dictionary keys that might not exist
    """
    if key in dct:
        return dct[key]
    else:
        return default
