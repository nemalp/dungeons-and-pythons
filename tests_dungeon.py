import unittest
from dungeon import Dungeon
from hero import Hero


class TestDungeon(unittest.TestCase):

    def setUp(self):
        self.d = Dungeon('map.txt')
        self.h = Hero(name="Bron", title="Dragonslayer",
                      health=100, mana=100, mana_regeneration_rate=2)

    def test_print_map(self):
        self.assertEqual(self.d.print_map(), '''S.##.....T
#T##..###.
#.###E###E
#.E...###.
###T#####G''')

    def test_spawn(self):
        self.assertTrue(self.d.spawn(self.h))
        self.assertFalse(Dungeon('map2.txt').spawn(self.h))

if __name__ == '__main__':
    unittest.main()
