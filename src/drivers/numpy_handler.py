import numpy
from typing import List, Union
from .interfaces.driver_handler_interface import DriverHandlerInterface

class NumpyHandler(DriverHandlerInterface):
    
    def __init__(self) -> None:
        self.__np = numpy
        
    def standard_derivation(self, numbers: List[Union[int, float]]) -> float:
        return self.__np.std(numbers)
    
    def variance(self, numbers: List[Union[int, float]]) -> float:
        return self.__np.var(numbers)
    
    def mean(self, numbers: List[Union[int, float]]) -> float:
        return self.__np.mean(numbers)