from file_readers import *
from random import randint

POTION_SIZES = [20, 40, 60, 80, 100]


def weapon_randomizer():
    weapons_storage = read_weapon_file()
    j = 0
    for i in range(randint(0, 100)):
        random_weapon = weapons_storage[j]
        j += 1
        if j == 3:
            j = 0


def spell_randomizer():
    spell_storage = read_spell_file()
    j = 0
    for i in range(randint(0, 100)):
        random_spell = spell_storage[j]
        j += 1
        if j == 3:
            j = 0


def potion_size_randomizer():
    j = 0
    for i in range(randint(0, 100)):
        random_potion_size = POTION_SIZES[j]
        j += 1
        if j == 3:
            j = 0
