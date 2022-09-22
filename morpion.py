from os import remove


def victoire_joueur1(test):
    """Vérifie si le joueur 1 a gagné"""

    if "A1" in test and "A2" in test and "A3" in test:      #A1 & A2 & A3
        return True

    elif "B1" in test and "B2" in test and "B3" in test:    #B1 & B2 & B3
        return True

    elif "C1" in test and "C2" in test and "C3" in test:    #C1 & C2 & C3
        return True
        
    elif "A1" in test and "B1" in test and "C1" in test:    #A1 & B1 & C1
        return True

    elif "A2" in test and "B2" in test and "C2" in test:    #A2 & B2 & C2
        return True

    elif "A3" in test and "B3" in test and "C3" in test:    #A3 & B3 & C3
        return True

    elif "A1" in test and "B2" in test and "C3" in test:    #A1 & B2 & C3
        return True

    elif "A3" in test and "B2" in test and "C1" in test:    #A3 & B2 & C1
        return True
    
    else:
        return False


def victoire_joueur2(test):
    """Vérifie si le joueur 2 a gagné"""

    if "A1" in test and "A2" in test and "A3" in test:      #A1 & A2 & A3
        return True

    elif "B1" in test and "B2" in test and "B3" in test:    #B1 & B2 & B3
        return True

    elif "C1" in test and "C2" in test and "C3" in test:    #C1 & C2 & C3
        return True
        
    elif "A1" in test and "B1" in test and "C1" in test:    #A1 & B1 & C1
        return True

    elif "A2" in test and "B2" in test and "C2" in test:    #A2 & B2 & C2
        return True

    elif "A3" in test and "B3" in test and "C3" in test:    #A3 & B3 & C3
        return True

    elif "A1" in test and "B2" in test and "C3" in test:    #A1 & B2 & C3
        return True

    elif "A3" in test and "B2" in test and "C1" in test:    #A3 & B2 & C1
        return True
    else:
        return False


dicotouche = {
    1:"A1",
    2:"B1",
    3:"C1",
    4:"A2",
    5:"B2",
    6:"C2",
    7:"A3",
    8:"B3",
    9:"C3",
}

def coupcase(coup_joueur):
    if coup_joueur > 0 and coup_joueur < 10:
        coup_joueur = dicotouche[coup_joueur]
        return coup_joueur
    else:
        return False




liste_coup_disponible = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
liste_coup_joueur1 = []
liste_coup_joueur2 = []

dicoprint = {
"PA1":"1",
"PB1":"2",
"PC1":"3",
"PA2":"4",
"PB2":"5",
"PC2":"6",
"PA3":"7",
"PB3":"8",
"PC3":"9",
}

def affichageXouO(cellule) :
    if cellule in liste_coup_joueur1:
        cellule="X"
    if cellule in liste_coup_joueur2:
        cellule="O"
        

while True:

    while True:

        print(" ##### JOUEUR1 #####\n","#     #     #     #\n","# ",dicoprint["PA1"]," # ",dicoprint["PB1"]," # ",dicoprint["PC1"]," #\n","#     #     #     #\n","###################\n","#     #     #     #\n","# ",dicoprint["PA2"]," # ",dicoprint["PB2"]," # ",dicoprint["PC2"]," #\n","#     #     #     #\n","###################\n","#     #     #     #\n","# ",dicoprint["PA3"]," # ",dicoprint["PB3"]," # ",dicoprint["PC3"]," #\n","#     #     #     #\n","###################")

        coup_joueur1 = int(input("(Joueur 1) Quel case voulez-vous jouer ? "))
        coup_joueur1_defini = coupcase(coup_joueur1)



        if coup_joueur1_defini in liste_coup_disponible:
            liste_coup_joueur1.append(coup_joueur1_defini)
            liste_coup_disponible.remove(coup_joueur1_defini)
            affichageXouO(coup_joueur1_defini)
            break

        else:
            print("Réessayez")

    print(liste_coup_joueur1)
    if victoire_joueur1(liste_coup_joueur1):
        print("Félicitations Joueur 1, vous avez gagné")
        break

    
    while True:

        print(" ##### JOUEUR2 #####\n","#     #     #     #\n","# ",dicoprint["PA1"]," # ",dicoprint["PB1"]," # ",dicoprint["PC1"]," #\n","#     #     #     #\n","###################\n","#     #     #     #\n","# ",dicoprint["PA2"]," # ",dicoprint["PB2"]," # ",dicoprint["PC2"]," #\n","#     #     #     #\n","###################\n","#     #     #     #\n","# ",dicoprint["PA3"]," # ",dicoprint["PB3"]," # ",dicoprint["PC3"]," #\n","#     #     #     #\n","###################")

        coup_joueur2 = int(input("(Joueur 2) Quel case voulez-vous jouer ? "))
        coup_joueur2_defini = coupcase(coup_joueur2)



        if coup_joueur2_defini in liste_coup_disponible:
            liste_coup_joueur2.append(coup_joueur2_defini)
            liste_coup_disponible.remove(coup_joueur2_defini)
            affichageXouO(coup_joueur2_defini)
            break

        else:
            print("Réessayez")

    print(liste_coup_joueur1)
    print(liste_coup_joueur2)
    if victoire_joueur2(liste_coup_joueur2):
        print("Félicitations Joueur 2, vous avez gagné")
        break

print("Fin de partie, merci d'avoir joué")