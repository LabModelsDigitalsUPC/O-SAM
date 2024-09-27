from enum import Enum
import datetime
from typing import Optional, Union, List, Set
from uuid import UUID, uuid4
from pydantic import BaseModel, conint, Field

from ..geometries.spatial_entities import Point3D, Vector3D


class IntegrationEnum(Enum):
    FULL = 'FULL'
    REDUCED =  'REDUCED'

class ElementEnum(Enum):
    SOLID = 'SOLID'
    SHELL =  'SHELL'
    BEAM =  'BEAM'
    MEMBRANE = 'MEMBRANE'
    TRUSS = 'TRUSS'

class Element(BaseModel):
    id: int = 0
    type: ElementEnum
    dofs: Set[int] = set()
    node_count: int = 0
    face_count: int = 0
    integration: IntegrationEnum = IntegrationEnum.FULL
    nodes: List[int] = []
    faces: List[List[int]] = []
    integration_points: List[Point3D] = []
    section: Optional[UUID] = None

    def set_id(self, id:int):
        self.id = id
    
    def set_nodes(self, nodes: List):
        if len(nodes) == self.node_count:  self.nodes = nodes
        else: raise ValueError(f'this element has {self.node_count}.  {len(nodes)} provided')
    
    def set_faces(self, nodes: List):
        if self.face_count == 1:
            self.faces = [nodes]
        if self.face_count == 4 :
            self.faces = [
                            [nodes[0], nodes[1], nodes[2]],
                            [nodes[0], nodes[1], nodes[3]],
                            [nodes[1], nodes[2], nodes[3]],
                            [nodes[0], nodes[1], nodes[4]]
                        ]
        if self.face_count == 6 :
            self.faces = [
                            [nodes[0], nodes[1], nodes[2], nodes[3]],
                            [nodes[4], nodes[7], nodes[6], nodes[5]],
                            [nodes[0], nodes[4], nodes[5], nodes[1]],
                            [nodes[1], nodes[5], nodes[6], nodes[2]],
                            [nodes[2], nodes[6], nodes[7], nodes[3]],
                            [nodes[3], nodes[7], nodes[4], nodes[0]]
                        ]
            
    def get_id(self)-> int:
        return self.id

    def get_node_ids(self)-> List:
        return self.nodes
    
    def get_type(self)->ElementEnum:
        return self.type
    
    def set_section(self, section_id: UUID):
        self.section = section_id

class Element2D(Element):
    type = ElementEnum.SHELL
    dofs:Set[int] = {1,2,3,4,5,6}

    def S3(self, nodes):
        self.node_count = 3
        self.face_count = 1
        self.integration = IntegrationEnum.FULL
        self.set_nodes(nodes)
        self.set_faces(nodes)
    
    def S3R(self, nodes):
        self.node_count = 3
        self.face_count = 1
        self.integration = IntegrationEnum.FULL
        self.set_nodes(nodes)
        self.set_faces(nodes)
    
    def S4(self, nodes):
        self.node_count = 4
        self.face_count = 1
        self.integration = IntegrationEnum.FULL
        self.set_nodes(nodes)
        self.set_faces(nodes)
    
    def S4R(self, nodes):
        self.node_count = 4
        self.face_count = 1
        self.integration = IntegrationEnum.REDUCED
        self.set_nodes(nodes)
        self.set_faces(nodes)
    
    def S8R(self, nodes):
        self.node_count = 8
        self.face_count = 1
        self.integration = IntegrationEnum.REDUCED
        self.set_nodes(nodes)
        self.set_faces(nodes)
    
class Element3D(Element):
    type = ElementEnum.SOLID
    dofs:Set[int] = {1,2,3}
    
    def C3D4(self, nodes):
        self.node_count = 5
        self.face_count = 4
        self.integration = IntegrationEnum.FULL
        self.set_nodes(nodes)
        self.set_faces(nodes)

    def C3D8(self, nodes):
        self.node_count = 8
        self.face_count = 6
        self.integration = IntegrationEnum.FULL
        self.set_nodes(nodes)
        self.set_faces(nodes)

    def C3D8R(self, nodes):
        self.node_count = 8
        self.face_count = 6
        self.integration = IntegrationEnum.REDUCED
        self.set_nodes(nodes)
        self.set_faces(nodes)
