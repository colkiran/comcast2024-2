
l1 = list(range(1, 31))
print(f"l1 :{l1}")

res = list(filter(lambda x: x % 3 == 0, l1))
print(f"res :{res}")

print("-" * 60)

st = "the quick brown fox jumps over the lazy dog"
print(f"st :{st}")

res = list(filter(lambda x: x != 'the', st.split()))
print(f"res :{res}")

res = list(filter(lambda y: len(y) > 3, st.split()))
print(f"res :{res}")

