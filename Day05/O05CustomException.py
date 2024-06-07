
class TooTiny(Exception):
    pass

class TooYoung(Exception):
    pass

class TooOld(Exception):
    pass

age = 105

try:
    if age < 6:
        raise TooTiny("voter is too very tiny to cast the vote....")
    elif age < 18:
        raise TooYoung("Voter is a little young to cast the vote....")
    elif age > 100:
        raise TooOld("Voter is very old to cast a vote....")
    else:
        print("You can cast your valuable vote.....")
except TooTiny as t:
    print("Exception captured......")
    print(t)
except TooYoung as y:
    print("Exception captured......")
    print(y)
except TooOld as o:
    print("Exception captured......")
    print(o)
finally:
    print("Completed the process of voting......")


