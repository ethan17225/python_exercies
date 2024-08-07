n = 0
l=[]
while n<100:
    isPrime = True

    if n%2==0:
        isPrime = False
    else:
        for d in range(3,n//2, 2):
            if n%d==0:
                isPrime = False
                break;

    if isPrime:
        l.append(n)

    n+=1


print (l)
