import random
from monster import Boss
from monster import Monster

class Combat:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def start_fight(self):
        # Vérification que le monstre est valide
        if not isinstance(self.monster, Monster):
            print("Error: The monster is invalid!")
            return False
        
        print(f"A wild {self.monster.name} appears!")
        
        while self.player.hp > 0 and self.monster.hp > 0:
            # Affichage des choix d'action
            action = self.get_combat_action()

            if action == "attack":
                damage = random.randint(5, 15)
                print(f"You attack and deal {damage} damage to {self.monster.name}.")
                self.monster.take_damage(damage)
                
                if self.monster.hp > 0:
                    monster_damage = self.monster.attack()
                    self.player.take_damage(monster_damage)
                    
                    if self.player.hp <= 0:
                        print("You have been defeated!")
                        break
            elif action == "run":
                print("You run away from the fight!")
                break
            else:
                print("Invalid action. Please choose 'attack' or 'run'.")
        
        # Vérification de la victoire ou défaite
        if self.monster.hp <= 0:
            if isinstance(self.monster, Boss):
                print("Congratulations! You have defeated the Dark Overlord and escaped the forest!")
                self.player.gain_xp(100)
                print("Game completed successfully.")
                return True
            else:
                xp_gain = 20
                self.player.gain_xp(xp_gain)
                print(f"You have defeated {self.monster.name} and gained {xp_gain} XP!")

        return False  # Retourne False si le joueur n'a pas vaincu le boss

    def get_combat_action(self):
        """Gère la saisie de l'utilisateur et vérifie si l'action est valide."""
        while True:
            action = input("Do you want to attack or run? (attack/run): ").lower().strip()
            if action in ["attack", "run"]:
                return action
            else:
                print("Invalid action. Please choose 'attack' or 'run'.")
