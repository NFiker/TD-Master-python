from random import randint

ENNEMY_HEALTH = 50
PLAYER_HEALTH = 50
NUMBER_OF_POTIONS = 3
TURN = 0
SKIP_TURN = False

RESET = '\033[0m' #RESET COLOR
CONGRATULATIONS = '\033[92m' + "CONGRATULATIONS" + RESET #GREEN
TURN_DISPLAY = f"'\033[93m' + 'Tour' {TURN} + {RESET})"  #YELLOW
GAME_OVER = '\033[91m' + "GAME OVER" + RESET #RED

while True:
  TURN += 1
  print("\n")
  print(f" {'-' * 25 } Tour {TURN} {'-' * 25}")

  #Jeu du joueur
  if  SKIP_TURN:
    print("Vous passez votre tour...")
    SKIP_TURN = False
  else:
    user_choice = ""
    while user_choice not in ["1", "2"]:
      user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
    
    print("-" * 20)

    if user_choice == "1": # Attaque
      your_attack = randint(5, 10)
      ENNEMY_HEALTH -= your_attack
      print(f"Vous avez infligé {your_attack} points de dégats à l'ennemi ⚔")

    elif user_choice == "2":
      if NUMBER_OF_POTIONS > 0:
        potion_health = randint(15, 50)
        PLAYER_HEALTH += potion_health
        NUMBER_OF_POTIONS -= 1
        SKIP_TURN = True
        print(f"Vous récupérez {potion_health} points de vie 🧡 ({NUMBER_OF_POTIONS} 🧪 restantes)")
      else:
        print("Vous n'avez plus de potions...")
        continue

    if ENNEMY_HEALTH <= 0:
      print("\n")
      print(f" {'-' * 25 } {CONGRATULATIONS} {'-' * 25}")
      print("Tu as gagné champiooon 😎")
      break

    # Attaque de l'ennemi
    ennemy_attack = randint(5, 15)
    PLAYER_HEALTH -= ennemy_attack
    print(f"L'ennemi vous a infligé {ennemy_attack} points de dégats ⚔")

    if PLAYER_HEALTH <= 0:
      print("\n")
      print(f" {'-' * 25 } {GAME_OVER} {'-' * 25}")
      print("Tu as perdu ! 😿")
      break

    print("-" * 20)
    
    print(f"Il vous reste {PLAYER_HEALTH} point{'s' if PLAYER_HEALTH > 1 else ''} de vie.")
    print(f"Il reste {ENNEMY_HEALTH} point{'s' if ENNEMY_HEALTH > 1 else ''} de vie à l'ennemi.")

print (f"Le combat s'est terminé en {TURN} tours")
print("Fin du jeu.")




