'''
Complete the file_type_getter function. This function accepts a list of tuples, where each tuple contains:

A "file type" (e.g. "code", "document", "image", etc)
A list of associated file extensions (e.g. ['.py', '.js'] or ['.docx', '.doc'])
First, use loops to create a dictionary that maps each file extension to its corresponding file type, based on the input tuples. 
For example, the resulting dictionary might be:

{
    '.doc': 'text',
    '.docx': 'document',
    '.py': 'code',
    '.jpg': 'image'
}

Next, return a lambda function that accepts a string (a file extension) and returns the corresponding file type. 
If the extension is not found in the dictionary, the lambda function should return "Unknown". I used the .get dictionary method to handle this.
'''
from typing import Any

def file_type_getter(file_extension_tuples: list[tuple[str,list[str]]]):
    file_types: dict[str:str] = {}

    for tup in file_extension_tuples:
        file_type, extensions = tup
        for extension in extensions:
            file_types[extension] = file_type
    
    get_extension = lambda ext: file_types.get(ext,"Unknown")

    return(get_extension)
