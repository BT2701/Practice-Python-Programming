from .Database import *
from .Department import *

class Student(Base):
    __tablename__ = "student"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    department=Column(Integer, nullable=False)

# Tạo bảng trong cơ sở dữ liệu
Base.metadata.create_all(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def create_student(db, name, age,department):
    db_student = Student(name=name, age=age, department=department)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session):
    return db.query(Student).all()