from helper_functions import check_for_enemies_in_cast_range

class Hero:

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.max_health = health
        self.mana = mana
        self.max_mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.location = None
        self.spell = None
        self.weapon = None
        self.map_ = None

    def known_as(self):
        return '{0} the {1}'.format(self.name, self.title)

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_mana(self, mana_points):
        if self.mana + mana_points > self.max_mana:
            self.mana = self.max_mana
        else:
            self.mana += mana_points


    def take_healing(self, healing_points):
        if not self.is_alive():
            return False

        if self.health + healing_points > self.max_health:
            self.health = self.max_health
        else:
            self.health += healing_points

        return True


    def take_damage(self, damage):
        if self.is_alive is False:
            return False
        if damage > self.health:
            self.health = 0
        else:
            self.health -= damage

    def is_alive(self):
        return self.health > 0

    def can_cast(self):
        if self.spell:
            if self.spell.cast_range > 0 and \
                    self.spell.mana_cost <= self.get_mana():
                return True
        return False

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def attack(self, by=None):
        if by == 'magic' and self.can_cast():
            if self.mana - self.spell.mana_cost < 0:
                self.mana = 0
            else:
                self.mana -= self.spell.mana_cost

            return self.spell.damage

        if by == 'weapon' and self.weapon:
            return self.weapon.damage

        return 0
