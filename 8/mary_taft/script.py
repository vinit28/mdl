import mdl
from display import *
from matrix import *
from draw import *

#runs an mdl script
def run(filename):
    color = [255, 255, 255]
    tmp = identity_matrix()

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "parsing failed"
        return

    stack = [tmp]
    screen = new_screen()
        
    for command in commands:
        print command
