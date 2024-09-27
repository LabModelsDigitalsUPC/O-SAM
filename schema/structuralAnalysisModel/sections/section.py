from enum import Enum
import datetime
from typing import Optional, Union, Set
from uuid import UUID, uuid4
from pydantic import BaseModel, conint, Field


class SectionEnum(Enum):
    SHELL_SECTION ='SHELL SECTION'
    BEAM_SECTION ='BEAM SECTION'
    SOLID_SECTION =  'SOLID SECTION'

class Section(BaseModel):
    id : UUID 
    name: str = 'section-default'
    section_type: SectionEnum
    material: Optional[str] = None

    def set_material(self, material:str):
        self.material =  material

    def get_material(self):
        return self.material
    
    def get_id(self):
        return self.id
    


class ShellSection(Section):
    section_type: SectionEnum = SectionEnum.SHELL_SECTION
    thickness: Optional[float] = 1
    integration_points: Optional[int] = 1

class SolidSection(Section):
    section_type:SectionEnum = SectionEnum.SOLID_SECTION

    
    