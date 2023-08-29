s = input()
t = len(s)
n = 0

if t%2 == 0:
    for i in range(t):
        if s[i] != s[t-i-1]:
            n = 0
        else:
            n = 1
else:
    for i in range(t):
        if s[i] != s[t-i-1]:
            n=0
        else:
            n=1

print(n)