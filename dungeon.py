from pprint import pprint
from random import randint
from treasure_randomizers import spell_randomizer, weapon_randomizer

TREASURE_TYPES = ['mpot', 'hpot', 'weapon', 'spell']


class Dungeon:
    def __init__(self, map):
        self.map = map

    def print_map(self):
        pprint(self.map)

    def spawn(self, hero):
        flag_spawn_found = False
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if map[i][j] == 'S':
                    hero.location = (i, j)
                    flag_spawn_found = True
                    self.map[i][j] = 'H'
                    break
                if flag_spawn_found is True:
                    break
        if flag_spawn_found is True:
            return True
        else:
            return False

    def treasure_check(self, hero):
        if self.map[hero.location[0]][hero.location[1]] == "T":
            return True
        return False

    def treasure_type_randomizer(self):
        j = 0
        for i in range(randint(0, 100)):
            result = TREASURE_TYPES[j]
            j += 1
            if j == 3:
                j = 0
        return result

    def pick_treasure(self, type_of_treasure, hero):
        if type_of_treasure == 'mpot':
            random_potion_size = potion_size_randomizer()
            if hero.take_mana(random_potion_size) is False:
                print('Unable to drink mana potion\n')
        elif type_of_treasure == 'hpot':
            random_potion_size = potion_size_randomizer()
            if hero.take_healing(random_potion_size) is False:
                print('Unable to drink health potion')
        elif type_of_treasure == 'weapon':
            random_weapon = weapon_randomizer()
            print("""You found a weapon!\n{} - {}\n
                   Would you like to equip it? (y/n)""".format(random_weapon.name, random_weapon.damage))
            user_equip_answer = input()
            if user_equip_answer == 'y' or user_equip_answer == 'Y':
                hero.equip(random_weapon)
            else:
                return None
        else:
            random_spell = spell_randomizer()
            print("""You found a spell!\n{} - {}\n
                   Would you like to  learn it? (y/n)""".format(random_spell.name, random_spell.damage))
            user_equip_answer = input()
            if user_equip_answer == 'y' or user_equip_answer == 'Y':
                hero.learn(random_spell)
            else:
                return None

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
                treasure_type = treasure_type_randomizer
                pick_treasure(treasure_type, hero)
            hero.location[0] -= 1
        elif direction == 'down':
            if obstacle_check(self, hero):
                return False
            if enemy_check(self, hero):
                pass
                # TODO: Implement fight initiation
            if treasure_check(self, hero):
                treasure_type = treasure_type_randomizer
                pick_treasure(treasure_type, hero)
            hero.location[0] += 1
        elif direction == 'left':
            if obstacle_check(self, hero):
                return False
            if enemy_check(self, hero):
                pass
                # TODO: Implement fight initiation
            if treasure_check(self, hero):
                treasure_type = treasure_type_randomizer
                pick_treasure(treasure_type, hero)
            hero.location[1] -= 1
        elif direction == 'right':
            if obstacle_check(self, hero):
                return False
            if enemy_check(self, hero):
                pass
                # TODO: Implement fight initiation
            if treasure_check(self, hero):
                treasure_type = treasure_type_randomizer
                pick_treasure(treasure_type, hero)
            hero.location += 1
        else:
            print("Invalid direction")
            return False
        self.map[hero.location[0]][hero.location[1]] = 'H'
