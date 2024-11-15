import random
from monster import Boss
from monster import Monster
from colorama import Fore, Style, init
import time
import os

# Initialisation de colorama
init(autoreset=True)

class Combat:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def start_fight(self):
        if not isinstance(self.monster, Monster):
            print("Error: The monster is invalid!")
            return False
        
        print(Fore.RED + f"A wild {self.monster.name} appears!" + Style.RESET_ALL)

        while self.player.hp > 0 and self.monster.hp > 0:
            action = self.get_combat_action()

            if action == "attack":
                # Utilisation de la power d'attaque du joueur et de la force du monstre
                damage = random.randint(self.player.attack_power - 2, self.player.attack_power + 2)  # Légère variation autour de l'attaque du joueur
                print(Fore.BLUE + f"You attack and deal {damage} damage to {self.monster.name}." + Style.RESET_ALL)
                self.monster.take_damage(damage)

                if self.monster.hp > 0:
                    # Le monstre attaque avec sa propre force
                    monster_damage = random.randint(self.monster.strength - 2, self.monster.strength + 2)  # Légère variation autour de la force du monstre
                    print(Fore.RED + f"{self.monster.name} attacks and deals {monster_damage} damage!" + Style.RESET_ALL)
                    self.player.take_damage(monster_damage)

                    if self.player.hp <= 0:
                        print(Fore.RED + "You have been defeated!" + Style.RESET_ALL)
                        return  # Quitter la méthode pour éviter de continuer à afficher d'autres messages
            
            elif action == "run":
                print("You run away from the fight!")
                return  # Quitter la méthode car le joueur s'est enfui

            else:
                print("Invalid action. Please choose 'attack' or 'run'.")

        # Victoire ou défaite
        if self.monster.hp <= 0:
            if isinstance(self.monster, Boss):
                print(Fore.YELLOW + "Congratulations! You have defeated the Dark Overlord and escaped the forest!" + Style.RESET_ALL)
                self.player.gain_xp(100)  # XP spécifique pour le boss
                return False
            else:
                xp_gain = self.monster.xp_reward  # Utiliser l'XP de la récompense du monstre
                print(Fore.RED + f"{self.monster.name} has been defeated!" + Style.RESET_ALL)
                self.player.gain_xp(xp_gain)
                print(Fore.YELLOW + f"You gained {xp_gain} XP!" + Style.RESET_ALL)
                time.sleep(6)
                os.system('clear')
        return False


    def get_combat_action(self):
        """Gère la saisie de l'utilisateur et vérifie si l'action est valide."""
        while True:
            action = input("Do you want to attack or run? (attack/run): ").lower().strip()
            if action in ["attack", "run"]:
                return action
            else:
                print("Invalid action. Please choose 'attack' or 'run'.")
