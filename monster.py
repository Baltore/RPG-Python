import random

class Monster:
    def __init__(self, name, hp, strength):
        self.name = name
        self.hp = hp
        self.strength = strength

    def attack(self):
        damage = random.randint(1, self.strength)
        print(f"{self.name} attacks and deals {damage} damage!")
        return damage

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} has {self.hp} HP left.")

# Ajout d'une classe spécifique pour le boss final
class Boss(Monster):
    def __init__(self):
        super().__init__("Dark Overlord", 100, 20)
