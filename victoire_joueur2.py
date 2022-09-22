def victoire_joueur2(test):

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