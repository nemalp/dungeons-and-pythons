import pickle
from weapon_and_spell_classes import Spell, Weapon

WEAPONS = []
SPELLS = []


def serialize_and_store_list(list_of_objects, filename):
    with open(filename, 'ab') as storage:
        pickle.dump(list_of_objects, storage)


def main():
    item_type = input("spells or weapons? ")
    choice = 'y'
    if item_type == 'spells':
        while choice != 'n':
            name = input("Enter spell name: ")
            damage = int(input("Enter spell damage: "))
            mana_cost = int(input("Enter mana cost: "))
            cast_range = int(input("Enter cast range: "))
            SPELLS.append(Spell(name, damage, mana_cost, cast_range))
            choice = input("Continue?(y/n)")
        serialize_and_store_list(SPELLS, "spells.src")
    elif item_type == 'weapons':
        while choice != 'n':
            name = input("Enter weapon name: ")
            damage = int(input("Enter weapon damage: "))
            WEAPONS.append(Weapon(name, damage))
            choice = input("Continue?(y/n)")
        serialize_and_store_list(WEAPONS, "weapons.src")

if __name__ == '__main__':
    main()
