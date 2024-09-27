from enum import Enum
import math
from typing import Optional, Union, List
from uuid import UUID, uuid4
from pydantic import BaseModel, conint, Field

from .section import Section, SectionEnum
from ..materials.material import Material, MaterialTypeEnum
from ..geometries.spatial_entities import Vector3D

ref= [
    'https://abaqus-docs.mit.edu/2017/English/SIMACAEKEYRefMap/simakey-r-beamsection.htm',
    'https://abaqus-docs.mit.edu/2017/English/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm',
    'https://abaqus-docs.mit.edu/2017/English/SIMACAEELMRefMap/simaelm-c-beamcrosssection.htm',
    'https://abaqus-docs.mit.edu/2017/English/SIMACAEELMRefMap/simaelm-c-beamsectionbehavior.htm'
]

class BeamSectionEnum(Enum):
    GENERAL = 'GENERAL'
    NONLINEARGENERAL = 'NON LINEAR GENERAL'
    MESHED =  'MESHED'
    ARBITRARY = 'ARBITRARY'
    BOX = 'BOX'
    CIRC =  'CIRC'
    HEX = 'HEX'
    I ='I'
    L = 'L'
    PIPE ='PIPE'
    RECT ='RECT'
    TRAPEZOID = 'TRAPEZOID'
    
class  BeamSection(Section): #TODO numerical integration over the section is required
    beam_section: BeamSectionEnum
    orientation: Vector3D

class BeamGeneralSection(Section):  #numerical integration over the section is not required
    section_type =  SectionEnum.BEAM_SECTION
    beam_section: BeamSectionEnum
    A: float = 0
    I11: float = 0
    I12: float = 0
    I22: float = 0
    J: float = 0
    sectorial_moment: float
    warping_constant: float
    orientation: Vector3D

    def __init__(self, orientation:Vector3D = Vector3D(X=0,Y=0,Z=-1)):
        self.orientation = orientation

class BeamBoxSection(BeamGeneralSection):
    section = BeamSectionEnum.BOX
    a: float
    b: float
    t1: float
    t2: float
    t3: float
    t4: float

    def calculate_A(self): 
        b1=self.b -self.t2 -self.t3
        a1=self.a -self.t1 -self.t2
        self.A = self.a*self.b-a1*b1
    
    def calculate_I(self): #TODO
        self.I11 = 0
        self.I12 = 0
        self.I22 = 0
    
    def calculate_J(self): #TODO
        self.J = 0

    def calculate_sectorial_moment(self): #TODO
        self.sectorial_moment =0
    
    def calculate_warping_constant(self): #TODO
        self.warping_constant = 0
    
    def calculate_geometrical_constants(self):
        self.calculate_A()
        self.calculate_I()
        self.calculate_J()
        self.calculate_sectorial_moment()
        self.calculate_warping_constant()
    
class CircSection(BeamGeneralSection):
    section = BeamSectionEnum.CIRC
    r:  float

    def calculate_A(self): #TODO
        self.A = math.pi*self.r**2
    
    def calculate_I(self): #TODO
        self.I11 = (math.pi/4)*self.r**4
        self.I12 = 0
        self.I22 = self.I11
    
    def calculate_J(self): #TODO
        self.J = 0

    def calculate_sectorial_moment(self): #TODO
        self.sectorial_moment =0
    
    def calculate_warping_constant(self): #TODO
        self.warping_constant = 0
    
    def calculate_geometrical_constants(self):
        self.calculate_A()
        self.calculate_I()
        self.calculate_J()
        self.calculate_sectorial_moment()
        self.calculate_warping_constant()

class HexSection(BeamGeneralSection):
    section = BeamSectionEnum.HEX
    circ_r: float
    t: float

    def calculate_A(self): 
        circ_r2= self.circ_r-self.t
        ext_A = (3 * math.sqrt(3) / 2) * self.circ_r**2
        int_A = (3 * math.sqrt(3) / 2) * circ_r2**2
        self.A = ext_A  - int_A
    
    def calculate_I(self): #TODO
        self.I11 = 0
        self.I12 = 0
        self.I22 = 0
    
    def calculate_J(self): #TODO
        self.J = 0

    def calculate_sectorial_moment(self): #TODO
        self.sectorial_moment =0
    
    def calculate_warping_constant(self): #TODO
        self.warping_constant = 0
    
    def calculate_geometrical_constants(self):
        self.calculate_A()
        self.calculate_I()
        self.calculate_J()
        self.calculate_sectorial_moment()
        self.calculate_warping_constant()

