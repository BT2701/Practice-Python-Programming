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

