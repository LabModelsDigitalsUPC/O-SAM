from enum import Enum
import datetime
from typing import Optional, Union, List
from uuid import UUID, uuid4
from pydantic import BaseModel, conint, Field
from ..schema.structuralAnalysisModel.structuralAnalysisModel import StructuralAnalysisModel
from ..schema.structuralAnalysisResults.structuralAnalysisResults import StructuralAnalysisResult

class StructuralAnalysisEnum(Enum):
    STATIC = 'STATIC'
    DYNAMIC = 'DYNAMIC'


class Simulation(BaseModel):
    id: Optional[UUID] =  Field(uuid4(), alias='_id')
    name: str
    description: str
    type: Optional[StructuralAnalysisEnum]
    created: float
    model: Optional[UUID]
    results: Optional[List[UUID]]




#########


