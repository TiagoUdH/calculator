from typing import Dict, List
from pytest import raises

from .calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class MockRequest:
    
    def __init__(self, body: Dict[str, List[float]]) -> None:
        self.json = body

class MockDriverHandler:
    
    def variance(self, numbers: List[float]) -> float:
        return 1000000

class MockDriverHandlerError:
    
    def variance(self, numbers: List[float]) -> float:
        return 3
        
def test_calculate():
    mock_request = MockRequest({ "numbers": [1, 1, 1, 1, 100] })
    
    calculator_3 = Calculator3(MockDriverHandler())
    
    response = calculator_3.calculate(mock_request)
    
    assert response == {'data': {'Calculator': 3, 'value': 1000000, 'Success': True}}
    
def test_calculate_integration():
    mock_request = MockRequest(body={ "numbers": [1, 1, 1, 1, 1000] })
    
    driver = NumpyHandler()
    calculator_3 = Calculator3(driver)
    
    formated_response = calculator_3.calculate(mock_request)
    
    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 3, 'value': 159680.16000000003, 'Success': True}}

def test_calculate_with_variance_error():
    mock_request = MockRequest({ "numbers": [1, 2, 3, 4, 5] })
    
    calculator_3 = Calculator3(MockDriverHandlerError())
    
    with raises(HttpBadRequestError) as exc_info:
        calculator_3.calculate(mock_request)
        
    assert isinstance(exc_info.value, HttpBadRequestError)
    assert str(exc_info.value) == 'Falha no processo: Variância menor que multiplicação'
    
def test_calculate_with_body_error():
    mock_request = MockRequest(body={ "something": 1 })
    
    driver = MockDriverHandler()
    calculator_3 = Calculator3(driver)
    
    with raises(HttpUnprocessableEntityError) as exc_info:
        calculator_3.calculate(mock_request)
    
    assert isinstance(exc_info.value, HttpUnprocessableEntityError)
    assert str(exc_info.value) == "body mal formatado!"
