import schemas
from fastapi import HTTPException

def calculate(calculator:schemas.CalculationRequest):
    
    print('==================================================================start')
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
            return calculator.num1 / calculator.num2
        case _:
            raise HTTPException(status_code=400, detail="Invalid operator")