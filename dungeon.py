from pprint import pprint
from random import randint

class Dungeon:
    def __init__(self, map):
        self.map = map

    def spawn(self, hero):
        flag_spawn_found = False
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if map[i][j] == 'S':
                    hero.location = (i, j)
                    flag_spawn_found = True
        self.map[i][j] = 'H'
        if flag_spawn_found is True:
            return True
        else:
            return False

    def treasure_check(self, hero):
        if self.map[hero.location[0]][hero.location[1]] == "T":
            return True
        return False

    def treasure_type_randomizer(self):
        for i in range(randint(100)):
            for j in ['mpot', 'hpot', 'weapon', 'spell']:
                result = j
        return result

    def pick_treasure(selfm type_of_treasure):
        if type_of_treasure == 'mpot':
            pass
            # TODO: Implement mana potion usage
        elif type_of_treasure == 'hpot':
            pass
            # TODO: Implement health potion usage
        elif type_of_treasure == 'weapon':
            pass
            # TODO: Implement weapon randomization
        else:
            pass
            # TODO: Implement spell randomization

    def obstacle_check(self, hero):
        if self.map[hero.location[0]][hero.location[1]] == "#":
            return True
        return False

    def enemy_check(self, hero):
        if self.map[hero.location[0]][hero.location[1]] == 'E':
            return True
        return False

    def hero_move(self, direction, hero):
        if direction == 'up':
            if obstacle_check(self, hero):
                return False
            if enemy_check(self, hero):
                pass
                # TODO: Implement fight initiation
            if treasure_check(self, hero):
                pass
                # TODO: Implement treasure randomization
            hero.location[0] -= 1
        elif direction == 'down':
            if obstacle_check(self, hero):
                return False
            if enemy_check(self, hero):
                pass
                # TODO: Implement fight initiation
            if treasure_check(self, hero):
                pass
                # TODO: Implement treasure randomization
            hero.location[0] += 1
        elif direction == 'left':
            if obstacle_check(self, hero):
                return False
            if enemy_check(self, hero):
                pass
                # TODO: Implement fight initiation
            if treasure_check(self, hero):
                pass
                # TODO: Implement treasure randomization
            hero.location[1] -= 1
        elif direction == 'right':
            if obstacle_check(self, hero):
                return False
            if enemy_check(self, hero):
                pass
                # TODO: Implement fight initiation
            if treasure_check(self, hero):
                pass
                # TODO: Implement treasure randomization
            hero.location += 1
        else:
            print("Invalid direction")
            return False
        self.map[hero.location[0]][hero.location[1]] = 'H'
