from base_class import BaseClass


class Enemy(BaseClass):

    def __init__(self, health, mana, damage):
        super.__init__(self, health, mana)
        self.damage = damage

    def attack(self, hero, by=None):
        if by == 'weapon':
            if self.equipped_weapon:
                hero.health -= self.equipped_weapon
        if by == 'magic':
            if self.can_cast():
                hero.health -= self.equipped_spell.damage
