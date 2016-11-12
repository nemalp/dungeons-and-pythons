import unittest
from hero import Hero
from spell_and_weapon import Spell, Weapon


class TestHero(unittest.TestCase):

    def setUp(self):
        self.hero = Hero(name="Bron", title="Dragonslayer",
                         health=100, mana=100, mana_regeneration_rate=2)
        self.hero1 = Hero(name="Bron", title="Dragonslayer",
                          health=0, mana=100, mana_regeneration_rate=2)
        self.spell = Spell(name='Fireball', damage=30,
                           mana_cost=50, cast_range=2)
        self.weapon = Weapon(name="The Axe of Destiny", damage=20)

    def test_known_as(self):
        self.assertEqual(self.hero.known_as(), 'Bron the Dragonslayer')

    def test_get_health(self):
        self.assertEqual(self.hero.get_health(), 100)

    def test_get_mana(self):
        self.assertEqual(self.hero.get_mana(), 100)

    def test_take_mana(self):
        self.hero.learn(self.spell)
        self.hero.take_mana(90)
        self.assertEqual(self.hero.get_mana(), 100)

        self.hero.attack(by='magic')
        self.hero.take_mana(20)
        self.assertEqual(self.hero.get_mana(), 70)

    def test_is_alive(self):
        self.assertTrue(self.hero.is_alive())
        self.assertFalse(self.hero1.is_alive())

    def test_learn_spell(self):
        self.assertFalse(self.hero.spell)
        self.hero.learn(self.spell)
        self.assertTrue(self.hero.spell)

    def test_equip_weapon(self):
        self.hero.equip(self.weapon)
        self.assertTrue(self.hero.weapon)

    def test_can_cast(self):
        self.assertFalse(self.hero.can_cast())
        self.hero.learn(self.spell)
        self.assertTrue(self.hero.can_cast())

    def test_attack(self):
        self.assertEqual(self.hero.attack(by='magic'), 0)
        self.assertEqual(self.hero.attack(by='weapon'), 0)

        self.hero.learn(self.spell)
        self.hero.equip(self.weapon)
        self.assertEqual(self.hero.attack(by='magic'), 30)
        self.assertEqual(self.hero.attack(by='weapon'), 20)


if __name__ == '__main__':
    unittest.main()
