from pydantic import BaseModel

class Point3D(BaseModel):
    X: float
    Y: float
    Z: float

    def set_coordinates(self, x:float, y:float, z:float):
        self.X = x
        self.Y = y
        self.Z = z
    
    def get_coordinates(self):
        return [self.X, self.Y, self.Z]


class Vector3D(BaseModel):
    X: float 
    Y: float 
    Z: float 

    def set_from_coordinates (self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z
    
    def set_from_points (self, pointA: Point3D, pointB: Point3D):
        self.X = pointB.X-pointA.X
        self.Y = pointB.Y-pointA.Y
        self.Z = pointB.Z-pointA.Z
    
    def get_coordinates(self)->list:
        return [self.X, self.Y, self.Z]
    
    def get_magnitude(self)->float:
        return (sum(x**2 for x in self.get_coordinates()))**0.5

    def unitize(self):
        self.X = self.X/self.get_magnitude()
        self.Y = self.Y/self.get_magnitude()
        self.Y = self.Y/self.get_magnitude()

def dot_product(v1: Vector3D, v2: Vector3D)->float:
    result = sum(x*y for x, y in zip(v1.get_coordinates(), v2.get_coordinates()))
    return result

def cross_product(v1:Vector3D, v2:Vector3D)->Vector3D:
    a=v1.get_coordinates()
    b=v2.get_coordinates()
    vector = Vector3D(X=a[1]*b[2] - a[2]*b[1], Y=a[2]*b[0] - a[0]*b[2], Z=a[0]*b[1] - a[1]*b[0])
    return vector

class Plane(BaseModel):
    origin: Point3D
    normal: Vector3D

    def set_from_normal(self, origin: Point3D, normal:  Vector3D):
        self.origin = origin
        self.normal = normal