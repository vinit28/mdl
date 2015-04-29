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

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    stack = [ tmp ]
    screen = new_screen()
        
    for command in commands:
        print command
        operator = command[0]
        if operator == "push":
            stack.append(stack[0])
        elif operator == "pop":
            stack = stack[1:]
        elif operator == "move":
            M = make_translate(command[1], command[2], command[3])
            if command[4] != None:
                scalar_mult(M, command[4])
            matrix_mult(M, stack[0])
        elif operator == "rotate2":
            if command[1] == "x":
                M = make_rotX(command[2])
            elif command[1] == "y":
                M = make_rotY(command[2])
            elif command[1] == "z":
                M = make_rotZ(command[2])
            if command[3] != None:
                scalar_mult(M, command[3])
            matrix_mult(M, stack[0])
        elif operator == "scale":
            M = make_scale(command[1], command[2], command[3])
            if command[4] != None:
                scalar_mult(M, command[4])
            matrix_mult(M, stack[0])
        elif operator == "box":
            points = []
            add_prism(points, command[1], command[2], command[3], command[4], command[5], command[6])
            matrix_mult(stack[0], points)
            draw_polygons(points, screen, color)
        elif operator == "sphere":
            points = []
            add_sphere(points, command[1], command[2], command[3], command[4])
            matrix_mult(stack[0], points)
            draw_polygons(points, screen, color)
        elif operator == "display":
            display(screen)
