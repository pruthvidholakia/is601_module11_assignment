from datetime import datetime
from typing import List, Optional, Literal
from uuid import UUID
from pydantic import BaseModel, Field


class CalculationBase(BaseModel):
    type: Literal['addition', 'subtraction', 'multiplication', 'division']
    inputs: List[float]
    user_id: UUID


class CalculationCreate(CalculationBase):
    pass


class CalculationUpdate(BaseModel):
    inputs: Optional[List[float]] = None


class CalculationInDBBase(CalculationBase):
    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class CalculationResponse(CalculationInDBBase):
    result: float = Field(..., description="Result of the calculation")
