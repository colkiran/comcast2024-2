
l = ['a', 'b', 'c', 'd', 'e']
print(f"l :{l}")

iterObj = iter(l)

while True:
    try:
        elem = next(iterObj)
        print(elem, end=" ")
    except StopIteration:
        break
print()

print("-"  * 60)
for i in l:
    print(i, end=" ")
print()

