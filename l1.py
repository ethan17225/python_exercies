def isEven(n):
    return n%2==0


i = 0
l=[]
while i<100:
    if isEven(i):
        l.append(i)
    i +=1



l1 = [x for x in range(0,100) if isEven(x)]
print (l1)
