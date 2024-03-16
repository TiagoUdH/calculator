from typing import Dict, List
from pytest import raises

from .calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class MockRequest:
    
    def __init__(self, body: Dict[str, List[float]]) -> None:
        self.json = body

class MockDriverHandler:
    
    def mean(self, numbers: List[float]) -> float:
        return 201.0
        
def test_calculate():
    mock_request = MockRequest({ "numbers": [1, 1, 1, 1, 1001] })
    
    calculator_4 = Calculator4(MockDriverHandler())
    
    response = calculator_4.calculate(mock_request)
    
    assert response == {'data': {'Calculator': 4, 'result': 201.0}}
    
def test_calculate_integration():
    mock_request = MockRequest(body={ "numbers": [1, 1, 1, 1, 1001] })
    
    driver = NumpyHandler()
    calculator_4 = Calculator4(driver)
    
    formated_response = calculator_4.calculate(mock_request)
    
    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 4, 'result': 201.0}}
    
def test_calculate_with_body_error():
    mock_request = MockRequest(body={ "something": 1 })
    
    driver = MockDriverHandler()
    calculator_4 = Calculator4(driver)
    
    with raises(HttpUnprocessableEntityError) as exc_info:
        calculator_4.calculate(mock_request)
    
    assert isinstance(exc_info.value, HttpUnprocessableEntityError)
    assert str(exc_info.value) == "body mal formatado!"
