from pydantic import BaseModel, Field
from typing import Optional, Set, List
from uuid import uuid4, UUID

from .mesh import Node

class NSet(BaseModel):
    name: str = 'nodeset-default'
    nodeIDs: Set[int] = Field(default_factory=set) #set of node ids

    def set_nodes(self, nodes:Set[int]):
        self.nodeIDs.update(nodes)
    
    def get_nodes(self):
        return self.nodeIDs

class ElSet(BaseModel):
    name: str = 'elset-default'
    elementIDs: Set[int] = Field(default_factory=set) #set of elements ids

    def set_elements(self, elements:List[int]):
        self.elementIDs.update(elements)
    
    def get_elements(self)-> Set[int]:
        return self.elementIDs