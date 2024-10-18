from fastapi import FastAPI
import schemas, calculator

app = FastAPI()

@app.post('/calculates')
async def test_calculation(request:schemas.CalculationRequest):
    
    result = calculator.calculate(request)
    
    return result

@app.post('/calculates/convert')
async def convert_unit(request: schemas.UnitRequest):
    result = calculator.convert_unit(request.value, request.from_unit, request.to_unit)
    return result