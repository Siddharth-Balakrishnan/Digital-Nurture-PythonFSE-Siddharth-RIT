from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, select, DateTime
from typing import List, Optional
from contextlib import asynccontextmanager
from datetime import datetime
from schemas import (CourseCreate, CourseUpdate, CourseResponse, 
                     StudentCreate, StudentUpdate, StudentResponse, 
                     EnrollmentCreate, EnrollmentUpdate, EnrollmentResponse)

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./coursemanager.db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    code = Column(String(20), unique=True, index=True, nullable=False)
    credits = Column(Integer, nullable=False)
    department_id = Column(Integer, nullable=False)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)
    department_id = Column(Integer, nullable=False)
    enrollment_year = Column(Integer, nullable=False)

class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    enrollment_date = Column(DateTime, default=datetime.utcnow)
    grade = Column(String(2), nullable=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title='Course Management API',
    description='A fully asynchronous REST API for managing college courses and enrollments.',
    version='1.0',
    contact={"name": "Digital Nurture Support", "email": "support@college.edu"},
    lifespan=lifespan
)

async def get_db():
    async with SessionLocal() as session:
        yield session

@app.post(
    '/api/courses/', 
    response_model=CourseResponse, 
    status_code=status.HTTP_201_CREATED, 
    tags=['Courses'],
    summary="Create a new course",
    response_description="The created course object"
)
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    db_course = Course(**course.model_dump())
    db.add(db_course)
    await db.commit()
    await db.refresh(db_course)
    return db_course

@app.get('/api/courses/', response_model=List[CourseResponse], tags=['Courses'])
async def list_courses(skip: int = 0, limit: int = 10, department_id: Optional[int] = None, db: AsyncSession = Depends(get_db)):
    query = select(Course).offset(skip).limit(limit)    
    if department_id is not None:
        query = query.filter(Course.department_id == department_id)
    result = await db.execute(query)
    return result.scalars().all()

@app.get('/api/courses/{course_id}', response_model=CourseResponse, tags=['Courses'])
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).filter(Course.id == course_id))
    course = result.scalar_one_or_none()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.put('/api/courses/{course_id}', response_model=CourseResponse, tags=['Courses'])
async def update_course(course_id: int, course_update: CourseUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).filter(Course.id == course_id))
    course = result.scalar_one_or_none()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
        
    update_data = course_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(course, key, value)
        
    await db.commit()
    await db.refresh(course)
    return course

@app.delete('/api/courses/{course_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Courses'])
async def delete_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).filter(Course.id == course_id))
    course = result.scalar_one_or_none()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
        
    await db.delete(course)
    await db.commit()
    return None

@app.get('/api/courses/{course_id}/students/', response_model=List[StudentResponse], tags=['Courses'])
async def get_enrolled_students(course_id: int, db: AsyncSession = Depends(get_db)):
    query = select(Student).join(Enrollment).filter(Enrollment.course_id == course_id)
    result = await db.execute(query)
    return result.scalars().all()

@app.post('/api/students/', response_model=StudentResponse, status_code=status.HTTP_201_CREATED, tags=['Students'])
async def create_student(student: StudentCreate, db: AsyncSession = Depends(get_db)):
    db_student = Student(**student.model_dump())
    db.add(db_student)
    await db.commit()
    await db.refresh(db_student)
    return db_student

@app.get('/api/students/', response_model=List[StudentResponse], tags=['Students'])
async def list_students(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    query = select(Student).offset(skip).limit(limit)    
    result = await db.execute(query)
    return result.scalars().all()

@app.get('/api/students/{student_id}', response_model=StudentResponse, tags=['Students'])
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Student).filter(Student.id == student_id))
    student = result.scalar_one_or_none()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put('/api/students/{student_id}', response_model=StudentResponse, tags=['Students'])
async def update_student(student_id: int, student_update: StudentUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Student).filter(Student.id == student_id))
    student = result.scalar_one_or_none()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
        
    update_data = student_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(student, key, value)
        
    await db.commit()
    await db.refresh(student)
    return student

@app.delete('/api/students/{student_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Students'])
async def delete_student(student_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Student).filter(Student.id == student_id))
    student = result.scalar_one_or_none()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
        
    await db.delete(student)
    await db.commit()
    return None

def send_confirmation_email(student_email: str):
    print(f'Sending confirmation to {student_email}')

@app.post('/api/enrollments/', response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED, tags=['Enrollments'])
async def create_enrollment(enrollment: EnrollmentCreate, background_tasks: BackgroundTasks, db: AsyncSession = Depends(get_db)):
    db_enrollment = Enrollment(**enrollment.model_dump())
    db.add(db_enrollment)
    await db.commit()
    await db.refresh(db_enrollment)
    
    result = await db.execute(select(Student).filter(Student.id == enrollment.student_id))
    student = result.scalar_one_or_none()
    if student:
        background_tasks.add_task(send_confirmation_email, student.email)
        
    return db_enrollment

@app.get('/api/enrollments/', response_model=List[EnrollmentResponse], tags=['Enrollments'])
async def list_enrollments(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    query = select(Enrollment).offset(skip).limit(limit)    
    result = await db.execute(query)
    return result.scalars().all()

@app.get('/api/enrollments/{enrollment_id}', response_model=EnrollmentResponse, tags=['Enrollments'])
async def get_enrollment(enrollment_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Enrollment).filter(Enrollment.id == enrollment_id))
    enrollment = result.scalar_one_or_none()
    if enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return enrollment

@app.put('/api/enrollments/{enrollment_id}', response_model=EnrollmentResponse, tags=['Enrollments'])
async def update_enrollment(enrollment_id: int, enrollment_update: EnrollmentUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Enrollment).filter(Enrollment.id == enrollment_id))
    enrollment = result.scalar_one_or_none()
    if enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
        
    update_data = enrollment_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(enrollment, key, value)
        
    await db.commit()
    await db.refresh(enrollment)
    return enrollment

@app.delete('/api/enrollments/{enrollment_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Enrollments'])
async def delete_enrollment(enrollment_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Enrollment).filter(Enrollment.id == enrollment_id))
    enrollment = result.scalar_one_or_none()
    if enrollment is None:
        raise HTTPException(status_code=404, detail="Enrollment not found")
        
    await db.delete(enrollment)
    await db.commit()
    return None
