from pydantic import BaseModel
from .spatial_entities import Vector3D

class ReferenceSystem3D(BaseModel):
    xAxis: Vector3D = Vector3D(X=1,Y=0,Z=0)
    yAxis: Vector3D = Vector3D(X=0,Y=1,Z=0)
    zAxis: Vector3D = Vector3D(X=0,Y=0,Z=1)