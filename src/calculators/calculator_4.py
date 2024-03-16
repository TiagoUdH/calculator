from flask import Request as FlaskRequest
from typing import Any, Dict, List, Union

from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4():
    
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.driver_handler = driver_handler
        
    def calculate(self, request: FlaskRequest):
        body = request.json
        input_data = self.__validate_body(body)
        
        mean = self.__proccess_data(input_data)
        
        formatted_response = self.__formatted_response(mean)
        
        return formatted_response       
        
    def __validate_body(self, body: Dict[str, Any]) -> List[Union[int, float]]:      
        if "numbers" not in body or not all(isinstance(num, (int, float)) for num in body["numbers"]):
            raise HttpUnprocessableEntityError("body mal formatado!")
        
        input_data = body["numbers"]
        
        return input_data
        
    def __proccess_data(self, numbers: List[Union[int, float]]) -> float:
        mean = self.driver_handler.mean(numbers)
        
        return mean
    
    def __formatted_response(self, mean: float) -> Dict[str, Dict[str, Union[int, float]]]:
        response = {
            "data": {
                "Calculator": 4,
                "result": round(mean, 2)
            }
        }
        
        return response