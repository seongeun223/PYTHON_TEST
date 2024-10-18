import schemas
from fastapi import HTTPException

def calculate(calculator:schemas.CalculationRequest):
    
    match calculator.operator:
        case '+':
            return calculator.num1 + calculator.num2
        case '-':
            return calculator.num1 - calculator.num2
        case '*':
            return calculator.num1 * calculator.num2
        case '/':
            if calculator.num2 == 0:
                raise HTTPException(status_code=400, detail="Cannot divide by zero")
            
            quotient = calculator.num1 / calculator.num2
            remainder = calculator.num1 % calculator.num2
            
            return f"{quotient} (나머지 : {remainder})"
        case _:
            raise HTTPException(status_code=400, detail="Invalid operator")
        
    