import schemas

def calculate(calculator:schemas.CalculationRequest) -> float:
    match calculator.operator:
        case '+':
            return calculator.num1 + calculator.num2
        case '-':
            return calculator.num1 - calculator.num2
        case '*':
            return calculator.num1 * calculator.num2
        case '/':
            if calculator.num2 == 0:
                raise