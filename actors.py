# start by creating a blueprint to build out instances of classes

class Wizard:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level


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