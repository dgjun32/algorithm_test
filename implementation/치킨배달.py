import itertools

N, M = list(map(int, input().split()))
city = []
chicken_idx = []
house_idx = []
for i in range(N):
    row = list(map(int, input().split()))
    city.append(row)
    for j, num in enumerate(row):
        if num == 1:
            house_idx.append((i,j))
        elif num == 2:
            chicken_idx.append((i,j))

# l1 distance 함수
def distance(a,b):
    return sum(list(map(lambda x,y : abs(x-y), a, b)))

# 집 위치가 주어졌을 때, 집에 대한 치킨 거리 구하는 함수
def c_dist(c_idxes, h_idx):
    min_dist = 1000000
    for c_idx in c_idxes:
        dist = distance(c_idx, h_idx)
        if dist < min_dist:
            min_dist = dist
    return min_dist


minimum = 1000000
# 치킨집의 개수를 인덱스로 표현
indexes = itertools.combinations([i for i in range(len(chicken_idx))], M)
# 가능한 치킨집의 모든 경우의 수에 대해 '도시의 치킨 거리' 계산
for idx in list(indexes):
    temp = 0
    r_chicken_idx = [chicken_idx[i] for i in idx]
    # 모든 집들에 대해 각 집의 치킨거리 구함 -> 도시의 치킨 거리에 더해줌
    for h_idx in house_idx:
        temp += c_dist(r_chicken_idx, h_idx)
    
    if temp < minimum:
        minimum = temp
    
print(minimum)