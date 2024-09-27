class ShapeFunction1D:
    def __init__(self, degree):
        self.degree = degree

    def shape(self, x):
        N = [0]*2
        if self.degree == 1:
            N[0] = 1 - x
            N[1] = x
        elif self.degree == 2:
            N = [0]*3
            N[0] = (1 - x)**2
            N[1] = 2*x*(1 - x)
            N[2] = x**2
        # Agrega aquí otros grados...
        return N
    
    def shape_dx(self, x):
        N = [0]*2
        if self.degree == 1:
            N[0] = -1
            N[1] = 1
        elif self.degree == 2:
            N = [0]*3
            N[0] = -2*(1 - x)
            N[1] = 2*(1 - 2*x)
            N[2] = 2*x
        # Agrega aquí otros grados...
        return N
    


class ShapeFunction2D:
    def __init__(self, degree):
        self.degree = degree

    def shape(self, x, y):
        N = [0]*3
        if self.degree == 1:
            N[0] = 1 - x - y
            N[1] = x
            N[2] = y
        elif self.degree == 2:
            N = [0]*4
            N[0] = (1 - x)*(1 - y)
            N[1] = x*(1 - y)
            N[2] = x*y
            N[3] = (1 - x)*y
        # Agrega aquí otros grados...
        return N
    
    def shape_dx(self, x, y):
        N = [0]*3
        if self.degree == 1:
            N[0] = -1
            N[1] = 1
            N[2] = 0
        elif self.degree == 2:
            N = [0]*4
            N[0] = -1 + y
            N[1] = 1 - y
            N[2] = y
            N[3] = -y
        # Agrega aquí otros grados...
        return N

    def shape_dy(self, x, y):
        N = [0]*3
        if self.degree == 1:
            N[0] = -1
            N[1] = 0
            N[2] = 1
        elif self.degree == 2:
            N = [0]*4
            N[0] = -1 + x
            N[1] = -x
            N[2] = x
            N[3] = 1 - x
        # Agrega aquí otros grados...
        return N

class ShapeFunction3D:
    def __init__(self, degree):
        self.degree = degree

    def shape(self, x, y, z):
        N = [0]*4
        if self.degree == 1:
            N[0] = 1 - x - y - z
            N[1] = x
            N[2] = y
            N[3] = z
        elif self.degree == 2:
            N = [0]*10
            N[0] = x*(2*x - 1)
            N[1] = y*(2*y - 1)
            N[2] = z*(2*z - 1)
            N[3] = 4*x*y
            N[4] = 4*y*z
            N[5] = 4*x*z
            N[6] = 1 - x - y - z
            N[7] = 4*y*(1 - x - y - z)
            N[8] = 4*z*(1 - x - y - z)
            N[9] = 4*x*(1 - x - y - z)
        
        return N
    
    def shape_dx(self, x, y, z):
        N = [0]*4
        if self.degree == 1:
            N[0] = -1
            N[1] = 1
            N[2] = 0
            N[3] = 0
        elif self.degree == 2:
            N = [0]*10
            N[0] = 4*x - 1
            N[1] = 0
            N[2] = 0
            N[3] = 4*y
            N[4] = 0
            N[5] = 4*z
            N[6] = -4*y - 4*z
            N[7] = -4*y
            N[8] = -4*z
            N[9] = 4*(1 - y - z)
        # Agrega aquí otros grados...
        return N

    def shape_dy(self, x, y, z):
        N = [0]*4
        if self.degree == 1:
            N[0] = -1
            N[1] = 0
            N[2] = 1
            N[3] = 0
        elif self.degree == 2:
            N = [0]*10
            N[0] = 0
            N[1] = 4*y - 1
            N[2] = 0
            N[3] = 4*x
            N[4] = 4*z
            N[5] = 0
            N[6] = -4*x - 4*z
            N[7] = 4*x
            N[8] = -4*z
            N[9] = -4*x
        # Agrega aquí otros grados...
        return N

    def shape_dz(self, x, y, z):
        N = [0]*4
        if self.degree == 1:
            N[0] = -1
            N[1] = 0
            N[2] = 0
            N[3] = 1
        elif self.degree == 2:
            N = [0]*10
            N[0] = 0
            N[1] = 0
            N[2] = 4*z - 1
            N[3] = 0
            N[4] = 4*y
            N[5] = 4*x
            N[6] = -4*x - 4*y
            N[7] = -4*y
            N[8] = 4*x
            N[9] = -4*x
        # Agrega aquí otros grados...
        return N