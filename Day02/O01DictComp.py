
d1 = [(x, y) for x in range(3) for y in range(3)]
print(f"d1 :{d1}")

print("-" * 60)
d2 = [(x, y) for x in range(1, 6) for y in range(1, x + 1)]
print(f"d2 :{d2}")

print("-" * 60)
st = "the quick brown fox jumps over the lazy dog"
res = {st :len(st) for st in st.split()}
print(f"res :{res}")

print("-" * 60)
sqrs = {x: x**2 for x in range(1, 11)}
print(f"Squares :{sqrs}")

players = {
    'sachin': [290, 350, 460, 401, 390],
    'sourav': [140, 190, 385, 430, 320],
    'rahul': [230, 410, 185, 275, 370],
    'sehwag': [380, 430, 485, 365, 400],
    'yuvraj':[160, 245, 350, 130, 175]
}

print(f"players :{players}")

print("-" * 60)
print(f"sachin :{players['sachin']}")

print("-" * 60)
print(f"sachin :{sum(players['sachin'])}")

print("-" * 60)
print({p: r for (p, r) in players.items()})

print("-" * 60)
scores = {player: sum(runs) for (player, runs) in players.items()}
print(scores)

print("-" * 60)
scores = {plyr: (lambda score: sum(score) / len(score))(scr)
          for (plyr, scr) in players.items()}
print(scores)

print("-" * 60)
basic = [{x: (lambda par: "Mr." + par)("Sachin {}".format(x))}
         for x in range(1, 6)]
print(basic)

print("-" * 60)
scores = [score for score in players.values()]
print(f"scores :{scores}")

players = {
    'sachin': [290, 350, 460, 401, 390],
    'sourav': [140, 190, 385, 430, 320],
    'rahul': [230, 410, 185, 275, 370],
    'sehwag': [380, 430, 485, 365, 400],
    'yuvraj':[160, 245, 350, 130, 175]
}

print("-" * 60)
scores =  [scr for score in players.values() for scr in score if scr > 200]
print(scores)

# print all players and their scores that is greater than 200 runs

print("-" * 60)
scores = {plyr: [scr for scr in score if scr > 200]
          for (plyr, score) in players.items()}
print(scores)
