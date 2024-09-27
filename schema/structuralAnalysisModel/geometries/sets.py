from pydantic import BaseModel
from typing import Optional, Set, List
from uuid import uuid4, UUID

from .mesh import Node

class NSet(BaseModel):
    name: str = 'nodeset-default'
    nodes: Set[int] = set() #set of node ids

    def set_nodes(self, nodes:Set[int]):
        self.nodes.update(nodes)
    
    def get_nodes(self):
        return self.nodes

class ElSet(BaseModel):
    name: str = 'elset-default'
    elements: Set[int] = set() #set of elements ids

    def set_elements(self, elements:List[int]):
        self.elements.update(elements)
    
    def get_elements(self)-> Set[int]:
        return self.elements