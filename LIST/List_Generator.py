colors= ['red', 'blue', 'green', 'white', 'black']

# basic
def basic0():
    for color in colors:
        yield color

# list conprihention
basic1= (color for color in colors)

def main():
    # test0= basic0()
    # print(test0.__next__())
    # print(list(test0))
    test1= basic1
    print(list(test1))


if __name__=='__main__':
    main()