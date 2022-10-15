n=int(input())
c=0
s=0
for i in range(n):
    t=2**i
    if t==n:
        s=1
        break
    elif t>n:
        s=0
        break
if s==1:
    print(True)
else:
    print(False)