import random
from pprint import pprint
from map_reader import load_map


class Dungeon:

    TREASURE_TYPES = ['heal', 'mana', 'weapon', 'spell']
    TREASURES = {
        'heal': [10, 20, 30, 40],
        'mana': [10, 20, 30, 40],
        'weapon': [],
        'spell': []
    }

    def __init__(self, map_):
        self.map_ = load_map(map_)

    def print_map(self):
        pprint(self.map_)

    def spawn(self, hero):
        spawning_point = False

        for row in range(len(self.map_)):
            for col in range(len(self.map_[row])):
                if self.map_[row][col] == 'S':
                    spawning_point = True
                    hero.location = (row, col)
                    self.map_[row][col] = 'H'

        if spawning_point:
            return True
        else:
            return False

    def pick_treasure(self, treasure_type, hero):
        treasures = ['heal', 'mana', 'weapon', 'spell']

        treasure = random.choice(treasures)
        # print(treasure)

        if treasure == 'heal':
            if hero.take_healing(treasure):
                hero.take_healing(random.choice(treasure))

        elif treasure == 'mana':
            if hero.take_mana(treasure):
                hero.take_mana(random.choice(treasure))

        elif treasure == 'weapon':
            hero.equip(random.choice(treasure))

        elif treasure == 'spell':
            hero.learn(random.choice(treasure))
