from abc import ABC, abstractmethod
from typing import List, Union

class DriverHandlerInterface(ABC):
    
    @abstractmethod
    def standard_derivation(self, numbers: List[Union[int, float]]) -> float:
        pass
    
    @abstractmethod
    def variance(self, numbers: List[Union[int, float]]) -> float:
        pass
    
    @abstractmethod
    def mean(self, numbers: List[Union[int, float]]) -> float:
        pass
    