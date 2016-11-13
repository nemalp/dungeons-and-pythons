import random
import pickle
from enemy import Enemy
from fight import Fight


NEIGHBOUR_INDEXES = [(-1, -1), (-1, 0), (-1, 1),
                     (0, -1), (0, 1),
                     (1, -1), (1, 0), (1, 1)]

TREASURE_TYPES = ['m_pot', 'h_pot', 'weapon', 'spell']
POTION_SIZES = [20, 30, 50]


def check_if_inside_map(location, map_):
    """
    The function takes a tuple -> location and
    a Dungeon object -> map and calculates if the location
    is inside it.
    Returns True if the location is inside the map;
    Returns False if the location is not inside the map.
    """
    if location[0] < 0 or location[0] > len(map_) - 1:
        return False
    if location[1] < 0 or location[1] > len(map_[0]) - 1:
        return False
    return True


def check_if_not_obstacle(location, map_):
    """
    Returns True if there is no obstacle on the given location
    Returns False if there is an obstacle on the given location
    """
    if map_[location[0]][location[1]] == "#":
            return False
    return True


def enemy_check(location, map_):
    """
    Returns True if there is an Enemy object at the given location.
    """
    item = map_[location[0]][location[1]]
    if isinstance(item, Enemy):
        return True
    return False


def treasure_check(location, map_):
    item = map_[location[0]][location[1]]
    if item == 'T':
        return True
    return False


def treasure_randomizer():
    """
    Randomizes the type of the treasure;
    If the type is a weapon or a spell it reads a serialized list
    from a binary file and chooses a random item from it.
    Returns a tuple containing the type of the treasure and the treasure itself.
    """
    treasure_type = random.choice(TREASURE_TYPES)
    if treasure_type == 'm_pot' or treasure_type == 'h_pot':
        treasure_value = random.choice(POTION_SIZES)
    elif treasure_type == 'weapon':
        with open('weapons.src', 'rb') as weapon_storage:
            all_weapons = pickle.load(weapon_storage)
        treasure_value = random.choice(all_weapons)
    else:
        with open('spells.src', 'rb') as spell_storage:
            all_spells = pickle.load(spell_storage)
        treasure_value = random.choice(all_spells)
    return (treasure_type, treasure_value)


def check_if_passable(location, map_):
    if check_if_inside_map(location, map_) and check_if_not_obstacle(location, map_):
        if enemy_check(location, map_):
            return map_[location[0]][location[1]]
        if treasure_check(location, map_):
            treasure_type, treasure_value = treasure_randomizer()
            return (treasure_type, treasure_value)
        else:
            return True
    else:
        return False


def load_map(filename):
    with open(filename, 'r') as f:
        data = f.read().split('\n')
        map_ = [list(x) for x in data if x.strip() != '']
        return map_



def objectify_map(map_):
    for i in range(len(map_)):
        for j in range(len(map_[i])):
            if map_[i][j] == 'E':
                map_[i][j] = Enemy(random.randint(1, 70), random.randint(1, 20), random.randint(1, 20))
                map_[i][j].location = [i, j]
    return map_


def find_direction_towards_enemy(hero, enemy):
    if enemy.location[0] > hero.location[0]:
        return 'up'
    elif enemy.location[0] < hero.location[0]:
        return 'down'
    if enemy.location[1] > hero.location[1]:
        return 'right'
    elif enemy.location[1] < hero.location[1]:
        return 'left'


def change_hero_location(hero, desired_location, matrix_format):
    is_passable = check_if_passable(desired_location, matrix_format)
    if is_passable is False:
        return False
    else:
        if isinstance(is_passable, Enemy):
            hero.location[0] = desired_location[0]
            hero.location[1] = desired_location[1]
            fight = Fight(hero, is_passable, find_direction_towards_enemy(hero, is_passable))
            fight.start_fight()
        if type(is_passable) == tuple:
            load_treasure(is_passable, hero)
        if hero.is_alive():
            matrix_format[hero.location[0]][hero.location[1]] = '.'
            matrix_format[desired_location[0]][desired_location[1]] = 'H'
            hero.location[0] = desired_location[0]
            hero.location[1] = desired_location[1]


def load_treasure(treasure_data, hero):
    if treasure_data[0] == 'm_pot':
        hero.take_mana(treasure_data[1])
    elif treasure_data[0] == 'h_pot':
        hero.take_healing(treasure_data[1])
    elif treasure_data[0] == 'weapon':
        hero.equip(treasure_data[1])
    else:
        hero.learn(treasure_data[1])


def check_for_enemies_in_cast_range(map_, hero_location, cast_range):
    """
    Checks for all enemies in a straight line and returns
    a list of the enemies in cast range.
    The calculation for the closest enemy is to be implemented elsewhere!
    """

    #check up
    all_enemies_in_cast_range = []
    flag_obstacle = False
    distance_to_enemy = 0
    for i in range(1, cast_range + 1):
        desired_location = (hero_location[0] - i, hero_location[1])
        if check_if_inside_map(desired_location, map_) is False:
            break
        if map_[hero_location[0] - i][hero_location[1]] == '#':
            flag_obstacle = True
        elif isinstance(map_[hero_location[0] - i][hero_location[1]], Enemy):
            if flag_obstacle:
                break
            else:
                distance_to_enemy += 1
                all_enemies_in_cast_range.append((map_[hero_location[0] - i][hero_location[1]],
                                                 distance_to_enemy, 'up'))


    #check down
    flag_obstacle = False
    for i in range(1, cast_range + 1):
        desired_location = (hero_location[0] + i, hero_location[1])
        if check_if_inside_map(desired_location, map_) is False:
            break
        if map_[hero_location[0] + i][hero_location[1]] == '#':
            flag_obstacle = True
        elif isinstance(map_[hero_location[0] + i][hero_location[1]], Enemy):
            if flag_obstacle:
                break
            else:
                distance_to_enemy += 1
                all_enemies_in_cast_range.append((map_[hero_location[0] + i][hero_location[1]],
                                                 distance_to_enemy, 'down'))

    #check left
    flag_obstacle = False
    for i in range(1, cast_range + 1):
        desired_location = (hero_location[0], hero_location[1] - i)
        if check_if_inside_map(desired_location, map_) is False:
            break
        if map_[hero_location[0]][hero_location[1] - i] == '#':
            flag_obstacle = True
        elif isinstance(map_[hero_location[0]][hero_location[1] - i], Enemy):
            if flag_obstacle:
                break
            else:
                distance_to_enemy += 1
                all_enemies_in_cast_range.append((map_[hero_location[0]][hero_location[1] - i],
                                                 distance_to_enemy, 'left'))

    #check right
    flag_obstacle = False
    for i in range(1, cast_range + 1):
        desired_location = (hero_location[0], hero_location[1] + i)
        if check_if_inside_map(desired_location, map_) is False:
            break
        if map_[hero_location[0]][hero_location[1] + i] == '#':
            flag_obstacle = True
        elif isinstance(map_[hero_location[0]][hero_location[1] + i], Enemy):
            if flag_obstacle:
                break
            else:
                distance_to_enemy += 1
                all_enemies_in_cast_range.append((map_[hero_location[0]][hero_location[1] + i],
                                                 distance_to_enemy, 'right'))
    if(any(all_enemies_in_cast_range)):
        return sorted(all_enemies_in_cast_range, key=lambda x: x[1])[0]
    else:
        return None
