import random
import pickle

NEIGHBOUR_INDEXES = [(-1, -1), (-1, 0), (-1, 1),
                     (0, -1), (0, 1),
                     (1, -1), (1, 0), (1, 1)]

TREASURE_TYPES = ['m_pot', 'h_pot', 'weapon', 'spell']
POTION_SIZES = [20, 30, 50]


def check_if_inside_map(location, map):
    """
    The function takes a tuple -> location and
    a Dungeon object -> map and calculates if the location
    is inside it.
    Returns True if the location is inside the map;
    Returns False if the location is not inside the map.
    """
    if location[0] < 0 or location[0] > map.row_len:
        return False
    if location[1] < 0 or location[1] > map.col_len:
        return False
    return True


def check_if_not_obstacle(location, map):
    """
    Returns True if there is no obstacle on the given location
    Returns False if there is an obstacle on the given location
    """
    if map.matrix_format[location[0]][location[1]] == "#":
            return False
    return True


def enemy_check(location, map):
    """
    Returns True if there is an Enemy object at the given location.
    """
    item = map.matrix_format[location[0]][location[1]]
    if isinstance(item, Enemy):
        return True
    return False


def treasure_check(location, map):
    item = map.matrix_format[location[0]][location[1]]
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
