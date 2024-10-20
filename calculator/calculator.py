import schemas
from fastapi import HTTPException


def calculate(calculator: schemas.CalculationRequest):

    match calculator.operator:
        case "+":
            return calculator.num1 + calculator.num2
        case "-":
            return calculator.num1 - calculator.num2
        case "*":
            return calculator.num1 * calculator.num2
        case "/":
            if calculator.num2 == 0:
                raise HTTPException(status_code=400, detail="Cannot divide by zero")

            quotient = calculator.num1 / calculator.num2
            remainder = calculator.num1 % calculator.num2

            return f"{quotient} (나머지 : {remainder})"
        case _:
            raise HTTPException(status_code=400, detail="Invalid operator")


def convert_unit(value: float, from_unit: str, to_unit: str):
    # 길이
    length_conversion = {"m": 1.0, "km": 1000.0, "inch": 0.0254,}

    # 무게
    weight_conversion = {"kg": 1.0, "lb": 0.453592}  # 파운드

    if from_unit in length_conversion and to_unit in length_conversion:
        converted_value = value * (length_conversion[from_unit] / length_conversion[to_unit])
        return f"{converted_value} {to_unit}"

    if from_unit in weight_conversion and to_unit in weight_conversion:
        converted_value = value * (weight_conversion[from_unit] / weight_conversion[to_unit])
        return f"{converted_value} {to_unit}"

    raise HTTPException(status_code=400, detail="Unsupported unit conversion.")
