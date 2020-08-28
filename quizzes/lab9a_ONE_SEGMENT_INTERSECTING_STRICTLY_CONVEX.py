class Vec:
    """A simple vector in 2D. Also use for points (position vector)"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y
        
    def lensq(self):
        return self.dot(self)
        
        
def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise"""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
	 # May want to throw an exception if area == 0
    return area > 0       
                
        
def signed_area(a, b, c):
    """Twice the area of the triangle abc.
       Positive if abc are in counter clockwise order.
       Zero if a, b, c are colinear.
       Otherwise negative.
    """
    p = b - a
    q = c - a
    return p.x * q.y - q.x * p.y


def is_on_segment(p, a, b):
    """Checks if the point p, lies on the line segment b - a
    """
    area = signed_area(p, a, b)
    len_pa = (p-a).lensq()
    len_pb = (p-b).lensq()
    len_ab = (a-b).lensq()
    if area == 0 and len_pa <= len_ab and len_pb <= len_ab:
        return True
    return False


def intersecting(a, b, c, d):
    """Checks if the line b - a intersects with the line d - c
    """
    cd_check = is_ccw(a, d, b) != is_ccw(a, c, b)
    ab_check = is_ccw(d, b, c) != is_ccw(d, a, c)
    return cd_check and ab_check

	
def is_strictly_convex(vertices):
    convex = True
    n = len(vertices)
    i = -2
    j = -1
    k = 0
    while convex and k < n:
        a = vertices[i]
        b = vertices[j]
        c = vertices[k]
        if not is_ccw(a, b, c):
            convex = False
        else:
            i += 1
            j += 1
            k += 1
    return convex

	
verts = [
    (0, 0),
    (0, 100),
    (100, 100),
    (100, 0)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))