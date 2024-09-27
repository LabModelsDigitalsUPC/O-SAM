from enum import Enum
import datetime
from typing import Optional, Union, List
from uuid import UUID, uuid4
from pydantic import BaseModel, conint, Field

from .distributed_load import DistributedLoad


class BodyLoadTypeEnum(Enum):
    BX = 'BX'
    BY = 'BY'
    BZ = 'BZ'
    BXNU = 'BXNU'
    BYNU ='BYNU'
    BZNU =  'BZNU'
    BR ='BR'
    BRNU = 'BRNU'
    VBF = 'VBF'
    SBF = 'SBF'
    GRAV = 'GRAV'
    CENT = 'CENT'
    CENTRIF = 'CENTRIF'
    CORIO = 'CORIO'
    ROTA =  'ROTA'
    ROTDYNF =  'ROTODYNF'
    PDBF =  'PDBF'

class BodyLoad(DistributedLoad):
    type: BodyLoadTypeEnum 