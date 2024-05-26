import sys
import os

# Giả sử file Student_HOF.py nằm trong thư mục Model nằm cùng cấp với file hiện tại
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Model.Student_HOF import *
from functools import reduce

db = session()
students = get_students(db)

def listStudent():
    for sv in students:
        print(' name: ',f'{sv.name}', ' age: ',f'{sv.age}',' department: ', f'{sv.department}',' math: ',f'{sv.math}', ' english: ',f'{sv.english}', ' it: ',f'{sv.it}')

def listMath():
    for sv in students:
        # dung generator luon cho vip
        yield sv.math

def listEnglish():
    for sv in students:
        yield sv.english

def listIT():
    for sv in students:
        yield sv.it

def dtb(x,y,z):
    return (x,y,z)/3

def studentById(id):
    for i in students:
        if id == i.id:
            return i
    return None

def diemById(id):
    diem=[]
    if studentById(id) != None:
        diem.append(studentById(id).math)
        diem.append(studentById(id).english)
        diem.append(studentById(id).it)
    return diem

def tb(id):
    total = reduce(dtb, diemById(id))
    return total

def printDiemTB():
    for sv in students:
        print(f'{sv.name}: ',tb(sv.id))