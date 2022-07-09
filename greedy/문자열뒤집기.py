string = input()

n = 0
start = string[0]
final = string[-1]

# 처음과 끝이 다른 경우 -> (문자가 바뀌는 횟수 + 1)/2
if start != final:
    for i, s in enumerate(string[1:]):
        if s != string[i]:
            n+=1
    print(int(n/2+0.5))

# 처음과 끝이 같은 경우 -> 문자가 바뀌는 횟수 / 2
else:
    for i, s in enumerate(string[1:]):
        if s != string[i]:
            n+=1
    print(int(n/2))
