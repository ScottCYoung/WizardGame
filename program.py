import random

from actors import Wizard, creature


def game_loop():
    # Get input from user until game ends


    creatures = [
        creature('Toad', 10),
        creature('Tiger', 30),
        creature('Bat', 3),
        creature('Dragon', 50),
        creature('Evil Wizard', 1000),
    ]

    hero = Wizard('Gandolph', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of {} has appeared from a dark and foggy forest'.format(
            active_creature.name, active_creature.level))

        cmd = input('Do you [a]ttack, [r]unaway or [l]ook around?')
        if cmd == 'a':
            hero.attack(active_creature)
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('look around')
        else:
            print('Ok, exiting game. Goodbye!')
            break


def print_header():
    print('---------------------------------')
    print('        Wizard Game')
    print('---------------------------------')
    print('')


def main():
    print('Welcome to main')
    print_header()
    game_loop()


if __name__ == '__main__':
    main()
