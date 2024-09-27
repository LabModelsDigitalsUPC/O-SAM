import json
from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

from .materials.material import Material
from .sections.section import Section
from .loads.load import Load
from .geometries.assembly import Object, Assembly
from .geometries.sets import NSet, ElSet
from .sections.section import Section
from .boundary_conditions import BoundaryCondition


class StructuralAnalysisModel(BaseModel):
    id:Optional[UUID ] =  Field(uuid4(), alias='_id')
    name:  str = 'default-SA-name'
    objects: List[Object] = []
    assembly: Assembly = Assembly()
    materials: List[Material] =  []
    sections: List[Section] =  []
    bc: List[BoundaryCondition] =  []
    loads: List[Load] = []

    def __init__(self, id = None):
        super().__init__()
        self.id = id

    def add_object(self, obj:Object):
        self.objects.append(obj)

    def add_material(self, mat:Material):
        self.materials.append(mat)

    def add_section(self, sec:Section):
        self.sections.append(sec)

    def add_bc(self, bc:BoundaryCondition):
        self.bc.append(bc)

    def add_load(self, load:Load):
        self.loads.append(load)

    def add_set(self, _set: NSet|ElSet):
        self.sets.append(_set)

    def get_object_by_name(self, name: str)->Object:
        return next(obj for obj in self.objects if obj.name == name)

    def get_object_by_id(self, id: UUID)->Object:
        return next(obj for obj in self.objects if obj.id == id)
    
    def get_objects(self)->List[Object]:
        return self.objects
    
    def get_nsets(self)-> List[NSet]:
        nsets=[]
        for obj in self.objects:
            nsets+=obj.get_nsets() 
        return nsets 

    def get_nset_names(self)-> List[str]:
        nsets:List[str]=[]
        for obj in self.objects:
            nsets+=obj.get_nset_names() 
        return nsets 

    def get_elset(self, name:str)->List[ElSet]:
        elsets=[]
        for obj in self.objects:
            elsets+=obj.get_elsets()
        return elsets

    def save(self, path):
        with open(path, 'w') as f:
            f.write(self.json(indent=None))

