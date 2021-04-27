# Alexis Gagnon
# 7 novembre 2020

#Programme organisant le data pour le mettre en ordre

# librairies
import sys
import numpy
import math

# fichier avec le raw data
d_raw = open("../_data/test_data", "r", encoding='UTF-8')

# fichier ou on va écrire le résultat final
d_ref = open("test_data_refined", "w", encoding='UTF-8')

#def semaine_pour_jour(day):
    # pour mois de may

for news in d_raw:
    for i in news:
        if i == "[":
            print(i + " has been removed")
        elif i == "]":
            print(i + " has been removed")
        elif i == "'":
            print(i + " has been removed")
        elif i == "@":
            print(i + " has been removed")
        elif i == ":":
            print(i + " has been removed")
        elif i == "…":
            print(i + " has been removed")
        elif i == "#":
            print(i + " has been removed")
        elif i == ".":
            print(i + " has been removed")
        elif i == "(":
            print(i + " has been removed")
        elif i == ")":
            print(i + " has been removed")
        elif i == "”":
            print(i + " has been removed")
        elif i == "“":
            print(i + " has been removed")
        elif i == ",":
            print(i + " has been removed")
        elif i == "/":
            print(i + " has been removed")
        elif i == "amd":
            print(i + " has been removed")
        elif i == "AMD":
            print(i + " has been removed")
        else :
            d_ref.write(i)

    print("news: " + news)