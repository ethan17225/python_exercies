def getNumber():
    return int(input("Enter the number: "))

def displayNumber(x):
    print (x)

def isEven(x):
    return x%2==0

def isOdd(x):
    return x%2!=0

def isPrime(x):
    if isEven(x):
        return False

    for d in range(3,x//2,2):
        if x%d==0:
            return False

    return True


def isArmstrong(x):

    p = len(str(x))

    temp = x
    sum = 0

    while temp>0:
        sum += (temp%10) ** p
        temp //= 10

    return x == sum
    


def main():
    n = getNumber()

    if isPrime(n):
        print("it's prime")
    else:
        print("not prime")

    if isArmstrong(n):
        print("it's Armstrong")
    else:
        print("not Armstrong")



main()




