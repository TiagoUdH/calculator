from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_2 import Calculator2

def calculator_2_factory():
    numpy_handler = NumpyHandler()
    calc = Calculator2(numpy_handler)
    
    return calc