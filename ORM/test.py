from Model.Student import *

# Thêm dữ liệu vào cơ sở dữ liệu
if __name__ == "__main__":
    # Khởi tạo phiên làm việc
    db = session()
    
    # Thêm sinh viên
    create_student(db, name="Alice", age=21, department=1)
    create_student(db, name="Bob", age=22,department=1)
    create_student(db, name="Charlie", age=23,department=1)
    
    # Truy vấn tất cả sinh viên
    students = get_students(db)
    for student in students:
        print(f"{student.name}, {student.age}, {student.department}")
