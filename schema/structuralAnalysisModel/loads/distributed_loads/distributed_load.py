from ..load import Load

ref = 'https://abaqus-docs.mit.edu/2017/English/SIMACAEPRCRefMap/simaprc-c-loaddistributed.htm'

class DistributedLoad(Load):
    el_set: str