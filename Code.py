def Menu():
    print("Welcome to the vocabulary quiz program. Select one of the following lists:")
    print("verbs.txt")
    f = input("Please make your selection: ")
    with open(f, 'r') as file:
        L = []
        for line in file:
            rec = line.split()
            L.append(rec)
    
    num_of_ques = input(f"{len(L)} entries found. How many words you like to be quizzed on?")
    

Menu()