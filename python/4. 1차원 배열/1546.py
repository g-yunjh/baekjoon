n = int(input())

arr = list(map(int, input().split()))

m = max(arr)

new_list = []
for i in arr:
    new_list.append(i/m*100)

new_mean = sum(new_list)/n
print(new_mean)