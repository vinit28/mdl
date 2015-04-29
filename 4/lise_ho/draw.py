from display import *
from matrix import *
import math
from math import cos, sin, pi

MAX_STEPS = 100

def add_box(poly,x,y,z,l,h,d):
    # need to be added in counter clockwise order
    #front face
    add_tri(poly, x,y,z, x,y-h,z,   x+l,y-h,z);
    add_tri(poly, x,y,z, x+l,y-h,z, x+l,y,z);
    #back face
    add_tri(poly, x,y-h,z-d, x,y,z-d, x+l,y-h,z-d);
    add_tri(poly, x+l,y-h,z-d, x,y,z-d,  x+l,y,z-d);
    #top face
    add_tri(poly, x,y,z-d, x,y,z,  x+l,y,z-d);
    add_tri(poly, x+l,y,z-d, x,y,z,  x+l,y,z);
    #bottom face
    add_tri(poly, x,y-h,z, x,y-h,z-d, x+l,y-h,z-d);
    add_tri(poly, x,y-h,z, x+l,y-h,z-d, x+l,y-h,z);
    #left face
    add_tri(poly, x,y,z,   x,y,z-d, x,y-h,z);
    add_tri(poly, x,y-h,z, x,y,z-d, x,y-h,z-d);
    #right face
    add_tri(poly,  x+l,y,z-d,  x+l,y,z,      x+l,y-h,z);
    add_tri(poly,  x+l,y,z-d, x+l,y-h,z,  x+l,y-h,z-d);
      
#add_polygon( ) function
def add_tri(poly, x,y,z,x1,y1,z1,x2,y2,z2): #adds for the polygons using triangles
    add_point(poly, x,y,z)
    add_point(poly, x1,y1,z1)
    add_point(poly, x2,y2,z2)

def add_triPoint(poly, p1, p2, p3):
    try:
        add_tri(poly, p1[0], p1[1], p1[2], p2[0], p2[1], p2[2], p3[0], p3[1], p3[2])
    except:
        pass

def add_sphere( poly, cx, cy, cz, r, step ):
    
    num_steps = int(MAX_STEPS / step)
    temp = []

    generate_sphere( temp, cx, cy, cz, r, step )

    lat = 0
    lat_stop = num_steps
    longt = 0
    longt_stop = num_steps
    
    while lat < lat_stop+1:
        longt = 0
        while longt < longt_stop:
            ind = lat * num_steps + longt 
            index = ind % len(temp)
            try:
                q = temp[index+num_steps+1]
                add_triPoint(poly,temp[index], temp[index+1+num_steps], temp[index+num_steps])
                add_triPoint(poly,temp[index], temp[index+1], temp[index+num_steps+1])
            except:
                print index, num_steps
            longt+= 1
        lat+= 1

def generate_sphere( temp, cx, cy, cz, r, step ):
    rotation = 0
    rot_stop = MAX_STEPS
    circle = 0
    circ_stop = MAX_STEPS

    while rotation < rot_stop + 1:
        circle = 0
        rot = float(rotation) / MAX_STEPS
        while circle <= circ_stop :
            
            circ = float(circle) / MAX_STEPS
            x = r * cos( pi * circ ) + cx
            y = r * sin( pi * circ ) * cos( 2 * pi * rot ) + cy
            z = r * sin( pi * circ ) * sin( 2 * pi * rot ) + cz
            
            add_point(temp, x,y,z)
            circle+= step
        rotation+= step
    i = 0
  
def add_torus( poly, cx, cy, cz, r0, r1, step ):
    num_steps = int(MAX_STEPS / step)
    temp = []

    generate_torus( temp, cx, cy, cz, r0, r1, step )

    lat = 0
    lat_stop = num_steps
    longt = 0
    longt_stop = num_steps
    
    while lat < lat_stop + 1:
        longt = 0
        while longt < longt_stop:
            ind = lat * num_steps + longt 
            index = ind % len(temp)
            try:
                q = temp[index+num_steps+1]
                add_triPoint(poly,temp[index], temp[index+1+num_steps], temp[index+num_steps])
                add_triPoint(poly,temp[index], temp[index+1], temp[index+num_steps+1])
            except:
                print index, num_steps
            longt+= 1
        lat+= 1

def generate_torus( temp, cx, cy, cz, r0, r1, step ):
    rotation = 0
    rot_stop = MAX_STEPS
    circle = 0
    circ_stop = MAX_STEPS

    while rotation < rot_stop + 1:
        circle = 0
        rot = float(rotation) / MAX_STEPS
        while circle < circ_stop + 1:
            
            circ = float(circle) / MAX_STEPS
            x = (cos( 2 * pi * rot ) * (r0 * cos( 2 * pi * circ) + r1 ) + cx)
            y = r0 * sin(2 * pi * circ) + cy
            z = (sin( 2 * pi * rot ) * (r0 * cos(2 * pi * circ) + r1))
            add_point( temp, x, y, z )
            circle+= step
        rotation+= step

