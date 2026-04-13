from enum import Enum
import datetime
from typing import Optional, Union, Set, Any, Dict
from uuid import UUID, uuid4
from pydantic import BaseModel, conint, Field


class SectionEnum(str, Enum):
    SHELL_SECTION = "SHELL SECTION"
    BEAM_SECTION = "BEAM SECTION"
    BEAM_GENERAL_SECTION = "BEAM GENERAL SECTION"
    SOLID_SECTION = "SOLID SECTION"


# Base for SectionType
class SectionType(BaseModel):
    pass


class ShellSection(SectionType):
    thickness: float

class SolidSection(SectionType):
    # You can extend later with real fields
    pass


class BeamSection(SectionType):
    # Extend later (like profile, dimensions, etc.)
    pass


# In the Section model, declare section as a union of possible types
class Section(BaseModel):
    id: UUID
    name: str
    section_type: SectionEnum
    material: Optional[str] = Field(default=None, exclude=True)
    section: Any 
    raw_section_dict: Optional[Dict] = Field(default=None, exclude=True)
   

    def set_material(self, material: str):
        self.material = material

    def get_material(self):
        return self.material

    def get_id(self):
        return self.id