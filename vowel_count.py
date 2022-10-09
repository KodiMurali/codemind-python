s='aeiouAEIOU'
n=input()
a=[]
c=0
for i in n:
    for j in s:
        if i==j:
            c+=1
print(c)