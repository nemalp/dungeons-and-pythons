from weapon_and_spell_classes import Weapon, Spell


def read_map_file():
    with open('map.txt', 'r') as f:
        result = []
        for line in f.readlines:
            line = line.strip('\n')
            row = []
            for char in line:
                row.append(char)
            result.append(row)
        return result


def read_weapon_file():
    weapons_storage = []
    with open('weapons.txt', 'r') as f:
        for line in f.readlines:
            line = line.strip('\n')
            weapon_data = line.split('|')
            weapon = Weapon(weapon_data[0], weapon_data[1])
            weapons_storage.append(weapon)
    return weapons_storage


def read_spell_file():
    spells_storage = []
    with open('spells.txt', 'r') as f:
        for line in f.readlines:
            line = line.strip('\n')
            spell_data = line.split('|')
            spell = Spell(spell_data[0], spell_data[1], spell_data[2], spell_data[3])
            spells_storage.append[spell]
    return spells_storage
