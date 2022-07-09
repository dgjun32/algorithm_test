data = input()

min_len = 1000
n = len(data)

for seg in range(1, n//2+1):
    code = ''
    count = 1
    prev = data[0:seg]

    for j in range(seg, n, seg):
        if prev == data[j:j+seg]:
            count += 1
        else:
            code += str(count)+prev if count >=2 else prev
            prev = data[j:j+seg]
            count = 1
    code += str(count)+prev if count >=2 else prev

    if len(code) <= min_len:
        min_len = len(code)

print(min_len)