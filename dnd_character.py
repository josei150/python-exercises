from random import randint
import math

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)


    def ability(self):
        hauls = []
        for _ in range(4):
            hauls.append(randint(1, 6))
        hauls.sort()
        hauls.pop(0)
        return sum(hauls)


def modifier(constitution):
    return math.floor((constitution - 10) / 2)


if __name__ == "__main__":
    character = Character()
    # print(character.strength)
    # print(character.dexterity)
    # print(character.constitution)
    # print(character.intelligence)
    # print(character.wisdom)
    # print(character.charisma)
    print(character.hitpoints)
    print(modifier(character.constitution))