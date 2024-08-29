'''
Fix the format_line function. It should apply the following transformations in order:

Strip whitespace from the beginning and end of the line.
Capitalize every character in the line.
Remove any periods from the line.
Suffix the line with an ellipsis: words go here...
Run the code. You should see that some subtle bugs are present.

Break up the function to make it easier to debug. Use print() statements to see what's going on at each step.

Tips
Be careful about whitespace! It's easy to miss in console output. I sometimes add a character, like a | to the beginning and end of a string to make whitespace more obvious when print debugging.

.replace(old, new) can be used to replace all instances of a character in a string.
.upper() capitalizes an entire string, .capitalize() capitalizes the first letter.
.strip() removes whitespace from the beginning and end of a string, .lstrip() and .rstrip() remove whitespace from the left and right respectively.
'''

def format_line(line: str) -> str:
    stripped_line: str = line.strip()
    print(stripped_line)
    capitalized_line: str = stripped_line.upper()
    print(capitalized_line)
    commas_removed: str = capitalized_line.replace(".", "")
    print(commas_removed)

    return (f"{commas_removed}...")
    
