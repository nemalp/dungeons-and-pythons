from helpers import load_map


class Dungeon:

    def __init__(self, map_):
        self.map_ = load_map(map_)

    def print_map(self):
        return '\n'.join([''.join(x) for x in self.map_])

    def spawn(self, hero):
        spawning_point_found = False

        for row in range(len(self.map_)):
            for col in range(len(self.map_[row])):
                if self.map_[row][col] == 'S':
                    self.map_[row][col] = 'H'
                    hero.location = (row, col)
                    spawning_point_found = True
                    break

        return spawning_point_found
