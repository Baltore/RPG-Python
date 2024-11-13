from player import Player
from map import Map
from combat import Combat
from monster import Monster
from item import Item
import random
import pickle

class Game:
    def __init__(self):
        self.is_running = True
        self.map = Map()
        self.player = None

    def display_menu(self):
        print("Main Menu :")
        print("1 - Create New Game")
        print("2 - Load Saved Game")
        print("3 - About")
        print("4 - Exit")

    def start_new_game(self):
        self.player = self.create_player()  # Appel de la fonction pour créer un joueur
        print(f"Welcome, {self.player.name}!")
        self.game_loop()

    def save_game(self):
        with open('savegame.pkl', 'wb') as f:
            pickle.dump(self.player, f)
        print("Game has been saved successfully!")

    def load_game(self):
        try:
            with open('savegame.pkl', 'rb') as f:
                self.player = pickle.load(f)
            print("Game loaded successfully! Welcome back, " + self.player.name)
            self.game_loop()
        except FileNotFoundError:
            print("No saved game found. Please start a new game.")

    def show_about(self):
        print("RPG Retro Game - Projet Python POO 2024")
        print("Créé par Qays/Matthis")

    def exit_game(self):
        self.is_running = False
        print("Exiting the game...")

    def create_player(self):
        while True:
            name = input("Please enter your name: ").strip()
            if name:  # Vérifie si le nom n'est pas vide
                return Player(name)
            else:
                print("Name cannot be empty. Please try again.")

    def get_direction(self):
        valid_directions = ["go north", "go south", "go east", "go west"]
        while True:
            direction = input("Which direction would you like to go? ").lower().strip()
            if direction in valid_directions:
                return direction
            else:
                print("Invalid direction. Please choose 'Go North', 'Go South', 'Go East', or 'Go West'.")

    def game_loop(self):
        try:
            while self.player.hp > 0:
                self.map.describe_current_location()

                # Chance aléatoire de trouver un objet (par exemple, 20%)
                if random.randint(1, 100) <= 20:
                    item = self.generate_random_item()
                    self.player.add_item(item)

                # Chance aléatoire de rencontrer un monstre (30%)
                if random.randint(1, 100) <= 30:
                    monster = Monster("Goblin", 30, 10)  # Exemple de monstre
                    combat = Combat(self.player, monster)
                    combat.start_fight()

                    if self.player.hp <= 0:
                        break

                command = input("Enter a command (go north, go south, go east, go west, status, use [item], exit): ").lower()
                if command.startswith("go "):
                    direction = command.split(" ")[1]
                    if self.map.move_player(direction):
                        print(f"You move {direction}.")
                    else:
                        print("You can't move in that direction.")
                elif command == "status":
                    self.player.show_status()
                elif command.startswith("use "):
                    item_name = command.split(" ", 1)[1]
                    self.player.use_item(item_name)
                elif command == "exit":
                    print("Exiting the game...")
                    break
                else:
                    print("Invalid command. Try 'go north', 'go south', 'status', 'use [item]', etc.")

            print("Game over. Returning to the main menu.")
        except Exception as e:
            print(f"An error occurred during the game: {e}")
            print("Returning to the main menu.")

    def generate_random_item(self):
        item_types = [
            Item("Health Potion", "potion", 30),
            Item("Small Sword", "weapon", 5)
        ]
        return random.choice(item_types)

    def run(self):
        try:
            while self.is_running:
                self.display_menu()
                choice = input("> ")
                if choice == "1":
                    self.start_new_game()
                elif choice == "2":
                    self.load_game()
                elif choice == "3":
                    self.show_about()
                elif choice == "4":
                    self.exit_game()
                else:
                    print("Invalid choice, please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Exiting the game.")
