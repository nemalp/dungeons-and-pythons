class Fight:
    def __init__(self, hero, enemy, direction_towards_enemy):
        self.hero = hero
        self.enemy = enemy
        self.direction_towards_enemy = direction_towards_enemy

    def start_fight(self):
        print('A fight is started between our Hero(health={}, mana={}) and Enemey(health={}, mana={}, damage={})'.format(
                                                                                                                         self.hero.health,
                                                                                                                         self.hero.mana,
                                                                                                                         self.enemy.health,
                                                                                                                         self.enemy.mana,
                                                                                                                         self.enemy.damage))
        while self.hero.is_alive() and self.enemy.is_alive():
            if self.enemy.location != self.hero.location:
                self.enemy.take_damage(self.hero.attack('magic'))
                print("Hero casts a {}. Hits enemy for {}. Enemy health is {}".format(self.hero.spell.name,
                                                                                      self.hero.spell.damage,
                                                                                      self.enemy.get_health()))
                if self.enemy.is_alive() is False:
                    print("Enemy is dead")
                    break
                if self.direction_towards_enemy == 'up':
                    self.enemy.location[0] += 1
                    print("Enemy moves one square down in order to get to the hero.")
                elif self.direction_towards_enemy == 'down':
                    self.enemy.location[0] -= 1
                    print("Enemy moves one square up in order to get to the hero.")
                elif self.direction_towards_enemy == 'left':
                    self.enemy.location[1] += 1
                    print("Enemy moves one square right in order to get to the hero.")
                else:
                    self.enemy.location[1] -= 1
                    print("Enemy moves one square left in order to get to the hero.")
            else:
                if self.hero.attack('weapon') < self.hero.attack('magic'):
                    self.enemy.take_damage(self.hero.attack('magic'))
                    print("Hero casts a {}. Hits enemy for {}. Enemy health is {}".format(self.hero.spell.name,
                                                                                          self.hero.spell.damage,
                                                                                          self.enemy.get_health()))
                    if self.enemy.is_alive() is False:
                        print("Enemy is dead")
                        break

                    self.hero.take_damage(self.enemy.attack('weapon'))
                    print("Enemy hits hero for {} damage. Hero health is {}".format(self.enemy.damage,
                                                                                    self.hero.get_health()))
                    if self.hero.is_alive() is False:
                        print("Hero is dead")
                        break
                else:
                    if self.hero.weapon is not None:
                        self.enemy.take_damage(self.hero.attack('weapon'))
                        print("Hero hits with {} for {} dmg. Enemy health is {}".format(self.hero.weapon.name,
                                                                                        self.hero.attack('weapon')))
                    else:
                        if self.hero.can_cast():
                            print("Hero casts a {}. Hits enemy for {}. Enemy health is {}".format(self.hero.spell.name,
                                                                                                  self.hero.spell.damage,
                                                                                                  self.enemy.get_health()))
                        else:
                            print("Hero can not do anything.")

                    if self.enemy.is_alive() is False:
                        print("Enemy is dead")
                        break
                    self.hero.take_damage(self.enemy.attack('weapon'))
                    print("Enemy hits hero for {} damage. Hero health is {}".format(self.enemy.damage,
                                                                                    self.hero.get_health()))
                    if self.hero.is_alive() is False:
                        print("Hero is dead")
                        break
