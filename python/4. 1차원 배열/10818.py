n = int(input())
x = list(map(int, input().split(" ")))
x_list = [min(x),max(x)]
print(*x_list)