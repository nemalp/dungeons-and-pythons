class Weapon:
    def __init__(self, name, damage=0):
        self.name = name
        self.damage = damage


class Spell(Weapon):
    def __init__(self, name, damage, mana_cost, cast_range):
        super.__init__(self, name, damage)
        self.mana_cost = mana_cost
        self.cast_range = cast_range
