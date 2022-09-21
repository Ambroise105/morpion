#Fonction qui vérifie si le joueur 1 a gagné
from os import remove


def victoire_joueur1():

    if "A1" and "A2" and "A3" in liste_coup_joueur1:      #A1 & A2 & A3
        print("Victory")

    elif "B1" and "B2" and "B3" in liste_coup_joueur1:    #B1 & B2 & B3
        print("Victory")

    elif "C1" and "C2" and "C3" in liste_coup_joueur1:    #C1 & C2 & C3
        print("Victory")
        
    elif "A1" and "B1" and "C1" in liste_coup_joueur1:    #A1 & B1 & C1
        print("Victory")

    elif "A2" and "B2" and "C2" in liste_coup_joueur1:    #A2 & B2 & C2
        print("Victory")

    elif "A3" and "B3" and "C3" in liste_coup_joueur1:    #A3 & B3 & C3
        print("Victory")

    elif "A1" and "B2" and "C3" in liste_coup_joueur1:    #A1 & B2 & C3
        print("Victory")

    elif "A3" and "B2" and "C1" in liste_coup_joueur1:    #A3 & B2 & C1
        print("Victory")
    else:
        print("Oups")


#Fonction qui vérifie si le joueur 2 a gagné
def victoire_joueur2():

    if "A1" and "A2" and "A3" in liste_coup_joueur2:      #A1 & A2 & A3
        print("Victory")

    elif "B1" and "B2" and "B3" in liste_coup_joueur2:    #B1 & B2 & B3
        print("Victory")

    elif "C1" and "C2" and "C3" in liste_coup_joueur2:    #C1 & C2 & C3
        print("Victory")
        
    elif "A1" and "B1" and "C1" in liste_coup_joueur2:    #A1 & B1 & C1
        print("Victory")

    elif "A2" and "B2" and "C2" in liste_coup_joueur2:    #A2 & B2 & C2
        print("Victory")

    elif "A3" and "B3" and "C3" in liste_coup_joueur2:    #A3 & B3 & C3
        print("Victory")

    elif "A1" and "B2" and "C3" in liste_coup_joueur2:    #A1 & B2 & C3
        print("Victory")

    elif "A3" and "B2" and "C1" in liste_coup_joueur2:    #A3 & B2 & C1
        print("Victory")
    else:
        print("Oups")

case = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]

liste_coup_disponible = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
liste_coup_joueur1 = []
liste_coup_joueur2 = []

A1="1"
B1="2"
C1="3"
A2="4"
B2="5"
C2="6"
A3="7"
B3="8"
C3="9"
print(" ###################\n","#     #     #     #\n","# ",A1," # ",B1," # ",C1," #\n","#     #     #     #\n","###################\n","#     #     #     #\n","# ",A2," # ",B2," # ",C2," #\n","#     #     #     #\n","###################\n","#     #     #     #\n","# ",A3," # ",B3," # ",C3," #\n","#     #     #     #\n","###################")

liste_coup_disponible.remove(test)
liste_coup_joueur1.append(test)

print(liste_coup_disponible)
print(liste_coup_joueur1)


while True:

    while True:

        coup_joueur1 = int(input("(Joueur 1) Quel case voulez jouer ?"))


        if coup_joueur1 in liste_coup_disponible:
            liste_coup_joueur1.append
            liste_coup_disponible.remove



    coup_joueur2 = int(input("(Joueur 2) Quel case voulez jouer ?"))#Fonction qui vérifie si le joueur 1 a gagné
from os import remove


def victoire_joueur1():

    if "A1" and "A2" and "A3" in liste_coup_joueur1:      #A1 & A2 & A3
        print("Victory")

    elif "B1" and "B2" and "B3" in liste_coup_joueur1:    #B1 & B2 & B3
        print("Victory")

    elif "C1" and "C2" and "C3" in liste_coup_joueur1:    #C1 & C2 & C3
        print("Victory")
        
    elif "A1" and "B1" and "C1" in liste_coup_joueur1:    #A1 & B1 & C1
        print("Victory")

    elif "A2" and "B2" and "C2" in liste_coup_joueur1:    #A2 & B2 & C2
        print("Victory")

    elif "A3" and "B3" and "C3" in liste_coup_joueur1:    #A3 & B3 & C3
        print("Victory")

    elif "A1" and "B2" and "C3" in liste_coup_joueur1:    #A1 & B2 & C3
        print("Victory")

    elif "A3" and "B2" and "C1" in liste_coup_joueur1:    #A3 & B2 & C1
        print("Victory")
    else:
        print("Oups")


#Fonction qui vérifie si le joueur 2 a gagné
def victoire_joueur2():

    if "A1" and "A2" and "A3" in liste_coup_joueur2:      #A1 & A2 & A3
        print("Victory")

    elif "B1" and "B2" and "B3" in liste_coup_joueur2:    #B1 & B2 & B3
        print("Victory")

    elif "C1" and "C2" and "C3" in liste_coup_joueur2:    #C1 & C2 & C3
        print("Victory")
        
    elif "A1" and "B1" and "C1" in liste_coup_joueur2:    #A1 & B1 & C1
        print("Victory")

    elif "A2" and "B2" and "C2" in liste_coup_joueur2:    #A2 & B2 & C2
        print("Victory")

    elif "A3" and "B3" and "C3" in liste_coup_joueur2:    #A3 & B3 & C3
        print("Victory")

    elif "A1" and "B2" and "C3" in liste_coup_joueur2:    #A1 & B2 & C3
        print("Victory")

    elif "A3" and "B2" and "C1" in liste_coup_joueur2:    #A3 & B2 & C1
        print("Victory")
    else:
        print("Oups")

case = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]

liste_coup_disponible = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
liste_coup_joueur1 = []
liste_coup_joueur2 = []

test = "A3"

liste_coup_disponible.remove(test)
liste_coup_joueur1.append(test)

print(liste_coup_disponible)
print(liste_coup_joueur1)


while True:

    while True:

        coup_joueur1 = int(input("(Joueur 1) Quel case voulez jouer ?"))


        if coup_joueur1 in liste_coup_disponible:
            liste_coup_joueur1.append
            liste_coup_disponible.remove



    coup_joueur2 = int(input("(Joueur 2) Quel case voulez jouer ?"))