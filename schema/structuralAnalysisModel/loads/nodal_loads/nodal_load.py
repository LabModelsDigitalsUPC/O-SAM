from typing import Optional, Union, List

from ..load import Load, LoadTypeEnum

class NodalLoad(Load):
    type: LoadTypeEnum = LoadTypeEnum.POINT_LOAD
    nodes: str
    dof: Optional[int] = None
    v: Optional[float]
