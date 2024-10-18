from pydantic import BaseModel, Field

class CalculationRequest(BaseModel):
    operator: str = Field(..., description="연산자 (+, -, *, /)")
    num1: float = Field(...,)
    num2: float = Field(...,)
    
class UnitRequest(BaseModel):
    value: float = Field(..., description="변환할 값")
    from_unit: str = Field(..., description="현재 단위")
    to_unit: str = Field(..., description="변환할 목표 단위")