from enum import Enum
import datetime
from typing import Optional, Union, List, Tuple
from uuid import UUID, uuid4
from pydantic import BaseModel, conint, Field




class BoundaryTypeEnum(Enum):
    DISPLACEMENT = 'DISPLACEMENT'
    FIXED = 'FIXED'
    VELOCITY =  'VELOCITY'


class BoundaryCondition(BaseModel):
    id: UUID = uuid4()
    type: BoundaryTypeEnum = BoundaryTypeEnum.DISPLACEMENT
    nodes: str
    applied_to: UUID|None =  None
    ux: Tuple[bool, float] = (False, 0)
    uy: Tuple[bool, float] = (False, 0)
    uz: Tuple[bool, float] = (False, 0)
    rx: Tuple[bool, float] = (False, 0)
    ry: Tuple[bool, float] = (False, 0)
    rz: Tuple[bool, float] = (False, 0)

    def XSYMM(self):
        self.ux =  (True,0)
        self.yx =  (False,0)
        self.zx =  (False,0)
        self.rx =  (False,0)
        self.ry =  (True,0)
        self.rz =  (True,0)
    
    def YSYMM(self):
        self.ux =  (False,0)
        self.yx =  (True,0)
        self.zx =  (False,0)
        self.rx =  (True,0)
        self.ry =  (False,0)
        self.rz =  (True,0)
    
    def ZSYMM(self):
        self.ux =  (False,0)
        self.yx =  (False,0)
        self.zx =  (True,0)
        self.rx =  (True,0)
        self.ry =  (True,0)
        self.rz =  (False,0)
    
    def ENCASTRE(self):
        self.ux =  (True,0)
        self.yx =  (True,0)
        self.zx =  (True,0)
        self.rx =  (True,0)
        self.ry =  (True,0)
        self.rz =  (True,0)
    
    def PINNED(self):
        self.ux =  (True,0)
        self.yx =  (True,0)
        self.zx =  (True,0)
        self.rx =  (False,0)
        self.ry =  (False,0)
        self.rz =  (False,0)
    
    def XASYMM(self):
        self.ux =  (False,0)
        self.yx =  (True,0)
        self.zx =  (True,0)
        self.rx =  (True,0)
        self.ry =  (False,0)
        self.rz =  (False,0)
    
    def YASYMM(self):
        self.ux =  (True,0)
        self.yx =  (False,0)
        self.zx =  (True,0)
        self.rx =  (False,0)
        self.ry =  (True,0)
        self.rz =  (False,0)

    def ZASYMM(self):
        self.ux =  (True,0)
        self.yx =  (True,0)
        self.zx =  (False,0)
        self.rx =  (False,0)
        self.ry =  (False,0)
        self.rz =  (True,0)

