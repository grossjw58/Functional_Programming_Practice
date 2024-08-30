'''
Debug the hex_to_rgb and is_hexadecimal functions. 
hex_to_rgb should take a hex triplet color code and return three integers for the RGB values using int(). 
int() is not being used correctly, examine the documentation to see how to convert hexadecimal values. 
Use the provided is_hexadecimal function after fixing the bug. 
If the input is not a six character long hexadecimal string, raise an exception "not a hex color string".
'''

def hex_to_rgb(hex_color: str) -> tuple[int]:
    if not isinstance(hex_color,str) or len(hex_color) != 6:
        raise Exception("not a hex color string")
    
    redstr: str = hex_color[:2]
    greenstr: str = hex_color[2:4]
    bluestr: str = hex_color[4:]

    if(is_hexadecimal(redstr) and is_hexadecimal(greenstr) and is_hexadecimal(bluestr)):
        red: int = int(redstr, base = 16)
        blue: int = int(bluestr, base = 16)
        green: int = int(greenstr, base = 16)

        return ((red,green,blue))

    else:
        raise Exception("not a hex color string")
    
def is_hexadecimal(hex_string: str) -> bool:
    try:
       int(hex_string, base = 16) 
       return True
    except:
        raise Exception ("not a hex color string")
        
    


