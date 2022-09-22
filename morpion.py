from os import remove

#Fonction qui vérifie si le joueur 1 a gagné
def victoire_joueur1():

    if "A1" and "A2" and "A3" in liste_coup_joueur1:      #A1 & A2 & A3
        return True

    elif "B1" and "B2" and "B3" in liste_coup_joueur1:    #B1 & B2 & B3
        return True

    elif "C1" and "C2" and "C3" in liste_coup_joueur1:    #C1 & C2 & C3
        return True
        
    elif "A1" and "B1" and "C1" in liste_coup_joueur1:    #A1 & B1 & C1
        return True

    elif "A2" and "B2" and "C2" in liste_coup_joueur1:    #A2 & B2 & C2
        return True

    elif "A3" and "B3" and "C3" in liste_coup_joueur1:    #A3 & B3 & C3
        return True

    elif "A1" and "B2" and "C3" in liste_coup_joueur1:    #A1 & B2 & C3
        return True

    elif "A3" and "B2" and "C1" in liste_coup_joueur1:    #A3 & B2 & C1
        return True
    else:
        return False


#Fonction qui vérifie si le joueur 2 a gagné
def victoire_joueur2():

    if "A1" and "A2" and "A3" in liste_coup_joueur2:      #A1 & A2 & A3
        return True

    elif "B1" and "B2" and "B3" in liste_coup_joueur2:    #B1 & B2 & B3
        return True

    elif "C1" and "C2" and "C3" in liste_coup_joueur2:    #C1 & C2 & C3
        return True
        
    elif "A1" and "B1" and "C1" in liste_coup_joueur2:    #A1 & B1 & C1
        return True

    elif "A2" and "B2" and "C2" in liste_coup_joueur2:    #A2 & B2 & C2
        return True

    elif "A3" and "B3" and "C3" in liste_coup_joueur2:    #A3 & B3 & C3
        return True

    elif "A1" and "B2" and "C3" in liste_coup_joueur2:    #A1 & B2 & C3
        return True

    elif "A3" and "B2" and "C1" in liste_coup_joueur2:    #A3 & B2 & C1
        return True
    else:
        return False

case = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]

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
    coup_joueur = dicotouche[coup_joueur]
    return coup_joueur




liste_coup_disponible = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
liste_coup_joueur1 = []
liste_coup_joueur2 = []

PA1="1"
PB1="2"
PC1="3"
PA2="4"
PB2="5"
PC2="6"
PA3="7"
PB3="8"
PC3="9"

def affichageXouO(cellule) :
    if cellule in liste_coup_joueur1:
        cellule="X"
    if cellule in liste_coup_joueur2:
        cellule="O"
        

while True:

    while True:

        print(" ###################\n","#     #     #     #\n","# ",PA1," # ",PB1," # ",PC1," #\n","#     #     #     #\n","###################\n","#     #     #     #\n","# ",PA2," # ",PB2," # ",PC2," #\n","#     #     #     #\n","###################\n","#     #     #     #\n","# ",PA3," # ",PB3," # ",PC3," #\n","#     #     #     #\n","###################")

        coup_joueur1 = int(input("(Joueur 1) Quel case voulez jouer ?"))



        if coup_joueur1 in liste_coup_disponible:
            liste_coup_joueur1.append(coup_joueur1)
            liste_coup_disponible.remove(coup_joueur1)
            break

        else:
            print("Dommage")
            
    
    while True:

        print(" ###################\n","#     #     #     #\n","# ",PA1," # ",PB1," # ",PC1," #\n","#     #     #     #\n","###################\n","#     #     #     #\n","# ",PA2," # ",PB2," # ",PC2," #\n","#     #     #     #\n","###################\n","#     #     #     #\n","# ",PA3," # ",PB3," # ",PC3," #\n","#     #     #     #\n","###################")

        coup_joueur2 = int(input("(Joueur 1) Quel case voulez jouer ?"))


        if coup_joueur2 in liste_coup_disponible:
            liste_coup_joueur2.append(coup_joueur2)
            liste_coup_disponible.remove(coup_joueur2)
            break

        else:
            print("Dommage")