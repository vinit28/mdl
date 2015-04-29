from display import *
from matrix import *
import math

#Go through matrix 2 entries at a time and call
#draw_line on each pair of points
def draw_lines( matrix, screen, color ):
    for i in range(len(matrix))[::2]:
        draw_line(screen,matrix[i][0],matrix[i][1],matrix[i+1][0],matrix[i+1][1],color)
        
#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix,x0,y0,z0)
    add_point(matrix,x1,y1,z1)
    
#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    matrix.append([int(x),int(y),int(z),1])

def add_polygon(matrix, x0, y0, z0, x1, y1, z1, x2, y2, z2):
    add_point(matrix,x0,y0,z0)
    add_point(matrix,x1,y1,z1)
    add_point(matrix,x2,y2,z2)

def draw_polygons(matrix, screen, color):
    for i in range(len(matrix))[::3]:
        if dotProduct(matrix, i) >= 0:
            draw_line(screen,matrix[i][0],matrix[i][1],matrix[i+1][0],matrix[i+1][1],color)
            draw_line(screen,matrix[i+1][0],matrix[i+1][1],matrix[i+2][0],matrix[i+2][1],color)
            draw_line(screen,matrix[i+2][0],matrix[i+2][1],matrix[i][0],matrix[i][1],color)
    
def parametric(matrix, step, f, g, h = None):
    if h == None:
        h = lambda x: 0
    t = 0
    oldX = f(0)
    oldY = g(0)
    oldZ = h(0)
    while t < 1.00001:
        t += step
        x = f(t)
        y = g(t)
        z = h(t)
        add_edge(matrix, oldX, oldY, oldZ, x, y, z)
        oldX = x
        oldY = y
        oldZ = z
    
#Add circle with center (x,y,z) and radius r to matrix
def add_circle(matrix, cx, cy, cz, r, step):
    def x(t):
        return r * math.cos(2 * math.pi * t) + cx
    def y(t):
        return r * math.sin(2 * math.pi * t) + cy
    parametric(matrix, step, x, y)

def add_curve(matrix, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type):
    if curve_type == "hermite":
        h = [[2, -3, 0, 1],
             [-2, 3, 0, 0],
             [1, -2, 1, 0],
             [1, -1, 0, 0]]
        g = [[x0, x2, x1 - x0, x3 - x2],
             [y0, y2, y1 - y0, y3 - y2]]
        matrix_mult(h,g)
        def x(t):
            return g[0][0] * t ** 3 + g[0][1] * t ** 2 + g[0][2] * t + g[0][3]
        def y(t):
            return g[1][0] * t ** 3 + g[1][1] * t ** 2 + g[1][2] * t + g[1][3]
        parametric(matrix,step,x,y)
    elif curve_type == "bezier":
        b = [[-1, 3, -3, 1],
             [3, -6, 3, 0],
             [-3, 3, 0, 0],
             [1, 0, 0, 0]]
        g = [[x0, x1, x2, x3],
             [y0, y1, y2, y3]]
        matrix_mult(b,g)
        def x(t):
            return g[0][0] * t ** 3 + g[0][1] * t ** 2 + g[0][2] * t + g[0][3]
        def y(t):
            return g[1][0] * t ** 3 + g[1][1] * t ** 2 + g[1][2] * t + g[1][3]
        parametric(matrix,step,x,y)
    else:
        print "Curve type not found"

#3D shapes
def add_prism(matrix, x, y, z, width, height, depth):
    add_polygon(matrix, x, y, z, x, y - height, z, x + width, y - height, z)
    add_polygon(matrix, x, y, z, x + width, y - height, z, x + width, y, z)
    add_polygon(matrix, x, y, z, x + width, y, z, x + width, y, z + depth)
    add_polygon(matrix, x, y, z, x + width, y, z + depth, x, y, z + depth)
    add_polygon(matrix, x, y, z + depth, x, y - height, z + depth, x, y - height, z)
    add_polygon(matrix, x, y, z + depth, x, y - height, z, x, y, z)
    add_polygon(matrix, x + width, y, z, x + width, y - height, z, x + width, y - height, z + depth)
    add_polygon(matrix, x + width, y, z, x + width, y - height, z + depth, x + width, y, z + depth)
    add_polygon(matrix, x + width, y, z + depth, x + width, y - height, z + depth, x, y - height, z + depth)
    add_polygon(matrix, x + width, y, z + depth, x, y - height, z + depth, x, y, z + depth)
    add_polygon(matrix, x, y - height, z, x, y - height, z + depth, x + width, y - height, z + depth)
    add_polygon(matrix, x, y - height, z, x + width, y - height, z + depth, x + width, y - height, z)

