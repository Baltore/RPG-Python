from player import Player
from map import Map
from combat import Combat
from monster import Monster
from monster import Boss
from item import Item
import random
import pickle
import time
import os
from colorama import Fore, Style, init

# Initialisation de colorama
init(autoreset=True)

class Game:
    def __init__(self):
        self.is_running = True
        self.map = Map()
        self.player = None

    def clear_console(self):
        """Efface la console."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_with_delay(self, text, delay=4):
        """Affiche le texte et le laisse à l'écran pendant un certain temps."""
        print(text)
        time.sleep(delay)
        self.clear_console()

    def display_menu(self):
        self.clear_console()
        print(Fore.YELLOW + Style.BRIGHT + "Main Menu :")
        print() 
        print("1 - Create New Game")
        print("2 - Load Saved Game")
        print("3 - About")
        print("4 - Exit")
        print() 

    def start_new_game(self):
        self.clear_console()
        self.player = self.create_player()
        print(f"{Fore.GREEN}{Style.BRIGHT}Welcome, {self.player.name}!")
        print()
        self.print_with_delay(f"{Style.BRIGHT}{Fore.GREEN}..." + Style.RESET_ALL)
        self.game_loop()

    # Méthode pour sauvegarder l'état du jeu dans la classe Game
    def save_game(self, filename="savegame.pkl"):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self.player, file)
            print(Fore.GREEN + "Game saved successfully!")
            self.print_with_delay("...")
        except Exception as e:
            print(Fore.RED + f"An error occurred while saving the game: {e}")
            self.print_with_delay("...")

        # Méthode pour charger l'état du jeu
    def load_game(self, filename="savegame.pkl"):
        try:
            with open(filename, 'rb') as file:
                self.player = pickle.load(file)
            print("Game loaded successfully!")
            self.print_with_delay("...")
            return True  # Indiquer que le chargement a réussi
        except FileNotFoundError:
            print("No save file found.")
            self.print_with_delay("...")
            return False  # Indiquer que le chargement a échoué
        except Exception as e:
            print(Fore.RED + f"An error occurred while loading the game: {e}")
            self.print_with_delay("...")
            return False


    def show_about(self):
        self.clear_console()
        print(Fore.CYAN + "RPG Retro Game - Projet Python POO 2024")
        print("Créé par Qays/Matthis")
        self.print_with_delay("...")

    def exit_game(self):
        self.is_running = False
        print(Fore.RED + "Exiting the game...")
        self.print_with_delay("...")

    def create_player(self):
        while True:
            name = input("Please enter your name: ").strip()
            if name:
                return Player(name)
            else:
                print(Fore.RED + "Name cannot be empty. Please try again.")
    
    def get_direction(self):
        valid_directions = ["go north", "go south", "go east", "go west"]
        while True:
            direction = input(Fore.GREEN + "Which direction would you like to go? ").lower().strip()
            if direction in valid_directions:
                return direction
            else:
                print(Fore.RED + "Invalid direction. Please choose 'Go North', 'Go South', 'Go East', or 'Go West'.")

    def game_loop(self):
        try:
            while self.player.hp > 0:
                self.map.describe_current_location()

                # Demander à l'utilisateur la direction
                command = input(Fore.CYAN + "Enter a command (go north, go south, go east, go west, status, use [item], save, exit): ").lower()

                # Vérifier si la commande commence par "go" pour récupérer la direction
                if command.startswith("go "):
                    direction = command.split(" ")[1]  # Extraire la direction

                    # Déplacer le joueur en fonction de la direction
                    if self.map.move_player(direction):
                        print(Fore.GREEN + f"You move {direction}.")
                    else:
                        print(Fore.RED + "You can't move in that direction.")
                    self.print_with_delay("...")

                elif command == "status":
                    self.player.show_status()
                    self.print_with_delay("...")
                elif command.startswith("use "):
                    item_name = command.split(" ", 1)[1]
                    self.player.use_item(item_name)
                    self.print_with_delay("...")
                elif command == "save":
                    self.save_game()
                    self.print_with_delay("Game has been saved successfully!")
                elif command == "exit":
                    print(Fore.RED + "Exiting the game...")
                    self.print_with_delay("...")
                    break
                else:
                    print(Fore.RED + "Invalid command. Try 'go north', 'go south', 'go east', 'go west', 'status', 'use [item]', etc.")
                    self.print_with_delay("...")

                # Si le joueur atteint le "Boss Lair", un boss apparaît
                if self.map.player_position == (2, 3):  # Check pour la position "Boss Lair"
                    boss = Boss()  # Créer un boss uniquement dans le Boss Lair
                    print(Fore.MAGENTA + f"A wild {boss.name} appears at the Boss Lair!")
                    self.print_with_delay("...")
                    combat = Combat(self.player, boss)
                    combat.start_fight()

                    # Vérifier si le joueur a vaincu le boss
                    if self.player.hp > 0:  # Le joueur a gagné
                        print(Fore.GREEN + "You have defeated the Dark Overlord!")
                        self.print_with_delay("...")

                        # Affichage de l'histoire du personnage et de ses exploits
                        story_text = f"""
                        After an arduous journey, you, the hero of the village, 
                        defeated the Dark Overlord, bringing peace to the land.
                        Your courage, resilience, and quick thinking were the keys to 
                        overcoming the darkest of foes. The villagers will remember you 
                        as the one who saved them from certain doom.

                        You have proven yourself not only as a great warrior but also as 
                        a true protector of the people. With the Overlord defeated, the 
                        village is safe, and your name will be forever etched in history.

                        You are a legend {self.player.name}.
                        """

                        print(Fore.YELLOW + story_text)
                        self.print_with_delay("...", delay=30)  # Afficher le texte pendant 30 secondes
                        
                        # Après l'affichage du message de victoire, revenir au menu
                        self.display_menu()  # Retourne au menu principal
                        return  # Quitte la boucle du game_loop et retourne au menu

                # Vérifier si le joueur n'est pas au "Small Village"
                if self.map.player_position != (0, 0):
                    # Génération d'un monstre aléatoire mais sans inclure le boss
                    if self.map.player_position != (2, 3) and random.randint(1, 100) <= 30:  # Pas de boss dans la zone aléatoire
                        # Définition des monstres possibles avec leur taux de spawn et XP
                        monsters = [
                            Monster("Goblin", 30, 10, 20),  # Goblin, 30% de chance, 20 XP
                            Monster("Slime", 15, 3, 7),     # Slime, 50% de chance, 7 XP
                            Monster("Skeleton", 25, 15, 20) # Squelette, 30% de chance, 20 XP
                        ]

                        # Liste des monstres pondérée par leur taux de spawn
                        weighted_monsters = [
                            monster for monster in monsters for _ in range(30 if monster.name == "Goblin" else 50 if monster.name == "Slime" else 30)
                        ]

                        # Choix aléatoire d'un monstre parmi la liste pondérée
                        chosen_monster = random.choice(weighted_monsters)

                        print(Fore.MAGENTA + f"A wild {chosen_monster.name} appears!")
                        self.print_with_delay("...")
                        combat = Combat(self.player, chosen_monster)
                        combat.start_fight()

                        if self.player.hp <= 0:  # Si le joueur est mort, on arrête
                            break



                    # Générer un item aléatoire à certains moments
                    if random.randint(1, 100) <= 20:  # 20% de chance d'apparition d'un objet
                        item = self.generate_random_item()
                        print(Fore.YELLOW + f"You found a {item.name}!")
                        command = input(Fore.GREEN + f"Do you want to pick up the {item.name}? (yes/no): ").lower()

                        if command == "yes":
                            self.player.add_item(item)  # Ajoute l'objet à l'inventaire
                            print(Fore.GREEN + f"You picked up the {item.name}.")
                            self.print_with_delay("...")
                        else:
                            print(Fore.RED + "You left the item behind.")
                            self.print_with_delay("...")
                else:
                    print(Fore.GREEN + "You are safe in the Small Village. No monsters or items here.")
                    self.print_with_delay("...")


            # Si le joueur est défait, afficher "Game Over" et revenir au menu
            print(Fore.RED + "Game over. Returning to the main menu.")
            self.print_with_delay("...")
            self.display_menu()  # Retourne au menu principal
        except Exception as e:
            print(Fore.RED + f"An error occurred during the game: {e}")
            print(Fore.RED + "Returning to the main menu.")
            self.print_with_delay("...")
            self.display_menu()  # Retourne au menu principal


    def generate_random_item(self):
        # Liste d'items avec un poids plus élevé pour les objets plus communs
        item_types = [
            Item("Small Potion", "potion", 15),  # 30% de chance
            Item("Big Potion", "potion", 30),    # 15% de chance
            Item("Sword", "weapon", 10),         # 30% de chance
            Item("Dark Sword", "weapon", 30)     # 10% de chance
        ]
        
        # Donne des poids différents pour chaque objet
        weights = [30, 15, 30, 10]  # Les probabilités sont exprimées en pourcentages

        # Choisir un item en fonction des poids
        chosen_item = random.choices(item_types, weights=weights, k=1)[0]
        return chosen_item

    def run(self):
        try:
            while self.is_running:
                self.display_menu()
                choice = input(Fore.YELLOW + "> " + Style.RESET_ALL)
                if choice == "1":
                    self.clear_console()
                    self.start_new_game()
                elif choice == "2":
                    self.clear_console()
                    if self.load_game():
                        print(Fore.GREEN + "Welcome back, " + self.player.name + "!")
                        self.game_loop()  # Lancer la boucle de jeu après le chargement réussi
                    else:
                        print(Fore.RED + "Failed to load the game. Returning to the main menu.")
                        self.print_with_delay("...")
                elif choice == "3":
                    self.clear_console()
                    self.show_about()
                elif choice == "4":
                    self.clear_console()
                    self.exit_game()
                else:
                    print(Fore.RED + "Invalid choice, please try again.")
                    self.print_with_delay("...")
        except Exception as e:
            print(Fore.RED + f"An unexpected error occurred: {e}")
            print(Fore.RED + "Exiting the game.")
            self.print_with_delay("...")
