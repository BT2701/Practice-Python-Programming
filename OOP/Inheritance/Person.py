class Person:
    def __init__(self, name="Duong Thanh Truong", dob='27/01/2003'):
        self.name= name
        self.dob=dob
    
    def setName(self, name):
        self.name=name

    def setDob(self, dob):
        self.dob=dob

    def getName(self):
        return self.name
    
    def getDob(self):
        return self.dob
    
    def printInfor(self):
        print ('Name: ', self.name)
        print('Date of birth: ', self.dob)
        
        