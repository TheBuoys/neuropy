from enum import Enum

class Color(Enum):
    BLACK           = 30
    RED             = 31
    GREEN           = 32
    YELLOW          = 33
    BLUE            = 34
    MAGENTA         = 35
    CYAN            = 36
    WHITE           = 37
    RESET           = 39

def colorprint(color, text, end='\n'):
    """Print text in selected color using ANSI color codes."""
    print('\033[' + str(color.value) + 'm' +  text + '\033[0m', end=end)
