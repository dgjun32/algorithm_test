N = int(input())

half = int(len(str(N)) / 2) # index는 정수로!
first = sum([int(i) for i in str(N)[:half]])
second = sum([int(i) for i in str(N)[half:]])

if first == second:
    print('Lucky')
else:
    print('Ready')

