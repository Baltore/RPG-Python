import random

class Monster:
    def __init__(self, name, hp, strength, xp_reward):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.xp_reward = xp_reward

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
        # Le Boss a un nom, des HP, de la force et de l'XP spécifique
        super().__init__("Dark Overlord", 100, 20, 50)  # 50 XP pour le boss final

