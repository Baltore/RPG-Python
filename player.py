from colorama import Fore, Style, init

# Initialisation de colorama
init(autoreset=True)

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100  # HP max par défaut
        self.xp = 0
        self.attack_power = 10  # Attaque de base du joueur
        self.level = 1  # Le niveau du joueur
        self.max_hp = 100  # HP max initial
        self.inventory = []  # L'inventaire commence vide

    def show_status(self):
        """Affiche les informations du joueur."""
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"XP: {self.xp}")
        print(f"Attack Power: {self.attack_power}")
        print(f"Inventory: {', '.join([item.name for item in self.inventory]) if self.inventory else 'None'}")

    def take_damage(self, damage):
        """Le joueur prend des dégâts."""
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0

    def gain_xp(self, amount):
        """Le joueur gagne de l'expérience et vérifie s'il passe au niveau supérieur."""
        self.xp += amount
        self.check_level_up()

    def check_level_up(self):
        """Vérifie si le joueur doit passer au niveau suivant."""
        level_thresholds = {2: 50, 3: 75}  # Seuils d'XP pour les niveaux 2 et 3
        if self.level < 3 and self.xp >= level_thresholds.get(self.level + 1, float('inf')):
            self.level += 1
            self.attack_power += 5  # Augmenter la puissance d'attaque
            self.max_hp += 50  # Augmenter les HP max
            self.hp = self.max_hp  # Restaurer les HP max
            self.xp = 0  # Réinitialiser l'XP après avoir passé un niveau
            print(f"{Fore.YELLOW}{self.name} has reached level {self.level}!")
            print(f"{Fore.YELLOW}Attack Power increased to {self.attack_power} and HP increased to {self.hp}/{self.max_hp}.")
        elif self.level == 3 and self.xp >= 150:  # Après le niveau 3, le joueur atteint le niveau max
            print(f"{self.name} has reached the maximum level!")

    def add_item(self, item):
        """Ajoute un objet à l'inventaire du joueur."""
        self.inventory.append(item)
        print(f"{item.name} has been added to your inventory.")
    
    def use_item(self, item_name):
        """Permet au joueur d'utiliser un objet de son inventaire."""
        item_found = False
        for item in self.inventory:
            if item.name.lower() == item_name.lower():  # Recherche insensible à la casse
                if hasattr(item, 'use'):  # Vérifie si l'objet a la méthode 'use'
                    item.use(self)  # Utilise l'objet
                    self.inventory.remove(item)  # Retire l'objet de l'inventaire après l'utilisation
                    item_found = True
                else:
                    print(f"{item_name} cannot be used.")
                break
        
        if not item_found:
            print(f"{self.name} does not have a {item_name} in their inventory.")
