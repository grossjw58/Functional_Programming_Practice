'''
In the world of document conversion, we sometimes need to handle fonts and font sizes.

Complete the get_median_font_size function. Given a list of numbers representing font sizes, return the median of the list.

For example:

[1, 2, 3] => 2
[10, 8, 7, 5] => 7
Copy icon
Notice the second list is out of order. Order the list, then find the middle index, and return the middle number. If there is an even amount of numbers, return the smaller of the two middle numbers (I know it's not a true median, but good for our purposes). If the list is empty, just return None.

Here are some helpful docs:

sorted
len
// (floor division)
To be a good little functional programmer, your code for this lesson should not:

Use loops
Mutate any variables (it's okay to create new ones)
'''
import math
def get_median_font_size(font_sizes: list[int]) -> int:
    sorted_list: list[int] = sorted(font_sizes)
    size: int = len(sorted_list)
    mid_point: int = 0

    if size <= 0:
        return None

    if size % 2 == 0:
        mid_point = (size // 2) - 1
    else:
        mid_point = size // 2 

    return(sorted_list[mid_point])
