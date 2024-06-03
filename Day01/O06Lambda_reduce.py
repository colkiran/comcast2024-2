
from functools import reduce

l1 = [3, 8, 5, 7, 10, 4, 6, 9, 2, 1]
print(f"l1 :{l1}")

res = reduce(lambda x, y: x if x > y else y, l1)
print(f"res :{res}")

# x = x + y
res = reduce(lambda x, y: x + y, l1)
print(f"res :{res}")
