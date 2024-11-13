class Item:
    def __init__(self, name, type, effect):
        self.name = name
        self.type = type  # "potion" ou "weapon"
        self.effect = effect  # Pour une potion, c'est le montant de HP restauré; pour une arme, la puissance d'attaque.

    def use(self, player):
        """Utilise l'objet et applique ses effets sur le joueur."""
        if self.type == "potion":
            if player.hp < 100:  # Vérifie si le joueur peut récupérer des HP
                player.hp += self.effect
                if player.hp > 100:  # Evite que le joueur dépasse les 100 HP max
                    player.hp = 100
                print(f"{player.name} uses {self.name} and restores {self.effect} HP!")
            else:
                print(f"{player.name} is already at full health. {self.name} cannot be used.")

        elif self.type == "weapon":
            print(f"{player.name} equips {self.name}, increasing attack power by {self.effect}.")
            player.attack_power += self.effect  # Augmente la puissance d'attaque du joueur
