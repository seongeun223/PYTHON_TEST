from pydantic import BaseModel, Field
from typing_extensions import Literal

class CalculationRequest(BaseModel):
    operator: Literal['+', '-', '*', '/'] = Field(..., description="연산자 (+, -, *, /)")
    num1: float = Field(...,)
    num2: float = Field(...,)
    