class ISection(BeamGeneralSection):
    section = BeamSectionEnum.I
    l:Optional[float] = None
    h:float
    b1: float
    b2: float
    t1:float
    t2:float
    t3:float

    def calculate_A(self): #TODO
        self.A = 0
    
    def calculate_I(self): #TODO
        self.I11 = 0
        self.I12 = 0
        self.I22 = 0
    
    def calculate_J(self): #TODO
        self.J = 0

    def calculate_sectorial_moment(self): #TODO
        self.sectorial_moment =0
    
    def calculate_warping_constant(self): #TODO
        self.warping_constant = 0
    
    def calculate_geometrical_constants(self):
        self.calculate_A()
        self.calculate_I()
        self.calculate_J()
        self.calculate_sectorial_moment()
        self.calculate_warping_constant()

class LSection(BeamGeneralSection):
    section = BeamSectionEnum.L
    a: float
    b: float
    t1: float
    t2: float

    def calculate_A(self): #TODO
        self.A = 0
    
    def calculate_I(self): #TODO
        self.I11 = 0
        self.I12 = 0
        self.I22 = 0
    
    def calculate_J(self): #TODO
        self.J = 0

    def calculate_sectorial_moment(self): #TODO
        self.sectorial_moment =0
    
    def calculate_warping_constant(self): #TODO
        self.warping_constant = 0
    
    def calculate_geometrical_constants(self):
        self.calculate_A()
        self.calculate_I()
        self.calculate_J()
        self.calculate_sectorial_moment()
        self.calculate_warping_constant()

class PipeSection(BeamGeneralSection):
    section = BeamSectionEnum.PIPE
    r: float
    t: float

    def calculate_A(self): #TODO
        self.A = 0
    
    def calculate_I(self): #TODO
        self.I11 = 0
        self.I12 = 0
        self.I22 = 0
    
    def calculate_J(self): #TODO
        self.J = 0

    def calculate_sectorial_moment(self): #TODO
        self.sectorial_moment =0
    
    def calculate_warping_constant(self): #TODO
        self.warping_constant = 0
    
    def calculate_geometrical_constants(self):
        self.calculate_A()
        self.calculate_I()
        self.calculate_J()
        self.calculate_sectorial_moment()
        self.calculate_warping_constant()

class RectSection(BeamGeneralSection):
    psection = BeamSectionEnum.RECT
    a: float
    b: float

    def calculate_A(self): #TODO
        self.A = 0
    
    def calculate_I(self): #TODO
        self.I11 = 0
        self.I12 = 0
        self.I22 = 0
    
    def calculate_J(self): #TODO
        self.J = 0

    def calculate_sectorial_moment(self): #TODO
        self.sectorial_moment =0
    
    def calculate_warping_constant(self): #TODO
        self.warping_constant = 0
    
    def calculate_geometrical_constants(self):
        self.calculate_A()
        self.calculate_I()
        self.calculate_J()
        self.calculate_sectorial_moment()
        self.calculate_warping_constant()
    
class TrapezoidSection(BeamGeneralSection):
    section = BeamSectionEnum.TRAPEZOID
    a: float
    b: float
    c: float
    d: float

    def calculate_A(self): #TODO
        self.A = 0
    
    def calculate_I(self): #TODO
        self.I11 = 0
        self.I12 = 0
        self.I22 = 0
    
    def calculate_J(self): #TODO
        self.J = 0

    def calculate_sectorial_moment(self): #TODO
        self.sectorial_moment =0
    
    def calculate_warping_constant(self): #TODO
        self.warping_constant = 0
    
    def calculate_geometrical_constants(self):
        self.calculate_A()
        self.calculate_I()
        self.calculate_J()
        self.calculate_sectorial_moment()
        self.calculate_warping_constant()

class ArbitrarySection(BeamGeneralSection): #Añadir validators
    section = BeamSectionEnum.ARBITRARY
    n: int #number of segments
    A: List[List[float]] #coordinates in the local axis of the section of the first point of the segment (x, y)
    B: List[List[float]] #idem for the second point of the segment (x, y)
    t: List[float] #Thickness per segment

    
