from typing import Any, Dict, Union
from flask import Request as FlaskRequest

from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator1:
    
    def calculate(self, request: FlaskRequest) -> Dict[str, Dict[str, Union[int, float]]]:
        body = request.json
        
        input_data = self.__validate_body(body)
        splited_number = input_data / 3
        
        first_process_result = self.__first_process(splited_number)
        second_proccess_result = self.__second_process(splited_number)
        
        calc_result = first_process_result + second_proccess_result + splited_number
        
        response: Dict[str, Dict[str, Union[int, float]]] = self.__format_response(calc_result)
        
        return response
        
    def __validate_body(self, body: Dict[str, Any]) -> Union[int, float]:
        if "number" not in body or not isinstance(body["number"], (int, float)):
            raise HttpUnprocessableEntityError("body mal formatado!")
        
        input_data = body["number"]
        
        return input_data
    
    def __first_process(self, first_number: float) -> float:
        first_part = first_number / 4 + 7
        second_part = first_part ** 2 * 0.257
        
        return second_part
    
    def __second_process(self, second_number: float) -> float:
        first_part = second_number ** 2.121
        second_part = first_part / 5 + 1
        
        return second_part
    
    def __format_response(self, calc_result: float) -> Dict[str, Dict[str, Union[int, float]]]:
        return {
            "data": {
                "Calculator": 1,
                "result": round(calc_result, 2)
            }
        }