#!/usr/bin/env python3

# always add shebang on top of page

# standard library first!
from random import randint


class Player:
    def __init__(self):
        self.dice = []
    def roll(self):
        # Clear current dice
        self.dice = []
        for i in range(6):
            self.dice.append(randint(1,6))
    def get_dice(self):
        return self.dice

class Dependapotomus(Player):
    def love(self, dependa: Player):
        dependa.dice = [randint(1,3) for i in range(6)]

p1 = Player()
p2 = Dependapotomus()

p1.roll()
p2.roll()

print(p1.get_dice())
print(sum(p1.get_dice()))

p2.love(p1)

print(p1.get_dice())
print(sum(p1.get_dice()))

