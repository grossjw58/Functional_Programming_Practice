'''
Complete the deduplicate_lists function. 
It takes two lists as input lst1 and lst2 and an optional reverse boolean, and returns a sorted list of unique elements. 
If reverse is True, then the returned list should be sorted in descending order. Use sorted and pass it the reverse parameter.
'''
from typing import Any

def deduplicate_lists(lst1: list[Any], lst2: list[Any], reverse: bool =False) -> list[Any]:
    full_list: list[Any] = lst1 + lst2 
    set_conversion: set[Any] = set(full_list) ##sets remove duplicates by default
    sorted_list: list[Any] = sorted(list(set_conversion),reverse = reverse) #convert back to list and sort
    return (sorted_list)