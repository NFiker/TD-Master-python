# filename =r'C:\Users\ichra/Documents/got.csv'
DOTTED_BREAK_LINE = ('-' * 20)
print(DOTTED_BREAK_LINE)

#------------------ 1/ 2/ 3/ Importation/format got ------------------#

import csv
import numpy as np
import random 
from math import sqrt


got = []
#Lecture base de données got
with open('got.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    count = 0
    for row in csvreader:
        if count > 0 : 
            new_row = []
            str_row = row[0:5]
            float_row = [float(i) for i in row[5:]]
            new_row = [*str_row, *float_row]
            got.append(new_row)



        count += 1 
    #La base de données "got" dispose de toutes les données du csv, on peut travailler avec dorénavant
    #On itère à travers le tableau afin d'obtenir ligne par ligne

    """Exemples attendus"""

    print(f'Premier élément de la base de données: {got[0]}')
    print(f'Expected "Northmen" to be : {got[0][3]}')

print(DOTTED_BREAK_LINE)
#------------------ 4/ Fonction Distance ------------------#

def euclidean_distance (example, neighbour):
    distance = 0
    for i in range(len(example)-1):
               if type(example[i]) == str:
                   if example[i] != neighbour[i]:
                      distance += 1
               else:  
                   distance += (example[i] - neighbour[i])**2
                   distance = sqrt(distance)
    return distance

"""On vérifie que la distance entre Arya et bran Stark est plus petite
que celle entre Arya Stark et Tyrion Lannister"""

#Arya Stark:
print(f'Arya Stark : {got[0]}')

#Bran Stark:
print(f'Bran Stark : {got[2]}')

#Tyrion Lannister: 
print(f'Tyrion Lannister : {got[13]}')


#Distance entre Arya et Bran:
print(f'Distance entre Arya Stark et Bran Stark : {euclidean_distance(got[0],got[2])}')

#Distance entre Arya et Tyrion:
print(f'Distance entre Arya Stark et Tyrion Lannister : {euclidean_distance(got[0],got[13])}')


print(DOTTED_BREAK_LINE)
#------------------ 5/ Distance exemple <> got ------------------#



def euclidean_distance_all(example, got):
        distance2 = []
        for d in got:
            if d != example:
                distance = euclidean_distance(example, d)
                distance2.append(distance)
        return distance2

#Distance entre Arya et toute la base de données got:
# print(euclidean_distance_all(got[0], got)) 


print(DOTTED_BREAK_LINE)
#------------------ 6/ Tri et repérage des indexs ------------------#



#Exemple pour distance entre Arya et toute la base de données:
arya_list = got[0]
arya_distances = euclidean_distance_all(got[0], got)

distance_sorted = sorted(arya_distances) 
# print(f'Distances triées entre Arya et les autres : {distance_sorted}')

indexs_distance_sorted = np.argsort(arya_distances) 
print(f'Indexs des distances triées entre Arya et les autres : {indexs_distance_sorted}')


print(DOTTED_BREAK_LINE)
#------------------ 7/ K plus proches voisins ------------------#

#Dictionnaire pour obtenir une liste d'exemples ordonnés par  distance dans le cas Arya:


def find_class(k, neighbours):   
    isAlive = 0
    for i in range(k):
        isAlive += got[indexs_distance_sorted[i]][14]
    if isAlive > k/2:
        isAlive = 1
    else:
        isAlive = 0
    return isAlive


"""Gadget facultatif: compteur de 'isAlive' pour vérifier la concordance de la prédiction obtenue"""
# Sélectionnez ici le nombre de voisins 'k' pour l'utiliser dynamiquement dans la fonction find_class et la vérification bonus
k = 200
#On crée une liste avec les 'isAlive' de tous les voisins 'k' souhaités.
is_alive_all = []
for i in range(k):
    is_alive_one =got[indexs_distance_sorted[i]][14]
    is_alive_all.append(is_alive_one)

count1 = 0
count0 = 0
for j in range(len(is_alive_all)) :
    if is_alive_all[j] == 1:
        count1 += 1
    else:
        count0 += 1
        
print(f'Le nombre de voisins en vie est de : {count1}')
print(f'Le nombre de voisins morts est de : {count0}')

if count1 > count0:
    print(f'Le nombre de voisins en vie est supérieur donc : ')
    print(f'Prédiction attendue : 1 - Prédiction obtenue : {find_class(k, indexs_distance_sorted)}')
else:
    print(f'Le nombre de voisins en vie est inférieur donc : ')
    print(f'Prédiction attendue : 0 - Prédiction obtenue : {find_class(k, indexs_distance_sorted)}')



print(DOTTED_BREAK_LINE)
#------------------ 8/ Fonction test leave_one_out ------------------#



def leave_one_out(got, k):
    score = 0
    for i in range(len(got)):
        index = random.randint(0, len(got))
        example = got[index]
        got_temp = got
        # got_temp = got_temp.remove(example)
        got_temp = [i for i in got_temp if index != example]
        list_distance = euclidean_distance_all(example, got_temp)
        pred = find_class(k, list_distance)
        if example[14] == pred:
            score += 1
    taux_pred = ((score)/(len(got)) **100)
    return taux_pred


# leave_one_out(got, 60)


print(DOTTED_BREAK_LINE)
#------------------ 9/ Fonction test leave_one_out ------------------#
with open("resultats.txt", "w") as file:
    file.write("Paramètres {i} : ")
