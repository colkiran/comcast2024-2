
l = ['a', 'b', 'c', 'd', 'e']
print(f"l :{l}")
print(type(l))

print(dir(l))
iterObj = iter(l)
print(dir(iterObj))
# __iter__ and __next__ methods are the protocols of iteration

print("-"  * 60)
e1 = iterObj.__next__()
print(f"element01 :{e1}")

print("-"  * 60)
e2 = iterObj.__next__()
print(f"element02 :{e2}")

print("-"  * 60)
e3 = next(iterObj)
print(f"element03 :{e3}")

print("-"  * 60)
e4 = next(iterObj)
print(f"element04 :{e4}")

print("-"  * 60)
e5 = next(iterObj)
print(f"element05 :{e5}")

print("-"  * 60)
e6 = next(iterObj)
print(f"element06 :{e6}")




