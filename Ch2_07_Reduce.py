'''
Complete the join and the join_first_sentences functions.

join()
This is a helper function we'll use in join_first_sentences. It takes two inputs:

A "doc_so_far" accumulator string. It's similar to the sum_so_far variable in the example above.
A "sentence" string. This is the next string we want to add to the accumulator.
It returns the result of concatenating the "doc" and "sentence" strings together, with a period and a space in between. For example:

doc = "This is the first sentence"
sentence = "This is the second sentence"
print(join(doc, sentence))
# This is the first sentence. This is the second sentence


join_first_sentences()
It accepts two arguments:

A list of sentence strings
An integer n
It should use the built-in functools.reduce() function alongside your join function to return a single string: 
the result of joining the first n sentences in the list. It should also add a final period (but no trailing space) to the end of the final "reduced" string.

If n is zero, just return an empty string.

Use list slicing to get the first n sentences. For example:

fruits = ["apple", "banana", "cherry", "date"]
print(fruits[:2])
# ["apple", "banana"]

Here's an example of the expected behavior:
joined = join_first_sentences(
    ["This is the first sentence", "This is the second sentence", "This is the third sentence"],
    2
)
print(joined)
# This is the first sentence. This is the second sentence.
'''

import functools as ft

def join(doc_so_far: str, sentence:str) -> str:
    return(f"{doc_so_far}. {sentence}")


def join_first_sentences(sentences: list[str], n:int) -> str:
    if n <= 0:
        return ""
    
    first_n_sentances: list[str] = sentences[:n]
    joined_sentances: str = ft.reduce(join,first_n_sentances)

    return(joined_sentances)
