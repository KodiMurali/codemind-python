t=int(input())
for i in range(t):
    n=int(input())
    s=0
    i=0
    l=[]
    while n!=0:
        r=n%10
        s=s+(r*(2**i))
        i+=1
        n=n//10
    j=0
    while s!=0:
        r=s%8
        l.insert(i,r)
        s=s//8
    l.reverse()
    for i in l:
        print(i,end='')
    print()
    