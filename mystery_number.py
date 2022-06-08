from random import randint

number_to_find = randint(0, 100)
remaining_attempts = 5

print("*** Le jeu du nombre mystère ***")

#Boucle principale
while remaining_attempts > 0:
  print(f"Il te reste {remaining_attempts} essai{'s' if remaining_attempts > 1 else ''}")

  #Saisie de l'utilisateur
  user_choice = input("Devine le nombre entre 0 et 100 : ")
  if not user_choice.isdigit():
    print("Veuillez entrer un nombre valide.")
    continue

  user_choice = int(user_choice)

  if number_to_find > user_choice: # Plus grand
    print(f"Le nombre mystère est plus grand que {user_choice}")

  elif number_to_find < user_choice: # Plus petit
    print(f"Le nombre mystère est plus petit que {user_choice}")

  else : #Egal (succès)
    break

  remaining_attempts -= 1

#Gagné ou perdu
if remaining_attempts == 0:
  print(f"Dommage ! le nombre mystère était {number_to_find} !")
  print("SPOOOOORT POUR TA RACE")
else:
  print(f"Bravo ! le nombre mystère était bien {number_to_find} !")
  print("MSKIINE LAUTRE VICTIME!! 💖🍕🍕💖")
  print(f"Tu as trouvé le nombre en {6 - remaining_attempts} essai{'s' if remaining_attempts > 2 else ''}")

print("Fin du Jeu.")
