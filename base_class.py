class BaseClass:
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana
        self.max_health = health
        self.equipped_weapon = None
        self.equipped_spell = None

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        if self.health < 1:
            return False
        return True

    def can_cast(self, distance_to_enemy):
        if self.mana >= self.equipped_spell.mana_cost and self.equipped_spell.cast_range >= distance_to_enemy:
            return True
        else:
            return False

    def take_damage(self, damage_points):
        if self.health < damage_points:
            self.health = 0
        else:
            self.health -= damage_points

    def take_healing(self, healing_points):
        if self.is_alive() is False:
            return False
        else:
            if self.health + healing_points > self.max_health:
                self.health = self.max_health
            else:
                self.health += healing_points
        return True

    def equip(self, weapon):
        self.equipped_weapon = weapon

    def learn(self, spell):
        self.equipped_spell = spell

    def attack(self, by=None, enemy):
        if by == 'weapon':
            if self.equipped_weapon:
                enemy.health -= self.equipped_weapon.damage
        if by == 'magic':
            if self.can_cast():
                enemy.health -= self.equipped_spell.damage
