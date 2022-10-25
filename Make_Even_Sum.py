n = int(input())
a = list(map(int,input().split()))
ns = sum(a)
if (ns%2==0):
    print("1")
else:
    print("0")
    