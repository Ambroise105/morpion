liste_coup_joueur1 = ["A1", "A2", "B1"]

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