from enum import Enum
import datetime
from typing import Optional, Union, List
from uuid import UUID, uuid4
from pydantic import BaseModel, conint, Field

class LoadTypeEnum(Enum):
    POINT_LOAD = 'POINT_LOAD'
    DISTRIBUTED_LOAD = 'DISTRIBUTED_LOAD'

class LoadCaseTypeEnum(Enum):
    DEAD = 'DEAD'
    LIVE = 'LIVE'
    SEISMIC = 'SEISMIC'
    WIND = 'WIND'
    EARTH_PRESSURE  = 'EARTH_PRESSURE'
    FLUID_PRESSURE = 'FLUID_PRESSURE'
    SNOW = 'SNOW'
    RAIN = 'RAIN'
    PRESTRESSING = 'PRESTRESSING'

class Load(BaseModel):
    id: UUID = uuid4()
    applied_to: UUID|None = None
    type: LoadTypeEnum

    def get_id(self):
        return self.id

class LoadCase(BaseModel):
    type : LoadCaseTypeEnum
    loads: List[Load]
    coeff: List[float] # de la misma longitud que la lista de loads
