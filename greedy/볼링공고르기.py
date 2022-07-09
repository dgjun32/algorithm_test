n, m = map(int, input().split())
li = list(map(int, input().split()))


import math
from math import comb
import collections

# compute total # of combinations
total = comb(n, 2)
# subtracting overlapping combinations
counts = list(collections.Counter(li).values())
sub = [comb(i,2) for i in counts]

print(total - sum(sub))

