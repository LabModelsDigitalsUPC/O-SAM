from enum import Enum
import datetime
from typing import Optional, Union, List
from uuid import UUID, uuid4
from pydantic import BaseModel, conint, Field

from .distributed_load import DistributedLoad


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

class SurfaceLoad(DistributedLoad):
    type: SurfaceLoadTypeEnum
    amplitude: list[float]


