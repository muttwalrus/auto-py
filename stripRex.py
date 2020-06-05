import re

def stripper(x, y = None):
    if y != None:
        stripRex = re.compile(r'^[' + y + ']+|['+ y + ']+$')
    else:
        stripRex = re.compile(r'^\s+|\s+$')
    return stripRex.sub('', x)
