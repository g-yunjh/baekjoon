n, x = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
true_a = []
for i in a:
    if i<x:
        true_a. append(i)
    else:
        pass
print(*true_a)