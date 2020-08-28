class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __repr__(self):
        """Return this point/vector as a string in the form "(x, y)" """
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)

        
class PointSortKey:
    """A class for use as a key when sorting points wrt bottommost point"""
    def __init__(self, p, bottommost):
        """Construct an instance of the sort key"""
        self.direction = p - bottommost
        self.is_bottommost = self.direction.lensq() == 0  # True if p == bottommost
        
    def __lt__(self, other):
        """Compares two sort keys. p1 < p2 means the vector the from bottommost point
           to p2 is to the left of the vector from the bottommost to p1.
        """
        if self.is_bottommost:
            return True   # Ensure bottommost point is less than all other points
        elif other.is_bottommost:
            return False  # Ensure no other point is less than the bottommost
        else:
            area = self.direction.x * other.direction.y - other.direction.x * self.direction.y
            return area > 0

def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise"""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
	 # May want to throw an exception if area == 0
    return area > 0       
                
def simple_polygon(points):
    '''Returns a simple polygon using is_ccw'''
    anchor = min(points, key=lambda p: (p.y, p.x))
    simple_poly = sorted(points, key=lambda p: PointSortKey(p, anchor))
    return simple_poly

def graham_scan(points):
    '''Returns the convex hull of a set of points'''
    bottommost = min(points, key=lambda p: (p.y, p.x))
    simple_poly = simple_polygon(points)
    n = len(simple_poly)
    stack = [simple_poly[_] for _ in range(3)]
    for i in range(3, n):
        while not is_ccw(stack[-2], stack[-1], simple_poly[i]):
            stack.pop()
        stack.append(simple_poly[i])
    
    return stack

points = [
    Vec(100, 100),
    Vec(0, 100),
    Vec(100, 0),
    Vec(0, 0),
    Vec(49, 50)]
verts = graham_scan(points)
for v in verts:
    print(v)