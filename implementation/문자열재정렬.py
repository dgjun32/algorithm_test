data = input()

alphabet = []
num = 0

for s in data:
    if s.isalpha():
        alphabet.append(s)
    else:
        num += int(s)

alphabet.sort()
ans = ''.join(alphabet) + str(num)
print(ans)