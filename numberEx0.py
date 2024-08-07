def getNumber():
    return int(input("Enter the number: "))

def displayNumber(x):
    print (x)

def isEven(x):
    return x%2==0

def isOdd(x):
    return x%2!=0

def halfIt(x):
    return x//2

def doubleIt(x):
    return x*2



n = getNumber()

displayNumber(n)

if isEven(n):
  n = halfIt(n)

if isOdd(n):
  n = doubleIt(n)

displayNumber(n)
