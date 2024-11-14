import random

class Monster:
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength

    def attack(self):
        damage = random.randint(1, self.strength)
        return damage

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0

# Ajout d'une classe spécifique pour le boss final
class Boss(Monster):
    def __init__(self):
        super().__init__("Dark Overlord", 100, 20)
