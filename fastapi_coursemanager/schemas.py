from pydantic import BaseModel
from typing import Optional, List


class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int


class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None


class CourseResponse(CourseCreate):
    id: int

    class Config:
        from_attributes = True  


class DepartmentResponse(BaseModel):
    id: int
    name: str
    head_of_dept: str
    budget: float
    courses: List[CourseResponse] = [] # Nests a list of courses!

    class Config:
        from_attributes = True
