
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

frts = list(filter(lambda x: x[1] > 100, fruits))
print(f"Price more than 200: {frts}")

Discount = [frtt[1] * 0.9 for frtt in frts]
print(f"10% Discount: {Discount}")

Discount = [frtt[1] * 0.75 for frtt in frts]
print(f"25% Discount: {Discount}")

Discount = [(frtt[0], frtt[1], frtt[1] * 0.9, frtt[1] * 0.75) for frtt in fruits if frtt[1] > 100]
print(f"Expensive Fruits: {Discount}")
