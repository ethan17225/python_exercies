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

def reverse(n):
    temp = n
    rev = 0

    while temp>0:
        rev = rev * 10 + temp%10
        temp = temp//10

    return rev

def isPalindrome(x):
    return x == reverse(x)



def main():

    for n in range (1, 1000):
        if isPrime(n) :
            print (n, "is prime")
        if isArmstrong(n):
            print (n, "is Armstrong")
        if isPalindrome(n):
            print (n, "is Palindrome")

main()




