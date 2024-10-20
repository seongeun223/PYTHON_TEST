from fastapi import FastAPI
import schemas, calculator

app = FastAPI()

calculation_history = []

@app.post('/calculates')
async def test_calculation(request:schemas.CalculationRequest):
    
    result = calculator.calculate(request)
    
    calculation_record = {
        "operator": request.operator,
        "num1": request.num1,
        "num2": request.num2,
        "result": result
    }
    calculation_history.append(calculation_record)
    
    return {result, calculation_history}

@app.post('/calculates/convert')
async def convert_unit(request: schemas.UnitRequest):
    result = calculator.convert_unit(request.value, request.from_unit, request.to_unit)
    
    conversion_record = {
        "value": request.value,
        "from_unit": request.from_unit,
        "to_unit": request.to_unit,
        "converted_value": result
    }
    calculation_history.append(conversion_record)
    
    return result

@app.get('/calculates/history')
async def get_calculation_history():
    return calculation_history