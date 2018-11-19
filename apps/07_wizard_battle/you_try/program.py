import random
import time

import actors
from actors import Wizard, Creature


def main():
    print_header()
    game_loop()


def print_header():
    print('-------------------')
    print('    Wizard App')
    print('-------------------')
    print()


def game_loop():

    creatures = [
        Creature('Toad', 1),
        Creature('Tiger', 3),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000),
    ]

    hero = Wizard('Gandalf', 75)

    while True:

        active_creature = random.choice(creatures)
        print()
        print('A {} of level {} has appeared from a dark and foggy forest...'.format(
            active_creature.name, active_creature.level))
        print()


        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("Wizard hides...")
                time.sleep(5)
                print("wizard returns!")
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('The wizard {} looks around:'.format(hero.name))
            for c in creatures:
                print(f' * A {c.name} of level {c.level}')
        else:
            print('OK, exiting game...bye!')
            break


if __name__ == "__main__":
    main()