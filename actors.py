# start by creating a blueprint to build out instances of classes
import random


class Wizard:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def attack(self, creature):
        print('The wizard {} has attacked {}!'.format(
            self.name, creature.name
        ))

        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print('You rolled {}'.format(my_roll))
        print('{} rolled {}'.format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('The wizard {} has handily triumped over {}'.format(self.name, creature.name))
        else:
            print('The wizard {} has been defeated!'.format(self.name))


class creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return 'Creature {} of level {}'.format(
            self.name, self.level
        )

# level
# name
