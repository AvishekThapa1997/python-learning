from typing import Optional
from pydantic import BaseModel, Field

class Employee(BaseModel):
    id: int
    name: str = Field(
        ..., # indicates required field
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Avishek Thapa"
    )
    department:Optional[str] = "General"
    salary:float = Field(
        ...,
        ge=10000,
        le=10000000,
        description="Employee Minimum Wage"
    )
    variable:float = Field(
        ...,
        ge=0,
        le=100,
        description="Employee Variable in CTC"
    )