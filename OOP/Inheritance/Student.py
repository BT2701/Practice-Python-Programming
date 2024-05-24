from Person import Person

class Student(Person):
    def __init__(self, name="Duong Thanh Truong", dob='27/01/2003', studentId='',department='' ):
        super().__init__(name, dob)
        self.studentId=studentId
        self.department= department
    
    def getStudentId(self):
        return self.studentId
    
    def setStudentId(self, studentId):
        self.studentId=studentId

    def getDepartment(self):
        return self.department
    
    def setDepartment(self, department):
        self.department=department

    # ghi de phuong thuc
    def printInfor(self):
        super().printInfor()
        print('StdentId: ', self.studentId)
        print('Department: ', self.department)