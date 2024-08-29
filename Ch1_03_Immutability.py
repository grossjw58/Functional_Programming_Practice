'''
The add_prefix function accepts 2 arguments:

"document": a string
"documents": the current tuple of strings
It should do 2 things:

Add a prefix of X. to the beginning of the new document, where X is the next index in the tuple. (The first document should be 0. , next should be 1. , etc.)
Return the documents tuple with the new document added to the end.
Run the code to see the error. Whoever wrote this code assumed that documents is a list, but it's a tuple!

Fix the bug. Instead of attempting to mutate the input tuple, create a brand new tuple with the new document added to the end and return that.
'''

def add_prefix(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = (prefix + document,)
    return documents + new_doc