n=int(input())
i=0
s=[]
sss=[]
while n!=0:
    r=n%10
    a=r%2
    s.append(a)
    n=n//2
s.reverse()
for i in s:
    if i==0:
        sss.append(1)
    else:
        sss.append(0)
ss=0
for i in sss:
    ss=ss*10+i
sum=0
i=0
while ss!=0:
    rr=ss%10
    sum=sum+(rr*(2**i))
    i+=1
    ss=ss//10
print(sum)