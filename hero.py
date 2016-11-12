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
            # TODO check if there is a enemy in the given cast range
            # if there is, start a fight
            if self.spell.mana_cost <= self.mana:
                self.mana -= self.spell.mana_cost

            return self.spell.damage

        if by == 'weapon' and self.weapon:
            return self.weapon.damage

        return 0

    def take_damage(self, damage_points):
        if damage_points > self.health:
            self.health = 0
        else:
            self.health -= damage_points
