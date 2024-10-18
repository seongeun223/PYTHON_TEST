from pydantic import BaseModel, Field

class CalculationRequest(BaseModel):
    operator: str = Field(..., description="연산자 (+, -, *, /)")
    num1: float = Field(...,)
    num2: float = Field(...,)
    