import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    color = [0, 120, 255]
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
    polygons = []
    points = []
    print commands
    
    for cmd in commands:
        temp = stack[ len(stack) -1]
        
        if cmd [0][0] == '#':
            pass
        
        elif cmd[0] == 'push':
            temp = stack.append(temp)
        
        elif cmd [0] == 'pop':
            stack.pop()
            temp = stack[len(stack) - 1]
            
        elif cmd [0] == 'move':
            t = make_translate( cmd[1], cmd[2], cmd[3] )
            matrix_mult( t, temp )
            
        elif cmd [0] == 'rotate':
            angel = cmd[2] * ( math.pi / 180 )
            if cmd[1] == 'x':
                r = make_rotX( angel )
            if cmd[1] == 'y':
                r = make_rotY( angel )
            if cmd[1] == 'z':
                r = make_rotZ( angel )
            matrix_mult( r, temp )
                                
        elif cmd [0] == 'scale':
            s = make_scale( cmd[1], cmd[2], cmd[3] )
            matrix_mult( s, temp )
            
        elif cmd [0] == 'box':
            add_box( polygons, cmd[1], cmd[2], cmd[3], cmd[4], cmd[5], cmd[6] )
        elif cmd [0] == 'sphere':
            add_sphere( polygons, cmd[1], cmd[2], 0 , cmd[3], 5 )
        elif cmd [0] == 'torus':
             add_torus( polygons, cmd[1], cmd[2], 0, cmd[3], cmd[4], 5 )
        elif cmd [0] == 'line':
            add_edge( points, cmd[1], cmd[2], cmd[3], cmd[4], cmd[5], cmd[6] )
        elif cmd [0] == 'save':
            screen = new_screen()
            save_extension( screen, commands[c].strip() )
            
        elif cmd [0] == 'display':
            screen = new_screen()
            draw_polygons( polygons, screen, color )
            draw_lines( points, screen, color)
            display( screen )
        else:
            print 'Invalid command: ' + cmd


        

    
      
