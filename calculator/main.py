from fastapi import FastAPI
import schemas, calculator

app = FastAPI()

@app.post('/calculates')
async def test_calculation(request:schemas.CalculationRequest):
    
    result = calculator.calculate(request)
    
    return result
