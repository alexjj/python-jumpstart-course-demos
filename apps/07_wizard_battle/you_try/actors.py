import random


class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, creature):
        print("The wizard {} attacks {}!".format(
            self.name, creature.name
        ))

        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print('You roll {}...'.format(my_roll))
        print('{} rolls {}...'.format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('The wizard has defeated over {}'.format(creature.name))
            print()
            return True
        else:
            print('The Wizard failed')
            return False


class Creature:
    # __init__ sets what is set when an instance is created. e.g. name and level. these are compulsory
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return f"Creature: {self.name} of level {self.level}"


