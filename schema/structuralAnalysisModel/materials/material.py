from enum import Enum
import datetime
from typing import Optional, Union, List
from uuid import UUID, uuid4
from pydantic import BaseModel, conint, Field, validator

class MaterialTypeEnum(Enum):
    ANISOTROPIC = 'ANISOTROPIC'
    #ENGINEERING_CONSTANTS= 'ENGINEERING CONSTANTS'#  ORTHOTROPIC GIVING ERNGINEERING VARIABLES
    ISOTROPIC = 'ISOTROPIC'
    #LAMINA ='LAMINA'#othotropic plane stress
    ORTHOTROPIC = 'ORTHOTROPIC'

class MaterialCategoryEnum(Enum):
    STEEL = 'STEEL'
    CONCRETE = 'CONCRETE'
    WOOD = 'WOOD'
    SOIL = 'SOIL'

class HardeningEnum(Enum):
    ISOTROPIC = 'ISOTROPIC'
    KINEMATIC = 'KINEMATIC'

class Function(BaseModel): #
    parameters: List[str]
    data: List[List[float]]

    @validator('data')
    def check_data(cls, data, values):
        if 'parameters' in values and len(values['parameters']) != len(data[0]):
            raise ValueError('La longitud de los datos debe ser igual a la longitud de los parámetros')
        return data
    
    def __init__(self, parameters:List[str], data:List[List[float]]):
        self.parameters = parameters
        self.data =data


################################################################

class Plasticity(BaseModel): #TODO
    functions: List[Function]
    yield_stress: float 
    plastic_strain: float

class Elasticity(BaseModel):
    behaviour_type: MaterialTypeEnum 
    funtions: Optional[List[Function]] =  None
    plane_stress: bool = False
    plane_strain: bool = False
    compression_factor: float = 1
    D1111: float = 0
    D1122: float = 0
    D2222: float = 0
    D1133: float = 0
    D2233: float = 0
    D3333: float = 0
    D1112: float = 0
    D2212: float = 0
    D3312: float = 0
    D1212: float = 0
    D1113: float = 0
    D2213: float = 0
    D3313: float = 0
    D1213: float = 0
    D1313: float = 0
    D1123: float = 0
    D2223: float = 0
    D3323: float = 0
    D1223: float = 0
    D1323: float = 0
    D2323: float = 0


    def set_from_nested_list(self, matrix, plane_stress=False, plane_strain=False):
        if len(matrix) != 6 or any(len(row) != 6 for row in matrix):
            raise ValueError("La matriz debe ser de tamaño 6x6")
        self.plane_stress=plane_stress
        self.plane_strain=plane_strain
        self.D1111 = matrix[0][0]
        self.D1122 = matrix[0][1]
        self.D2222 = matrix[1][1]
        self.D1133 = matrix[0][2]
        self.D2233 = matrix[1][2]
        self.D3333 = matrix[2][2]
        self.D1112 = matrix[0][3]
        self.D2212 = matrix[1][3]
        self.D3312 = matrix[2][3]
        self.D1212 = matrix[3][3]
        self.D1113 = matrix[0][4]
        self.D2213 = matrix[1][4]
        self.D3313 = matrix[2][4]
        self.D1213 = matrix[3][4]
        self.D1313 = matrix[4][4]
        self.D1123 = matrix[0][5]
        self.D2223 = matrix[1][5]
        self.D3323 = matrix[2][5]
        self.D1223 = matrix[3][5]
        self.D1323 = matrix[4][5]
        self.D2323 = matrix[5][5]

    def set_isotropic(self, E, v, plane_stress =False):

        # Matriz de elasticidad para un material isotrópico
        D = [[1/E, -v/E, -v/E, 0, 0, 0],
        [-v/E, 1/E, -v/E, 0, 0, 0],
        [-v/E, -v/E, 1/E, 0, 0, 0],
        [0, 0, 0, 1/(2*(1+v)), 0, 0],
        [0, 0, 0, 0, 1/(2*(1+v)), 0],
        [0, 0, 0, 0, 0, 1/(2*(1+v))]]

        self.set_from_nested_list(D, plane_stress)

    def set_orthotropic(self, E1, E2, E3, v12, v13, v23, G12, G13, G23 ):

        v21 = v12 * E2 / E1
        v31 = v13 * E3 / E1
        v32 = v23 * E3 / E2

        D = [[1/E1, -v12/E1, -v13/E1, 0, 0, 0],
            [-v21/E2, 1/E2, -v23/E2, 0, 0, 0],
            [-v31/E3, -v32/E3, 1/E3, 0, 0, 0],
            [0, 0, 0, 1/G12, 0, 0],
            [0, 0, 0, 0, 1/G13, 0],
            [0, 0, 0, 0, 0, 1/G23]]
        
        self.set_from_nested_list(D)
    
    def get_matrix(self):
        if self.plane_stress or self.plane_strain:
            D=[[self.D1111, self.D1122, self.D1112],
                [self.D1122, self.D2222, self.D2212],
                [self.D1112, self.D2212, self.D1212]]
        else:
            D=[[self.D1111, self.D1122, self.D1133, self.D1112, self.D1113, self.D1123],
                [self.D1122, self.D2222, self.D2233, self.D2212, self.D2213, self.D2223],
                [self.D1133, self.D2233, self.D3333, self.D3312, self.D3313, self.D3323],
                [self.D1112, self.D2212, self.D3312, self.D1212, self.D1213, self.D1223],
                [self.D1113, self.D2213, self.D3313, self.D1213, self.D1313, self.D1323],
                [self.D1123, self.D2223, self.D3323, self.D1223, self.D1323, self.D2323]]
        
        return D

################################################################

class Material(BaseModel):
    name: str = 'material-default'
    category: Optional[MaterialCategoryEnum]= None
    mass_density: float =  0
    elastic: Optional[Elasticity] = None
    plastic: Optional[Plasticity] = None

    def set_elastic_properties(self, material_type:MaterialTypeEnum , material_properties:List):
        
        if material_type.value == 'ISOTROPIC':
            assert  len(material_properties) == 2
            e:Elasticity=Elasticity(behaviour_type=material_type)
            e.set_isotropic(E=material_properties[0],v=material_properties[1])
            self.elastic = e
        elif material_type  == 'ORTHOTROPIC':
            if isinstance(material_properties, float):
                
                assert  len(material_properties) == 9
                
                e:Elasticity=Elasticity(behaviour_type=material_type)
                e.set_orthotropic(
                    E1 =  material_properties[0],
                    E2 =  material_properties[1],
                    E3 =  material_properties[2],
                    v12 = material_properties[3],
                    v13= material_properties[4],
                    v23=material_properties[5],
                    G12=material_properties[6],
                    G13=material_properties[7],
                    G23=material_properties[8]
                    )
                
                self.elastic = e
            
            else:
                
                assert len(material_properties) == 6, "La matriz debe tener 6 filas"
                
                for row in material_properties:
                    assert isinstance(row,List)
                    assert len(row) == 6, "Cada fila de la matriz debe tener 6 elementos"
                
                e:Elasticity =  Elasticity(behaviour_type=material_type)
                e.set_from_nested_list(material_properties)
        else:
            
            assert len(material_properties) == 6, "La matriz debe tener 6 filas"
            
            for row in material_properties:
                assert isinstance(row,List)
                assert len(row) == 6, "Cada fila de la matriz debe tener 6 elementos"

            e:Elasticity=Elasticity(behaviour_type=MaterialTypeEnum.ANISOTROPIC)
            e.set_from_nested_list(material_properties)
            
            self.elastic=e




