# hàm nhận hàm khác làm tham số (map)
def binhPhuong(x):
    return x*x


numbers=[1,2,3,4,5,6,7,8,9]

def isSoNT(x):
    if x <2:    return False
    else:
        for i in range(2,x):
            if x%i==0:
                return False
    return True

def getListSnt():
    return list(filter(isSoNT,numbers))

if __name__=='__main__':
    numList=map(binhPhuong,getListSnt())
    print(list(numList))


def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)
times5 = make_multiplier(5)

print(times3(10))  # Output: 30
print(times5(10))  # Output: 50









# on tap tonng quan
# map
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]


# filter
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_even, numbers)

print(list(even_numbers))  # Output: [2, 4]




# ham kep
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)
times5 = make_multiplier(5)

print(times3(10))  # Output: 30
print(times5(10))  # Output: 50





# reduce
from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
total = reduce(add, numbers)

print(total)  # Output: 15







# lambda
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x * x, numbers)

print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]


numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))  # Output: [2, 4]



numbers = [1, 2, 3, 4, 5, 6]
squared_even_numbers = map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers))

print(list(squared_even_numbers))  # Output: [4, 16, 36]
