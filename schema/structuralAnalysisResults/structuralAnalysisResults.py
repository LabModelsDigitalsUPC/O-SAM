from enum import Enum
import datetime
from typing import Optional, Union, List
from uuid import UUID, uuid4
from pydantic import BaseModel, conint, Field


class ResultTypeEnum(Enum):
    DISPLACEMENT = 'DISPLACEMENT'
    STRESS = 'STRESS'
    STRAIN = 'STRAIN'
    MOMENT = 'MOMENT'
    SHEAR = 'SHEAR'
    AXIAL = 'AXIAL'

class PositionEnum(Enum):
    NODES = 'NODES'
    GAUSS_POINTS = 'GAUSS_POINTS'

class StructuralAnalysisResult(BaseModel):
    id: Optional[UUID ] =  Field(uuid4(), alias='_id')
    dimension:int
    type: ResultTypeEnum
    simulation_id: UUID
    step: Optional[float]
    position: PositionEnum
    components_name: Optional[List[str]]
    gauss_points: Optional[List[List[float]]]
    values_nodes: Optional[List[List[float]]] # depende  de si  es  en los nodos o en gauss points. si es en nodos un valor por cada componente. Si es en gauss es 1*element*gausspoint
    values_gauss: Optional[List[List[List[float]]]]