class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

    def __getitem__(self, axis):
        return self.x if axis == 0 else self.y

    def __repr__(self):
        """String representation of self"""
        return "({}, {})".format(self.x, self.y)
        

class QuadTree:
    """A QuadTree class for COSC262.
       Richard Lobb, May 2019
    """
    MAX_DEPTH = 20
    def __init__(self, points, centre, size, depth=0, max_leaf_points=2):
        self.centre = centre
        self.size = size
        self.depth = depth
        self.max_leaf_points = max_leaf_points
        self.children = []
        # *** COMPLETE ME ***
        self.points = []
        for p in points:
            if self.in_square(p):
                self.points.append(p)
        
        if len(self.points) <= self.max_leaf_points:
            self.is_leaf = True
        else:
            self.is_leaf = False        
            
        if not self.is_leaf and self.depth <= self.MAX_DEPTH:
            for i in range(4):
                child_centre, child_size = self.calc_child(i)
                child = QuadTree(self.points, child_centre, child_size, depth + 1, 
                                 self.max_leaf_points)
                self.children.append(child)           
        
    def calc_child(self, i):
        """Gets child centre and size depending on quadrant
        """
        nsize = self.size / 4
        child_size = self.size / 2
        if i == 0:
            child_centre = Vec(self.centre.x - nsize, self.centre.y - nsize)
        elif i == 1:
            child_centre = Vec(self.centre.x - nsize, self.centre.y + nsize)
        elif i == 2:
            child_centre = Vec(self.centre.x + nsize, self.centre.y - nsize)
        elif i == 3:
            child_centre = Vec(self.centre.x + nsize, self.centre.y + nsize)
            
        return child_centre, child_size
            
    def in_square(self, p):
        """Determines if p is in square with centre centre and size size
        """
        top = self.centre.y + self.size / 2
        bottom = self.centre.y - self.size / 2
        left = self.centre.x - self.size / 2
        right = self.centre.x + self.size / 2
        if p.x >= left and p.x < right and p.y >= bottom and p.y < top:
            return True
        else:
            return False

    def plot(self, axes):
        """Plot the dividing axes of this node and
           (recursively) all children"""
        if self.is_leaf:
            axes.plot([p.x for p in self.points], [p.y for p in self.points], 'bo')
        else:
            axes.plot([self.centre.x - self.size / 2, self.centre.x + self.size / 2],
                      [self.centre.y, self.centre.y], '-', color='gray')
            axes.plot([self.centre.x, self.centre.x],
                      [self.centre.y - self.size / 2, self.centre.y + self.size / 2],
                      '-', color='gray')
            for child in self.children:
                child.plot(axes)
        axes.set_aspect(1)
                
    def __repr__(self, depth=0):
        """String representation with children indented"""
        indent = 2 * self.depth * ' '
        if self.is_leaf:
            return indent + "Leaf({}, {}, {})".format(self.centre, self.size, self.points)
        else:
            s = indent + "Node({}, {}, [\n".format(self.centre, self.size)
            for child in self.children:
                s += child.__repr__(depth + 1) + ',\n'
            s += indent + '])'
            return s
        