def add_box0(points, x,y,z,l,h,d):
    print "I want to draw only the vertices of my box"
    add_edge(points,x,y,z,x,y,z)
    add_edge(points,x,y-h,z,x,y-h,z)
    add_edge(points,x+l,y,z,x+l,y,z)
    add_edge(points,x+l,y-h,z,x+l,y-h,z)
    add_edge(points,x,y,z-d,x,y,z-d)
    add_edge(points,x,y-h,z-d,x,y-h,z-d)
    add_edge(points,x+l,y,z-d,x+l,y,z-d)
    add_edge(points,x+l,y-h,z-d,x+l,y-h,z-d)

def add_sphere0(points,cx,cy,r,step):
    print "I want my sphere with points"
    t = 0
    c = 0
    cz = 0
    while c < 1 + step: 
        t = 0
        while t < 1 + step :
            theta = t*2.0*math.pi
            p = c*1.0*math.pi
            x = r*math.cos(theta) + cx
            y = r*math.cos(p)*math.sin(theta) + cy
            z = r*math.sin(theta)*math.sin(p) + cz
            add_edge(points,x,y,z,x,y,z);
            t += step
        c += step

def add_torus0(points,cx,cy,r,r2,step):
    t = 0
    c = 0
    cz = 0
    while c < 1 + step: #circle rotation  # 0 -> a little over 1
        p = c*2.0*math.pi
        t = 0 #need to reset t
        while t < 1 + step :  # 0 -> a little over 1
            theta = t*2.0*math.pi
           
            x = math.cos(p)*(r*math.cos(theta) + r2) + cx
            y = r*math.sin(theta) + cy
            z = -1*math.sin(p)*(r*math.cos(theta)+r2) + cz
            add_edge(points,x,y,z,x,y,z);
            t += step
        c += step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    xm = generate_curve_coefs(x0,x1,x2,x3,curve_type)
    ym = generate_curve_coefs(y0,y1,y2,y3,curve_type)
    t = 0
    while (t <= 1.0+step):
        x = xm[0][0]*(t*t*t) + xm[0][1]*(t*t) + xm[0][2]*t + xm[0][3]
        y = ym[0][0]*(t*t*t) + ym[0][1]*(t*t) + ym[0][2]*t + ym[0][3]
        add_edge(points,x0,y0,0,x,y,0)
        x0 = x
        y0 = y
        t += step
        
def add_circle( points, cx, cy, cz, r, step ):
    t = 0
    ang = t*2.0*math.pi
    x = cx
    y = cy
    z = cz
    x0 = r*math.cos(ang) + cx;
    y0 = r*math.sin(ang) + cy;
    while t <= step+1 : #1.05 or something <-step
        ang = t*2.0*math.pi
        x = r*math.cos(ang) + cx;
        y = r*math.sin(ang) + cy;
        add_edge(points,x0,y0,cz,x,y,cz);
        x0 = x;
        y0 = y;
        t += step   
   
def draw_lines( matrix, screen, color ):
    if len( matrix ) == 0:
        print "No line-drawing in this script"
        return
    if len( matrix ) < 2:
        print "Need at least 2 points to draw a line"
    p = 0
    while p < len( matrix ) - 1:
        draw_line( screen, matrix[p][0], matrix[p][1],
                   matrix[p+1][0], matrix[p+1][1], color )
        p+= 2

def surface_normal(p1,p2,p3):
    A= [p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2]]
    B= [p3[0]-p1[0], p3[1]-p1[1], p3[2]-p1[2]]
    N = [A[1]*B[2]-A[2]*B[1], 
         A[2]*B[0]-A[0]*B[2],
         A[0]*B[1]-A[1]*B[0]]
    return N

def dot_product(N,V): #p1,p2,p3 arrays of point coords
    return N[0]*V[0] + N[1]*V[1] + N[2]*V[2]

def draw_triangles(poly,  screen, color):
    # go through the polygon matrix and draw lines of each fo the three points
    if len ( poly ) < 3 and len( poly ) > 0: #if poly is 0, it skip the loop...
        print "You need at least 3 points to draw a triangle"
    V = [0,0,-1] #view vector
    t = 0
    while t < len ( poly ) - 1:
        N = surface_normal(poly[t], poly[t+1], poly[t+2])
        V = [0,0,-1]
        dot = dot_product(N,V)
        if dot < 0: #if cos delta is < 0, it is visible
            draw_line(screen, poly[t][0], poly[t][1], poly[t+1][0], poly[t+1][1], color)
            draw_line(screen, poly[t+1][0], poly[t+1][1], poly[t+2][0], poly[t+2][1], color)
            draw_line(screen, poly[t+2][0], poly[t+2][1], poly[t][0], poly[t][1], color)
        t+=3
    
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )

def draw_line( screen, x0, y0, x1, y1, color ):
    dx = x1 - x0
    dy = y1 - y0
    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp
    
    if dx == 0:
        y = y0
        while y <= y1:
            plot(screen, color,  x0, y)
            y = y + 1
    elif dy == 0:
        x = x0
        while x <= x1:
            plot(screen, color, x, y0)
            x = x + 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            d = d - dy
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            d = d - dx
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            d = d + dy
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx

