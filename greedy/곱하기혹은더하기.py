num = input()

# solution 1
N = len(num)
temp = int(num[0])

for i, n in enumerate(num[1:]):
    temp = max(temp*int(n), temp+int(n))


# solution 2 - 조금 더 효율적인 솔루션
N = len(num)
temp = int(num[0])

for i, n in enumerate(num[1:]):
    # 현재까지의 계산값이 2 이하이면 둘 다 비교
    if temp <= 2:
        temp = max(temp*int(n), temp+int(n))
    # 현재까지의 계산값이 2 초과면, 다음 숫자가 1만 아니면 무조건 곱해주는게 이득임
    else:
        if n == '1':
            temp = temp + int(n)
        else:
            temp = temp*int(n)

print(temp)
