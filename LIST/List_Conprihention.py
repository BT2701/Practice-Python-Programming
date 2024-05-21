widths= [1,3,6,1,7,9]
heights= [1,6,3,2,9,0]
weights= [1,2,4,5,9,8]
def dienTich(width, height):
    return width * height

def chuVi(width, height):
    return (width+height)/2
def theTich(width, height, weight):
    return width*height*weight

# sở dĩ dùng [] là để đánh dấu đó là một list các diện tích/ chu vi/ thể tích
print('Diện tích: ',[dienTich(width, height) for width, height in zip(widths, heights)])
print( 'Chu vi: ',[chuVi(width, height) for width, height in zip (widths, heights)])
print('Thể tích: ',[theTich(width, height, weight) for width, height, weight in zip(widths, heights, weights)]) 