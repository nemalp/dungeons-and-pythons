import random
from pprint import pprint
from map_reader import load_map
from helpers import check_position


class Dungeon:

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

    def update_map(self, hero):
        self.map_[hero.location[0]][hero.location[1]] = 'H'

    def pick_treasure(self, treasure_type, hero):
        treasures = ['heal', 'mana', 'weapon', 'spell']

        treasure = random.choice(treasures)

        if treasure == 'heal':
            healing = random.choice(Dungeon.TREASURES[treasure])

            if hero.take_healing(healing) is False:
                print('Cannot take healing')

        elif treasure == 'mana':
            mana = random.choice(Dungeon.TREASURES[treasure])

            if hero.take_mana(mana) is False:
                print('Cannot take mana')

        elif treasure == 'weapon':
            weapon = random.choice(Dungeon.TREASURES[treasure])
            hero.equip(weapon)

        elif treasure == 'spell':
            spell = random.choice(Dungeon.TREASURES[treasure])
            hero.learn(spell)

    def move_hero(self, direction, hero):
        if check_position(hero, direction, self.map_) is False:
            return False

        elif direction == 'up':
            hero.location[0] -= 1
            self.update_map(hero)

        elif direction == 'down':
            hero.location[0] += 1
            self.update_map(hero)

        elif direction == 'left':
            hero.location[1] -= 1
            self.update_map(hero)

        elif direction == 'right':
            hero.location[1] += 1
            self.update_map(hero)
