class Map:
    def __init__(self):
        # Représente la carte comme une grille de descriptions de lieux
        self.grid = [
            ["Starting Point", "Forest Path", "Clearing", "River Bank"],
            ["Dense Forest", "Old Cabin", "Open Field", "Mountain Base"],
            ["Dark Cave", "Swamp", "Ruined Tower", "Boss Lair"]
        ]
        self.player_position = (0, 0)  # Position de départ du joueur

    def describe_current_location(self):
        x, y = self.player_position
        location_description = self.grid[x][y]
        print(f"You are at: {location_description}")

    def move_player(self, direction):
        """Déplace le joueur en fonction de la direction spécifiée."""
        x, y = self.player_position

        # Assurez-vous que la direction est bien un des choix valides
        if direction not in ["north", "south", "east", "west"]:
            print("Invalid direction. Please choose 'north', 'south', 'east', or 'west'.")
            return False

        # Déplacement du joueur en fonction de la direction
        if direction == "north" and x > 0:
            self.player_position = (x - 1, y)
        elif direction == "south" and x < len(self.grid) - 1:
            self.player_position = (x + 1, y)
        elif direction == "east" and y < len(self.grid[0]) - 1:
            self.player_position = (x, y + 1)
        elif direction == "west" and y > 0:
            self.player_position = (x, y - 1)
        else:
            print("You can't move in that direction. You may be at the edge of the map.")
            return False

        return True
