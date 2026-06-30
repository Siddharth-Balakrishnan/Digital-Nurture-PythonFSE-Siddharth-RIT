from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, select
from typing import List, Optional
from contextlib import asynccontextmanager

from schemas import CourseCreate, CourseUpdate, CourseResponse

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

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(title='Course Management API', version='1.0', lifespan=lifespan)

async def get_db():
    async with SessionLocal() as session:
        yield session

@app.get('/')
async def root():
    return {'message': 'API running'}

@app.post('/api/courses/', response_model=CourseResponse, status_code=201)
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    db_course = Course(**course.model_dump())
    
    db.add(db_course)
    await db.commit()
    await db.refresh(db_course)
    
    return db_course

@app.get('/api/courses/{course_id}', response_model=CourseResponse)
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).filter(Course.id == course_id))
    course = result.scalar_one_or_none()
    
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.get('/api/courses/', response_model=List[CourseResponse])
async def list_courses(
    skip: int = 0, 
    limit: int = 10, 
    department_id: Optional[int] = None, 
    db: AsyncSession = Depends(get_db)
):
    query = select(Course).offset(skip).limit(limit)    

    if department_id is not None:
        query = query.filter(Course.department_id == department_id)
        
    result = await db.execute(query)
    courses = result.scalars().all()
    
    return courses
