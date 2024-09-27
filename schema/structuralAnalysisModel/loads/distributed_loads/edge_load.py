from enum import Enum
import datetime
from typing import Optional, Union, List
from uuid import UUID, uuid4
from pydantic import BaseModel, conint, Field

from .distributed_load import DistributedLoad


class SurfaceBasedEdgeLoadTypeEnum(Enum):
    EDLD = 'EDLD'
    EDNOR = 'EDNOR'
    EDSHR = 'EDSHR'
    EDTRA = 'EDTRA'
    EDMOM = 'EDMOM'
    EDLDNU = 'EDLDNU'
    EDNORNU = 'EDNORNU'
    EDSHRNU = 'EDSHRNU'
    EDTRANU = 'EDTRANU'
    EDMOMNU = 'EDMOMNU'

class ElementBasedEdgeLoadTypeEnum(Enum):
    EDLDn = 'EDLDn'
    EDNORn = 'EDNORn'
    EDSHRn = 'EDSHRn'
    EDTRAn = 'EDTRAn'
    EDMOMn = 'EDMOMn'
    EDLDnNU = 'EDLDnNU'
    EDNORnNU = 'EDNORnNU'
    EDSHRnNU = 'EDSHRnNU'
    EDTRAnNU = 'EDTRAnNU'
    EDMOMnNU = 'EDMOMnNU'
    PX = 'PX'
    PY  = 'PY'
    PZ = 'PZ'
    PXNU = 'PXNU'
    PYNU = 'PYNU'
    PZNU = 'PZNU'
    P1 = 'P1'
    P2 = 'P2'
    P1NU = 'P1NU'
    P2NU = 'P2NU'
    



class SurfaceBasedEdgeLoad(DistributedLoad):
    type: SurfaceBasedEdgeLoadTypeEnum

class ElementBasedEdgeLoad(DistributedLoad):
    type: ElementBasedEdgeLoadTypeEnum