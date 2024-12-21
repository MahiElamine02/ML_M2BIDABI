# Créer une fonction à partir de la cellule d'en haut
def sets_creation(df,first_threshold, ratio):
    
    # Simple
    training_set = df[:first_threshold]
    test_set = df[first_threshold:]
    
    # Dynamical
    training_set_treshold = int(len(df)*ratio)
    training_set = df[:training_set_treshold]
    test_set = df[training_set_treshold:]

    # Separer le y (variable a predire) des X (variables explicatives)
    X = test_set.drop(columns=['median_house_value'])
    Y = test_set['median_house_value']

    print("training_set size", len(training_set))
    print("test_set size", len(test_set))

    return X, Y
    