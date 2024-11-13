class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100  # HP max par défaut
        self.xp = 0
        self.attack_power = 10  # Attaque de base du joueur
        self.inventory = []  # L'inventaire commence vide

    def show_status(self):
        """Affiche les informations du joueur."""
        print(f"Name: {self.name}")
        print(f"HP: {self.hp}")
        print(f"XP: {self.xp}")
        print(f"Attack Power: {self.attack_power}")
        print(f"Inventory: {', '.join([item.name for item in self.inventory]) if self.inventory else 'None'}")

    def take_damage(self, damage):
        """Le joueur prend des dégâts."""
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            print("You have been defeated!")

    def gain_xp(self, amount):
        """Le joueur gagne de l'expérience."""
        self.xp += amount
        print(f"You gained {amount} XP!")

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
