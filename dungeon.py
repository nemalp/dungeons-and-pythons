from helper_functions import load_map, objectify_map, check_if_passable, change_hero_location, check_for_enemies_in_cast_range
from enemy import Enemy
from fight import Fight

class Dungeon:
    def __init__(self):
        self.hero = None
        self.map_ = load_map("map.txt")
        self.matrix_format = objectify_map(self.map_)

    def hero_attack(self, by):
        if by == 'magic':
            if self.hero.can_cast():
                enemy_to_attack = check_for_enemies_in_cast_range(self.matrix_format, self.hero.location, self.hero.spell.cast_range)
                if enemy_to_attack:
                    fight = Fight(self.hero, enemy_to_attack[0], enemy_to_attack[2])
                    fight.start_fight()

    def spawn(self, hero):
        spawning_point_found = False
        for row in range(len(self.map_)):
            for col in range(len(self.map_[row])):
                if self.map_[row][col] == 'S':
                    self.map_[row][col] = 'H'
                    hero.location = [row, col]
                    self.hero = hero
                    hero.map_ = self.matrix_format
                    spawning_point_found = True
                    break
        return spawning_point_found

    def print_map(self):
        printable_map = ''
        for row in range(len(self.matrix_format)):
            for col in range(len(self.matrix_format[row])):
                if isinstance(self.matrix_format[row][col], Enemy):
                    printable_map += 'E'
                else:
                    printable_map += self.matrix_format[row][col]
            printable_map += '\n'
        return printable_map

    # possible implementation of moving

    def move_hero(self, hero, direction):
        if direction == 'up':
            desired_location = (hero.location[0] - 1, hero.location[1])
            change_hero_location(hero, desired_location, self.matrix_format)
        elif direction == 'down':
            desired_location = (hero.location[0] + 1, hero.location[1])
            change_hero_location(hero, desired_location, self.matrix_format)
        elif direction == 'left':
            desired_location = (hero.location[0], hero.location[1] - 1)
            change_hero_location(hero, desired_location, self.matrix_format)
        elif direction == 'right':
            desired_location = (hero.location[0], hero.location[1] + 1)
            change_hero_location(hero, desired_location, self.matrix_format)
        else:
            return False
