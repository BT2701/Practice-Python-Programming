widths= [1,3,6,1,7,9]
heights= [1,6,3,2,9,0]
weights= [1,2,4,5,9,8]
def dienTich(width, weight):
    return width * weight

def chuVi(width, weight):
    return (width+weight)/2
def theTich(width, height, weight):
    return width*height*weight

def checkSNT(x):
    if x< 2: 
        return False
    else:
        for i in range (2,x): 
            if x%i==0:
                return False
    return True

print('Chiều dài: ', [width for width in widths])
print('Chiều cao: ', [height for height in heights])
print ('Chiều rộng: ', [weight for weight in weights])
print('=======================')
# sở dĩ dùng [] là để đánh dấu đó là một list các diện tích/ chu vi/ thể tích
print('Diện tích: ',[dienTich(width, weight) for width, weight in zip(widths, weights)])
print( 'Chu vi: ',[chuVi(width, weight) for width, weight in zip (widths, weights)])
print('Thể tích: ',[theTich(width, height, weight) for width, height, weight in zip(widths, heights, weights)]) 
print('danh sach so nguyen to: ', [x for x in widths if checkSNT(x)])