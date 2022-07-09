li = list(map(int, input().split()))
k = int(input())

n = len(li)
temp = 0
idx = 0

while (sum(li) > 0) & (temp < k):
    # 음식이 있을 때까지 Iterate
    while li[idx]==0:
        idx = idx+1
        idx = idx % n
    
    # eat food
    li[idx] = li[idx]-1
    idx += 1
    idx = idx % n
    temp += 1

# stop iteration(음식이 다 떨어졌거나, 방송 중단됐거나)

# 만약 모든 음식을 다 먹었으면 -1 
if sum(li)==0:
    print(-1)
# 음식이 있을 때까지 iterate
else:
    while li[idx]==0:
        idx = idx+1
        idx = idx%n
    print(idx+1)

    
    