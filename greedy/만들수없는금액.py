N = map(int, input())
data = list(map(int, input().split()))

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)

