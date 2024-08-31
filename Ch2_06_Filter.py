'''
Complete the remove_invalid_lines function. It accepts a document as input. It should:

Use the built-in filter function and a lambda to return a copy of the input document
Remove any lines that start with a - character.
Keep all other lines and preserve trailing newlines.
For example, this:

* Star Wars episode 1 is underrated
- Star Wars episode 9 is fine
* Star Wars episode 3 is the best

Should become:

* Star Wars episode 1 is underrated
* Star Wars episode 3 is the best
'''

def remove_invalid_lines(document):
    document_lines = document.split("\n")
    filtered_lines = list(filter(lambda x: not(x.startswith("-")), document_lines))
    rejoined_doc = "\n".join(filtered_lines)

    return(rejoined_doc)