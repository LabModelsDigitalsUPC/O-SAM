from enum import Enum
import math
from typing import Optional, Union, List
from uuid import UUID, uuid4
from pydantic import model_validator,Field, model_serializer, model_serializer

from .section import Section, SectionEnum, BeamSection
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
    
class BeamGeneralSection(BeamSection):  #numerical integration over the section is not required
    section: BeamSectionEnum = Field(serialization_alias='beam_section')
    A: float = 0
    I11: float = 0
    I12: float = 0
    I22: float = 0
    J: float = 0
    sectorial_moment: float = 0
    warping_constant: float = 0
    orientation: Vector3D = Field(default_factory=lambda: Vector3D(X=0, Y=0, Z=-1))

    @model_serializer(mode='wrap')
    def serialize_model(self, handler):
        data = handler(self)
        if 'section' in data:
             data['beam_section'] = data.pop('section')

        # Format orientation as a list of 3 coordinates
        if 'orientation' in data:
            orient = data['orientation']
            if isinstance(orient, dict):
                data['orientation'] = [orient.get('X', 0), orient.get('Y', 0), orient.get('Z', 0)]
            elif hasattr(orient, 'get_coordinates'):
                data['orientation'] = orient.get_coordinates()

        # Remove calculated properties as requested
        # For GENERAL section, these are the input parameters, so we keep them in cross_section or as is.
        # Actually, let's keep them if section is GENERAL.
        if self.section != BeamSectionEnum.GENERAL:
            for field in ['A', 'I11', 'I12', 'I22', 'J', 'sectorial_moment', 'warping_constant']:
                if field in data:
                    # Handle ArbitrarySection 'A' collision: if it's a list, keep it (geometry), if number, delete it (Area).
                    if field == 'A' and isinstance(data[field], list):
                        continue
                    del data[field]
        
        # Structure cross_section parameters
        cross_section = {}
        # List of potential geometric parameters appearing in various subclasses
        geom_params = ['l', 'h', 'b1', 'b2', 't1', 't2', 't3', 't4', 'r', 'a', 'b', 'c', 'd', 't', 'circ_r', 'n']
        
        if self.section == BeamSectionEnum.GENERAL:
             geom_params.extend(['A', 'I11', 'I12', 'I22', 'J'])

        # 'A' and 'B' for ArbitrarySection
        if 'A' in data and isinstance(data['A'], list): 
             geom_params.append('A')
        if 'B' in data: geom_params.append('B')
        
        keys_to_move = []
        for k, v in data.items():
            if k in geom_params:
                cross_section[k] = v
                keys_to_move.append(k)
        
        for k in keys_to_move:
            del data[k]
        
        if cross_section:
            data['cross_section'] = cross_section

        return data

class BeamBoxSection(BeamGeneralSection):
    section: BeamSectionEnum = Field(BeamSectionEnum.BOX, serialization_alias='beam_section')
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
    
    @model_validator(mode='after')
    def calculate_geometrical_constants(self):
        self.calculate_A()
        self.calculate_I()
        self.calculate_J()
        self.calculate_sectorial_moment()
        self.calculate_warping_constant()
        return self
    
class CircSection(BeamGeneralSection):
    section: BeamSectionEnum = Field(BeamSectionEnum.CIRC, serialization_alias='beam_section')
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
    section: BeamSectionEnum = Field(BeamSectionEnum.HEX, serialization_alias='beam_section')
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
    section: BeamSectionEnum = Field(BeamSectionEnum.I, serialization_alias='beam_section')
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
    section: BeamSectionEnum = Field(BeamSectionEnum.L, serialization_alias='beam_section')
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
    section: BeamSectionEnum = Field(BeamSectionEnum.PIPE, serialization_alias='beam_section')
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
    section: BeamSectionEnum = Field(BeamSectionEnum.RECT, serialization_alias='beam_section')
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
    section: BeamSectionEnum = Field(BeamSectionEnum.TRAPEZOID, serialization_alias='beam_section')
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
    section: BeamSectionEnum = Field(BeamSectionEnum.ARBITRARY, serialization_alias='beam_section')
    n: int #number of segments
    A: List[List[float]] #coordinates in the local axis of the section of the first point of the segment (x, y)
    B: List[List[float]] #idem for the second point of the segment (x, y)
    t: List[float] #Thickness per segment

    
