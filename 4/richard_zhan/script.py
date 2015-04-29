import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    points = []

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    stack = [ tmp ]
    screen = new_screen()
    print "----------------------------------------"
    for symbol in symbols:
        print symbol
    print "----------------------------------------"
    for command in commands:
        print command

    for command in commands:
        if command[0] == "push":
            stack.append(stack[-1])
        elif command[0] == "move":
            matrix_mult(make_translate(command[1],command[2],command[3]), stack[-1])
        elif command[0] == "box":
            m = []
            add_box( m, command[1], command[2], command[3], command[4], command[5], command[6] )
            for x in stack:
                matrix_mult(x,m)
            for x in m:
                points.append(x)
            draw_polygons( m, screen, color )
        elif command[0] == "rotate" and command[1] == "y":
            matrix_mult(make_rotY(command[2]),stack[1])
        elif command[0] == "display":
            display(screen)




   
   
