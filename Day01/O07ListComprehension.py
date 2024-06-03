
squares = [x ** 2 for x in range(1, 11)]
print(f"squares :{squares}")

fruits = [
    ('apple', 350),
    ('oranges', 180),
    ('grapes', 140),
    ('gauva', 90),
    ('watermelon', 75),
    ('banana', 60),
    ('strawberry', 400),
    ('pineapple', 130)
]

print(f"fruits :{fruits}")
print("-" * 60)

prices = ["fruit" for fruit in fruits]
print(prices)
print("-" * 60)

prices = [fruit for fruit in fruits]
print(f"prices :{prices}")
print("-" * 60)

frts = [fruit[0] for fruit in fruits]
print(frts)
print("-" * 60)

prices = [fruit[1] for fruit in fruits]
print(f"prices :{prices}")
print("-" * 60)

prices = [fruit[1] * 0.9 for fruit in fruits]
print(f"prices :{prices}")
print("-" * 60)

prices = [fruit[1] * 0.75 for fruit in fruits]
print(f"price :{prices}")

# print the fruits whose price > 200 with original prc, 10 and 25 % disc