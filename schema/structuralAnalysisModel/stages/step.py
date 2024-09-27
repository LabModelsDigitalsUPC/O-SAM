from enum import Enum
import datetime
from typing import Optional, Union, Set
from uuid import UUID, uuid4
from pydantic import BaseModel, conint, Field, validator

from ..boundary_conditions import BoundaryCondition
from ..loads.load import Load

class MethodEnum(Enum):
    RIKS =  'RIKS'
    GENERAL =  'GENERAL'

class StaticAnalysis(BaseModel):
    method:  Optional[MethodEnum] = None

class GeneralStaticAnalysis(StaticAnalysis):
    method = MethodEnum.GENERAL
    init_time_increment: Optional[float]
    time_period: Optional[float]
    min_time_increment: Optional[float]
    max_time_increment: Optional[float]
    

class RiksStaticAnalysis(StaticAnalysis):
    method = MethodEnum.RIKS
    init_alen_increment: Optional[float] = None#arch length
    total_alen_scalefactor:  Optional[float]  = 1
    min_alen_increment: Optional[float] = total_alen_scalefactor*10^-9#arch  length
    max_alen_increment: Optional[float] = None #arch length
    max_load_prop: Optional[float]  =  None
    control_node: Optional[int] = None
    control_dof: Optional[int] = None
    threshold: Optional[float] = None


class DynamicAnalysis(BaseModel):
    pass

class AmplitudeEnum(Enum):
    STEP='STEP'
    RAMP ='RAMP'

class Step(BaseModel):
    name: Optional[str] = None
    analysis: Optional[Union[StaticAnalysis, DynamicAnalysis]]=  None
    amplitude: Optional[AmplitudeEnum]=  None
    nlgeom: Optional[bool] =  False
    max_automated_increments: int = 100
    boundary_conditions: Set[UUID] = set()
    loads: Set[UUID] = set()

    def set_analysis(self, analysis: Union[StaticAnalysis, DynamicAnalysis]):
        self.analysis = analysis

