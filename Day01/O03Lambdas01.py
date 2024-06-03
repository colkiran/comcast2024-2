
def add(x, y):
    return x + y

res = add(10, 20)
print(res)

print("-" * 60)

a = add

res = a(38, 73)

print(res)

print("-" * 60)

l = lambda x, y: x + y

res = l(83, 78)

print(res)