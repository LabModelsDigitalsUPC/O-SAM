from pydantic import BaseModel
from typing import Optional, List
from uuid import uuid4, UUID

from .mesh  import Mesh
from .spatial_entities import Plane
from .spatial_operations import Translation, Rotation
from .reference_systems import ReferenceSystem3D
from .sets import *
from ..sections.section import Section


class Object(BaseModel):
    id: UUID
    name: Optional[str] = None
    mesh: Mesh = Mesh()
    nsets: List[NSet] = []
    elsets: List[ElSet] =[]
    coordinateSystem: ReferenceSystem3D = ReferenceSystem3D()

    def set_name(self, name:str):
        self.name =  name
    
    def set_mesh(self, mesh: Mesh):
        self.mesh = mesh
    
    def set_system(self, system: ReferenceSystem3D):
        self.coordinateSystem = system
    
    def add_nset_from_list(self, name:str, ids:Set[int]):
        #IF NSET NAME ALREADY IN THE SET AVOID ADDITION
        nset =  next((ns for ns in self.nsets if ns.name == name), None)
        if not nset:
            nset = NSet(name=name)
            nset.set_nodes(ids)
            self.nsets.append(nset)
        else: raise ValueError(f"nset with name'{nset} already exists'")

    def update_nset_from_list(self, name:str,ids:Set[int]):
        #IF NSET NAME NOT IN SET CREATE NSET
        nset =  next((ns for ns in self.nsets if ns.name == name), None)
        if nset: nset.nodes.update(ids)
        else:  self.add_nset_from_list(name, ids)

    def add_elset_from_list(self, name:str, ids:List[int]):
        elset =  next((els for els in self.elsets if els.name == name), None)
        if  not elset:
            elset = ElSet(name=name)
            elset.set_elements(ids)
            self.elsets.append(elset)
        else: raise ValueError(f"nset with name'{elset} already exists'")

    def update_elset_from_list(self, name:str, ids:List[int]):
            #IF NSET NAME NOT IN SET CREATE NSET
            elset =  next((els for els in self.elsets if els.name == name), None)
            if elset: elset.elements.update(ids)
            else:  self.add_elset_from_list(name, ids)

    def get_name(self):
        return self.name
    
    def get_elements(self):
        return self.mesh.elements.copy()
    
    def get_element_by_id(self, id:int):
        return self.mesh.get_element_by_id(id)
    
    def get_nodes(self):
        return self.mesh.nodes.copy()
    
    def get_node_by_id(self, id:int):
        return self.mesh.get_node_by_id(id)

    def get_nsets(self)->List[NSet]:
        return self.nsets
    
    def get_nset_names(self)->List[str]:
        return [nset.name for nset in self.nsets]

    def get_nset_nodes(self, name:str):
        #check if nset is in object's nsets
        nset= next((nset for nset in self.nsets if nset.name == name), None)
        if nset: 
            #return the node set
            return nset.nodes
        else: raise ValueError(f"Nset with name '{name}' does not exist.")
    
    def get_elsets(self)->List[ElSet]:
        return self.elsets

    def get_elset(self, name:str):
        #check if nset is in object's nsets
        elset= next(elset for elset in self.elsets if elset.name == name)
        if elset: 
            #return the element set
            return elset.elements
        else: raise ValueError(f"Elset with name '{name}' does not exist.")

    def get_elset_nodes(self, name:str):
        elset= next(elset for elset in self.elsets if elset.name == name)
        if  elset:
            nodes = set()
            for el_id in elset.elements:
                element = self.get_element_by_id(el_id)
                nodes.update(element.get_node_ids())
            return nodes
        else: raise ValueError(f"Elset with name '{name}' does not exists.")

    def get_id(self)->UUID:
        return self.id

class Instance(BaseModel):
    id: UUID
    name: str
    referenced_object: UUID
    nsets: List[str] = []
    elsets: List[str] = []
    translation: Optional[Translation]
    rotation: Optional[Rotation]


    def  set_referenced_object(self, object_id:  UUID):
        self.referenced_object = object_id
    
    def get_referenced_object(self)->UUID:
        return self.referenced_object
    
    def get_name(self):
        return self.name
    
    def add_nset(self, nset:str):
        self.nsets.append(nset)
    
    def add_elset(self, elset:str):
        self.elsets.append(elset)
    

class Assembly(BaseModel):
    name: str = 'assembly-default'
    instances: List[Instance] = []

    def add_instance(self, instance:Instance):
        self.instances.append(instance)
    
    def set_name(self, name:str):
        self.name = name
    
    def get_instances(self):
        return self.instances
    
    def get_name(self)-> str:
        return self.name
    
    def get_instance_by_name(self,  name:str):
        return next(inst for inst in self.instances if inst.name == name)
    
    def get_instance_by_id(self,  id:UUID):
        return next(inst for inst in self.instances if inst.id == id)