def add_sphere(matrix, cx, cy, cz, r, step):
    j = 0
    while j < 1.00001 - step:
        k = 0
        a = j + step
        #edge case 1
        x1 = r * math.cos(math.pi * k) + cx
        y1 = r * math.sin(math.pi * k) * math.cos(2 * math.pi * j) + cy
        z1 = r * math.sin(math.pi * k) * math.sin(2 * math.pi * j) + cz
        x2 = r * math.cos(math.pi * (k + step)) + cx
        y2 = r * math.sin(math.pi * (k + step)) * math.cos(2 * math.pi * a) + cy
        z2 = r * math.sin(math.pi * (k + step)) * math.sin(2 * math.pi * a) + cz
        x3 = r * math.cos(math.pi * (k + step)) + cx
        y3 = r * math.sin(math.pi * (k + step)) * math.cos(2 * math.pi * j) + cy
        z3 = r * math.sin(math.pi * (k + step)) * math.sin(2 * math.pi * j) + cz
        add_polygon(matrix, x1, y1, z1, x2, y2, z2, x3, y3, z3)
        x1 = x3
        y1 = y3
        z1 = z3
        k += step
        while k < 1.00001 - 2 * step:
            #p_i+n
            x2 = r * math.cos(math.pi * k) + cx
            y2 = r * math.sin(math.pi * k) * math.cos(2 * math.pi * a) + cy
            z2 = r * math.sin(math.pi * k) * math.sin(2 * math.pi * a) + cz
            k += step
            #p_i+n+1
            x3 = r * math.cos(math.pi * k) + cx
            y3 = r * math.sin(math.pi * k) * math.cos(2 * math.pi * a) + cy
            z3 = r * math.sin(math.pi * k) * math.sin(2 * math.pi * a) + cz
            add_polygon(matrix, x1, y1, z1, x2, y2, z2, x3, y3, z3)
            #p_i+1
            x4 = r * math.cos(math.pi * k) + cx
            y4 = r * math.sin(math.pi * k) * math.cos(2 * math.pi * j) + cy
            z4 = r * math.sin(math.pi * k) * math.sin(2 * math.pi * j) + cz
            add_polygon(matrix, x1, y1, z1, x3, y3, z3, x4, y4, z4)
            #update p_i
            x1 = x4
            y1 = y4
            z1 = z4
        #edge case 2
        x2 = r * math.cos(math.pi * k) + cx
        y2 = r * math.sin(math.pi * k) * math.cos(2 * math.pi * a) + cy
        z2 = r * math.sin(math.pi * k) * math.sin(2 * math.pi * a) + cz
        x3 = r * math.cos(math.pi * (k + step)) + cx
        y3 = r * math.sin(math.pi * (k + step)) * math.cos(2 * math.pi * a) + cy
        z3 = r * math.sin(math.pi * (k + step)) * math.sin(2 * math.pi * a) + cz
        add_polygon(matrix, x1, y1, z1, x2, y2, z2, x3, y3, z3)
        j += step

def add_torus(matrix, cx, cy, r1, r2, step):
    j = 0
    while j < 1.00001 - step:
        k = 0
        a = j + step
        while k < 1.00001:
            #p_i
            x1 = math.cos(2 * math.pi * j) * (r1 * math.cos(2 * math.pi * k) + r2) + cx
            y1 = r1 * math.sin(2 * math.pi * k) + cy
            z1 = -math.sin(2 * math.pi * j) * (r1 * math.cos(2 * math.pi * k) + r2)
            #p_i+n
            x2 = math.cos(2 * math.pi * a) * (r1 * math.cos(2 * math.pi * k) + r2) + cx
            y2 = r1 * math.sin(2 * math.pi * k) + cy
            z2 = -math.sin(2 * math.pi * a) * (r1 * math.cos(2 * math.pi * k) + r2)
            k += step
            #p_i+n+1
            x3 = math.cos(2 * math.pi * a) * (r1 * math.cos(2 * math.pi * k) + r2) + cx
            y3 = r1 * math.sin(2 * math.pi * k) + cy
            z3 = -math.sin(2 * math.pi * a) * (r1 * math.cos(2 * math.pi * k) + r2)
            #p_i+1
            x4 = math.cos(2 * math.pi * j) * (r1 * math.cos(2 * math.pi * k) + r2) + cx
            y4 = r1 * math.sin(2 * math.pi * k) + cy
            z4 = -math.sin(2 * math.pi * j) * (r1 * math.cos(2 * math.pi * k) + r2)
            add_polygon(matrix, x1, y1, z1, x2, y2, z2, x3, y3, z3)
            add_polygon(matrix, x1, y1, z1, x3, y3, z3, x4, y4, z4)
        j += step

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0, x1, y1, color ):
    if (x1 >= x0):
        x = x0
        y = y0
        a = 2*(y1 - y0)
        b = -2*(x1 - x0)
        if (y1 >= y0):
            if x0 != x1 and 1. * (y1 - y0)/(x1 - x0) <= 1:
                d = a + b/2
                while (x <= x1):
                    plot(screen,color,x,y)
                    if d > 0:
                        y += 1
                        d += b
                    x += 1
                    d += a
            else:
                d = a/2 + b
                while (y <= y1):
                    plot(screen,color,x,y)
                    if d < 0:
                        x += 1
                        d += a
                    y += 1
                    d += b
        else:
            if x0 != x1 and 1. * (y1 - y0)/(x1 - x0) >= -1:
                d = a - b/2
                while (x <= x1):
                    plot(screen,color,x,y)
                    if d < 0:
                        y -= 1
                        d -= b
                    x += 1
                    d += a
            else:
                d = a/2 - b
                while (y >= y1):
                    plot(screen,color,x,y)
                    if d > 0:
                        x += 1
                        d += a
                    y -= 1
                    d -= b
    else:
        draw_line(screen,x1,y1,x0,y0,color)        
