# Alexis Gagnon
# 5 novembre 2020

# Programme qui a pour but de garder le premier jour de chaque semaine pour ensuite le comparé aux nouvelles de la semaine précédente
# Récupération d'un total de 5 nombres, mais le code va pouvoir être modifiée pour essayer plusieurs modèles à l'avenir

# librairies
import sys
import numpy
import math

# fichier avec le raw data
d_raw = open("test_label.txt", "r", encoding='UTF-8')

# fichier ou on va écrire le résultat final
d_ref = open("D:/PyCharmProjects/TensorFlow/Projects/FinalProject/DataCollection/_label/test_labels_refined", "w", encoding='UTF-8')

# count
i = 0
nombre_precedent = ""

def premier_jour_de_semaine(day):
    # for month of may
    global nombre_precedent

    if nombre_precedent == "\n":
        print("Premier jour de semaine\n")
        return True
    else:
        print("Pas premier jour de semaine\n")
        return False

for number in d_raw:
    i+=1
    try :
        print("Date: " + str(i))
        number = float(number)
        print("pourcentage" + str(number))
        number = round(number, 2)
        print("pourcentage arrondi: " + str(number))
        if premier_jour_de_semaine(i):
            d_ref.write(str(number) + "\n")
        nombre_precedent = str(number)
    except Exception as e:
        print(e)
        print(number)
        nombre_precedent = str(number)
