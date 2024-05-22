# color list
# colors = ['red', 'blue', 'green', 'yellow']

# change to iter
# iters= iter(colors)

# basic iterator
# print ('basic iterator: ',next(iters))
# print('2 cu phap nay giong nhau: ', iters.__next__())

# self iterator
# print('iter: ', iters.__iter__())

# mix iterator with list conprihention
# print('using list conprihention',[next(iters) for i in range(1,4)])



# advanced iterator in python
class circle:
    def __init__(self, data):
        self.data=data
        self.index=0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            self.s= self.dienTich(self.data[self.index])
            self.v= self.chuVi(self.data[self.index])
            self.index = self.index +1
        else:
            raise StopIteration
        return self
    
    def dienTich(self, r):
        return r*3.14*r
    def chuVi(self, r):
        return 2*r*3.14  

class student:
    def __init__(self, id, name, age, dependent, mathGrade, englishGrade, size):
        self.id =id
        self.name=name
        self.age= age
        self.dependent=dependent
        self.mathGrade=mathGrade
        self.englishGrade= englishGrade
        self.index=0
        self.size=size
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < self.size:
            result=[]
            result.append(self.id[self.index])
            result.append(self.name[self.index])
            result.append(self.age[self.index])
            result.append(self.dependent[self.index])
            result.append(self.avg(self.mathGrade[self.index], self.englishGrade[self.index]))
            self.index= self.index+1
        else:
            raise StopIteration
        return result
    
    def avg(self, mathGrade, englishGrade):
        return (mathGrade+englishGrade)/2

        

def main():
    # data=[1,4,2,7]
    # x= circle(data)
    # print('Chu vi: ',[x.__next__().v for i in range(0, len(data))])
    # print('Dien tich: ',[x.__next__().s for i in range(0, len(data))])
    size= 3
    id=[1,2,3]
    name=['Nguyen Van A', 'Pham Thi B' , 'Le Van C']
    age=[19,19,19]
    dependent=['CNTT','QTKD','TMDT']
    mathGrade=[10,9,8]
    englishGrade=[10,8,7]
    sinhvien= student(id, name, age, dependent, mathGrade, englishGrade, size)
    for i in range(0, size):
        print('sinh vien: ', sinhvien.__next__())
if __name__ =="__main__":
    main()