from hero import Hero
from dungeon import Dungeon
from helper_functions import load_map, check_for_enemies_in_cast_range
from pprint import pprint
from weapon_and_spell_classes import Spell

def main():
    hero = Hero("Ime", "Titla", 100, 100, 10)
    dungeon = Dungeon()
    print(dungeon.print_map())
    dungeon.spawn(hero)
    print(dungeon.print_map())
    dungeon.move_hero(hero, 'right')
    print(dungeon.print_map())
    dungeon.move_hero(hero, 'down')
    print(dungeon.print_map())
    if hero.weapon is not None:
        print(hero.weapon.name)
        print(hero.weapon.damage)
    if hero.spell is not None:
        print(hero.spell.name)
        print(hero.spell.damage)
    print(hero.get_health())
    print(hero.get_mana())
    dungeon.move_hero(hero, "down")
    dungeon.move_hero(hero, "down")
    print(dungeon.print_map())
    dungeon.move_hero(hero, 'right')
    dungeon.move_hero(hero, 'right')

if __name__ == '__main__':
    main()
