from typing import Optional, Union, List
from pydantic import BaseModel

from ..elements.element import Element
from .spatial_entities import  Point3D

class Node(Point3D):
    id: int

    def set_id(self, id:int):
        self.id = id

class Mesh(BaseModel):
    nodes: List[Node] = []
    elements: List[Element] = []
    node_count: int = 0
    el_count: int = 0
    
    def add_node_from_coords(self, id, x, y, z):
        if not id: id = self.node_count + 1
        self.nodes.append(Node(id=id, X=x, Y=y, Z=z))
        self.node_count+=1

    def add_node(self, node:Node):
        self.nodes.append(node)
        self.node_count+=1

    def add_element(self, element: Element):
        self.elements.append(element)
        self.el_count+=1

    def get_node_by_id(self,id:int):
        node= next((node for node in self.nodes if node.id == id), None)
        if node: return node
        else: raise ValueError(f"Node with id '{id}' is not defined")
    
    def get_element_by_id(self, id:int):
        element = next((element for element in self.elements if element.get_id() == id), None)
        if element: return element
        else: raise ValueError(f"Element with id '{id}' is not defined")

