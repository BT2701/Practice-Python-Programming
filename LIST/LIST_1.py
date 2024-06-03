# CREATE AN EMPTY LIST
## emptyList1= []
## emptyList2= list()


# CREATE AN LIST WITH ELEMENTS
colors=['red', 'blue', 'green', 'white', 'black']   #ROOT


# GET SIZE OF LIST
## len(colors)           # 5


# COUNT ELEMENTS IN LIST
## colors.count('red')     # 1
 


# SELECT ELEMENTS
## print(colors)        #'red', 'blue', 'green', 'white', 'black'
## print(colors[:])      #'red', 'blue', 'green', 'white', 'black'
## print(colors[1:4])      #'blue', 'green', 'white'


# HANDLE LIST
## colors.append("yellow")     #'red', 'blue', 'green', 'white', 'black', 'yellow'
## colors.insert(2,'purple')      #'red', 'blue', 'purple', 'green', 'white', 'black'
## colors.remove('white')        #'white' is removed.  remove() function just delete only one element. If colors contain two elements 'white', remove() function will delete the first element

## if 'white' in colors:        
##     colors.remove('white')

##colors.pop(3)       #index 3='white', index 3 will be removed

##colors.clear()    #make list empty


# SORT LIST
##colors.reverse()    #reverse the list(Đảo ngược danh sách)
##colors.sort()         #sort list ascending
##colors.sort(reverse=True)   #decrease

# for i in range(0,len(colors)):
#     print(colors[i])


maMonHoc={"lập trình python":1, "java": 2, "mã nguồn mở": 3}
maNganh={1: 'cntt', 2:'ktpm', 3:'httt'}

valueMonHoc= list(maMonHoc.values())
keyNganh=list(maNganh.keys())

newDict={}
for i in range(len(valueMonHoc)):
    if valueMonHoc[i]==keyNganh[i]:
        monHoc= [key for key, val in maMonHoc.items() if val==valueMonHoc[i] ] [0]
        nganh=[val for key, val in maNganh.items() if key==keyNganh[i] ] [0]
        newDict[monHoc]=nganh

print(newDict)