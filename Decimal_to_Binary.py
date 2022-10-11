t=int(input())
for i in range(t):
    n=int(input())
    i=0
    s=[]
    while n!=0:
        r=n%10
        a=r%2
        s.append(a)
        n=n//2
    s.reverse()
    for i in s:
        print(i,end='')
    print()