from .DatabaseHOF import *

class Student(Base):
    __tablename__ = "student"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    department=Column(Integer, nullable=False)
    math=Column(Integer, nullable=True)
    english=Column(Integer, nullable=True)
    it=Column(Integer, nullable=True)

# Tạo bảng trong cơ sở dữ liệu
Base.metadata.create_all(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def create_student(db, name, age,department, math, english, it):
    db_student = Student(name=name, age=age, department=department, math=math, english=english, it=it)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session):
    return db.query(Student).all()

def get_math_score_by_id(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        return student.math
    else:
        return None