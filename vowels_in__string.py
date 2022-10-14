n = "AEIOUaeiou"
s = input()
ss = []
for i in s:
    if i in n:
        if i not in ss:
            ss.append(i)
print(*ss)