T=int(input())
for ak in range(T):
    N=int(input())
    if(N%4==0):
        print(N+3)
    elif(N%4==1):
        print(N)
    else:
        print(3)