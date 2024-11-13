# RPG Retro Game - Python POO 2024

## Description
Ce projet est un jeu RPG rétro développé en Python, utilisant la programmation orientée objet (POO). Le jeu propose une aventure où le joueur se déplace dans un monde composé de différentes zones, combat des monstres, collecte des objets et peut sauvegarder et charger sa progression (En Cours de développement). Le jeu offre une expérience interactive en ligne de commande avec des éléments de RPG classiques tels que la gestion d'un inventaire, l'acquisition d'XP, et des combats au tour par tour.

## Fonctionnalités
- **Création et gestion de joueur** : Le joueur peut créer un personnage avec un nom et des caractéristiques de base telles que des points de vie (HP), des points d'expérience (XP), et des objets dans l'inventaire.
- **Exploration du monde** : Le joueur peut se déplacer à travers différentes zones du monde, qui sont représentées sous forme de grille.
- **Système de combat** : Le joueur rencontre des monstres aléatoires et peut les combattre au tour par tour. Des boss spéciaux peuvent être rencontrés à la fin du jeu.
- **Collecte d'objets** : Des objets aléatoires (par exemple, potions et armes) peuvent être trouvés et ajoutés à l'inventaire du joueur.
- **Sauvegarde et chargement de jeu** : (En Cours de développement) Le jeu permet de sauvegarder la progression du joueur dans un fichier et de la recharger lors d'une session suivante.
- **Gestion des erreurs** : Le jeu gère diverses erreurs, notamment les erreurs de navigation, les entrées invalides de l'utilisateur, et les exceptions imprévues.

## Installation

1. Clonez ce dépôt sur votre machine locale :

   ```bash
   git clone https://github.com/votre-utilisateur/rpg-retro-game.git
   
2. Lancez le jeu avec la commande suivante :

python main.py

3. Comment jouer

Menu principal :

- 1 : Créer un nouveau jeu.
- 2 : Charger un jeu sauvegardé.
- 3 : Voir les informations sur le jeu.
- 4 : Quitter le jeu.

Commandes pendant le jeu :

- go north / south / east / west : Déplacez-vous dans le monde.
- status : Affichez l'état actuel de votre personnage (HP, XP, inventaire).
- use [item] : Utilisez un objet de votre inventaire (par exemple, "use Health Potion").
- exit : Quittez le jeu.

Structure du code
Le projet est organisé en plusieurs fichiers Python :

- main.py : Fichier principal qui lance le jeu, gère le menu principal et les interactions avec l'utilisateur.
- game.py : Contient la logique principale du jeu, la gestion des menus et des sauvegardes.
- player.py : Définit la classe Player, qui gère les caractéristiques du joueur (HP, XP, inventaire).
- map.py : Définit la classe Map, qui gère la carte du monde et les déplacements du joueur.
- combat.py : Contient la logique de combat, y compris les interactions avec les monstres.
- monster.py : Définit la classe Monster et la classe Boss pour gérer les ennemis.
- item.py : Définit la classe Item pour gérer les objets collectés par le joueur.

Auteurs
Qays/Matthis : Créateur et développeur principal.
