def isScalene (x, y, z):
    if y != z and y !=x and z != x:
        print ("this is scalene")
        return True
    else:
        print ("this is NOT scalene")
        return False
isScalene(3,3,8)



#Create a function that takes in two numbers as arguments and returns a list of numbers starting from start to the end number (inclusive) specified in the arguments.
def genNums(start, end):
    m = []
    while (start != end):
        m.append(start)
        start = start + 1
    print (m)
genNums(9,21)




#Write a function that takes in two numbers and return the bigger number
def getBigNum(x,y):
    if x > y:
        print(x)
        print("is bigger")
        return (x)
    if y > x:
        print(y)
        print("is bigger")
        return (y)
getBigNum(50,6)


#Write a function that takes in list as parameter and returns the bigger number from the list.
