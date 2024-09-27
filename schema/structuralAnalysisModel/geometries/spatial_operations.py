from pydantic import BaseModel

from .spatial_entities import *


class Translation(BaseModel):
    X: float = 0
    Y: float = 0
    Z: float = 0

    def set_from_vector(self, vec:Vector3D):
        self.X = vec.X
        self.Y = vec.Y
        self.Z = vec.Z

class Rotation(BaseModel):
    A: Point3D = Point3D(X=0, Y=0, Z=0)
    B: Point3D = Point3D(X=0, Y=0, Z=1)
    angle: float = 0

