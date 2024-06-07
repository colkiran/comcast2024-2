
def fun():
    x = 1
    print("apples from Ooty....")
    yield 1
    x += 9
    print("Oranges from kanpur......")
    yield x
    x += 10
    print("Grapes from hubli.....")
    yield x

res = fun()
print(f"res :{res}")

print("-" * 60)
print(next(res))

print("-" * 60)
print(next(res))

print("-" * 60)
print(next(res))

# print("-" * 60)
# print(next(res))

print("-" * 60)
def fun():
    for i in range(1, 11):
        yield i

fObj = fun()

print(fObj.__next__())
print(fObj.__next__())
print(fObj.__next__())

print("-" * 60)
for x in fun():
    print(x, end=" ")
print()
