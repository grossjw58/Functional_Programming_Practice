"""
Complete the toggle_case function using string methods. It takes a string as input line, and returns a string.

If line is in titlecase, convert it to all uppercase and add three "!" to the end.
If line is all uppercase, convert it to all lowercase except for the first letter and remove any trailing "!".
If line is all lowercase or only the first letter is capitalized, convert it to title case.
Otherwise, just return line unchanged.
Tips
You will have to use the link to the official Python documentation to find the right string methods. Reading documentation is a skill all developers need to master.
"""

def toggle_case(line: str) -> str | None: 
    if line.istitle():
        upper_case:str = line.upper()
        suffixed: str = f"{upper_case}!!!"
        return (suffixed)
    
    if line.isupper():
        lower_case: str = line.lower()
        capitalized: str = lower_case.capitalize()
        replaced: str = capitalized.rstrip("!")
        return(replaced)

    if len(line) > 0 and line[1:].islower():
        lower_case: str = line.lower()
        title_case: str = lower_case.title()
        return (title_case)
    
    return (line)