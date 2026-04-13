from enum import Enum
import datetime
from typing import Optional, Union, List
from uuid import UUID, uuid4
from pydantic import BaseModel, conint, Field

class LoadTypeEnum(Enum):
    POINT_LOAD = 'POINT_LOAD'
    DISTRIBUTED_LOAD = 'DISTRIBUTED_LOAD'
    SURFACE_LOAD = 'SURFACE_LOAD'

class LoadCaseTypeEnum(Enum):
    DEAD = 'DEAD'
    DEAD_SW = 'DEAD+SW'
    LIVE = 'LIVE'
    SEISMIC = 'SEISMIC'
    WIND = 'WIND'
    EARTH_PRESSURE  = 'EARTH_PRESSURE'
    FLUID_PRESSURE = 'FLUID_PRESSURE'
    SNOW = 'SNOW'
    RAIN = 'RAIN'
    PRESTRESSING = 'PRESTRESSING'
    NOTDEFINED = "NOTDEFINED"

class LoadCase(BaseModel):
    id: UUID = uuid4()
    name: str
    type : LoadCaseTypeEnum
    selfWeight: List[float]

class LoadType(BaseModel):
    pass

class NodalLoad(LoadType):
    nset: str
    dof: Optional[int] = None
    v: Optional[float]

class Load(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    type: LoadTypeEnum
    caseName: Optional[str] = None
    instances: List[UUID]
    load: Union[NodalLoad, 'DistributedLoad', 'SurfaceLoad']

    def get_id(self):
        return self.id


class SurfaceLoadTypeEnum(Enum):
    TRVECn = 'TRVECn'
    TRVEC = 'TRVEC'
    TRSHRn = 'TRSHRn'
    TRSHR = 'TRSHR'
    TRVECnNU = 'TRVECnNU'
    TRVECNU = 'TRVECNU'
    TRSHRnNU = 'TRSHRnNU'
    TRSHRNU = 'TRSHRNU'
    Pn = 'Pn'
    P = 'P'
    PnNU = 'PnNU'
    PNU = 'PNU'
    HPn = 'HPn'
    HP = 'HP'
    VPn = 'VPn'
    VP = 'VP'
    SPn = 'SPn'
    SP = 'SP'
    PORMECHn = 'PORMECHn'
    PORMECH  = 'PORMECH'
    HPI = 'HPI'
    HPE = 'HPE'
    PI = 'PI'
    PE  = 'PE'
    PINU = 'PINU'
    PENU = 'PENU'

class DistributedLoad(LoadType):
    elset: str
    dir: str
    v1: float
    v2: float
    x1: float
    x2: float

class SurfaceLoad(LoadType):
    type: Optional[SurfaceLoadTypeEnum] = SurfaceLoadTypeEnum.P
    elset: str
    v: float
    xdir: float
    ydir: float
    zdir: float
