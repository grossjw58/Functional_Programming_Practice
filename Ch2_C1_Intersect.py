'''
Complete the get_common_formats function using the .intersection() method. 
It should take in two arguments, formats1 and formats2, each a list of strings representing the file formats supported by two different pieces of software.

It should return a set of strings representing the file formats that are supported by both pieces of software.
'''
from typing import Any

def get_common_formats(formats1: list[Any], formats2: list[Any]) -> set[Any]:
    common_formats: set[Any] = set(formats1).intersection(set(formats2))
    return(common_formats)
