# Compréhension de liste

nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = []
for i in nombres:
  if i % 2 == 0:
    nombres_pairs.append(i)
print(nombres_pairs)

nombres_pairs2 = [i for i in nombres if i % 2 == 0]
print(nombres_pairs2)



nombres = range(-10, 10)
nombres_positifs = []
for i in nombres:
  if i >= 0:
    nombres_positifs.append(i)
print(nombres_positifs)

nombres_positifs2 = [i for i in nombres if i >= 0]
print(nombres_positifs2)




nombres = range(5)
nombres_doubles = []
for i in nombres:
  nombres_doubles.append(i*2)
print(nombres_doubles)

nombres_doubles2 = [i*2 for i in nombres]
print(nombres_doubles2)




nombres = range(10)
nombres_inverses = []
for i in nombres:
  if i % 2 == 0:
    nombres_inverses.append(i)
  else:
    nombres_inverses.append(-i)
print(nombres_inverses)

nombres_inverses2 = [i if i % 2 == 0 else -i for i in nombres]
print(nombres_inverses2)




users = ["user"]

for i in range(10):
  users2 = ("\n").join(users) 
  print(f"{users2} {i + 1}")

  for i in range(10):
    print(f"user {i + 1}")

  for i in range(1, 11):
    print(f"user {i}")


mot = "python"

for letter in reversed(mot):
  print(letter)

  # while

  continuer = "o"
  while continuer == "o":
    print("On continue !")
    continuer = input("Voulez vous continuer ? o/n")
  