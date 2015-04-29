import math

def make_translate( x, y, z ):
    m = new_matrix()
    ident(m)
    m[3][0] = x
    m[3][1] = y
    m[3][2] = z
    return m
    
def make_scale( x, y, z ):
    m = new_matrix()
    m[0][0] = x
    m[1][1] = y
    m[2][2] = z
    m[3][3] = 1
    return m
    
def make_rotX( theta ):    
    m = new_matrix()
    theta = math.pi * theta / 180
    m[0][0] = 1
    m[1][1] = math.cos(theta)
    m[2][1] = -math.sin(theta)
    m[1][2] = math.sin(theta)
    m[2][2] = math.cos(theta)
    m[3][3] = 1
    return m
    
def make_rotY( theta ):
    m = new_matrix()
    theta = math.pi * theta / 180
    m[0][0] = math.cos(theta)
    m[2][0] = -math.sin(theta)
    m[1][1] = 1
    m[0][2] = math.sin(theta)
    m[2][2] = math.cos(theta)
    m[3][3] = 1
    return m
    
def make_rotZ( theta ):
    m = new_matrix()
    theta = math.pi * theta / 180
    m[0][0] = math.cos(theta)
    m[1][0] = -math.sin(theta)
    m[0][1] = math.sin(theta)
    m[1][1] = math.cos(theta)
    m[2][2] = 1
    m[3][3] = 1
    return m
    
def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i != j:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1
    
def scalar_mult( matrix, x ):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= x
    
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    newM = new_matrix(len(m1[0]),len(m2))
    for i in range(len(m1[0])):
        for j in range(len(m2)):
            sum = 0
            for n in range(len(m2[0])):
                sum += m1[n][i] * m2[j][n]
            newM[j][i] = sum
    for a in range(len(m2)):
        for b in range(len(m2[0])):
            m2[a][b] = newM[a][b]

def dotProduct(matrix, i, viewVector=[0, 0, -1]):
    a = [matrix[i + 1][n] - matrix[i][n] for n in range(3)]
    b = [matrix[i + 2][n] - matrix[i][n] for n in range(3)]
    normal = [a[1] * b[2] - a[2] * b[1],
             a[2] * b[1] - a[1] * b[2],
             a[0] * b[1] - a[1] * b[0]]
    return sum([normal[i] * viewVector[i] for i in range(3)])
