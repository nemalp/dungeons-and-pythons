from base_class import BaseClass


class Hero(BaseClass):
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        super.__init__(self, health, mana)
        self.name = name
        self. title = title
        self.mana_regeneration_rate = mana_regeneration_rate
        self.max_mana = mana
        self.location = None

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def take_mana(self, mana_points):
        if self.mana + mana_points > self.max_mana:
            self.mana = self.max_mana
        else:
            self.mana += mana_points
