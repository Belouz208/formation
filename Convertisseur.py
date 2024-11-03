

# print (choix_client)
bon_choix = False
fin_program = False

while not bon_choix or not fin_program:

    print("1 - Cm ----> Pouce")
    print("2 - Pouce-------Cm")
    print()
    choix_client = input("Faite votre Choix 1 Ou 2 Ou 3 : ")

    if choix_client == "1":
        print()
        val_cm = input("Veuillez Donner la valeur en Cm : ")
        val_cm = float (val_cm)
        resultat_conv = round(0.394 * val_cm,2)
        print(f"La valeur resultat_conversation de {val_cm} Cm est egal a {resultat_conv} Pouce")
        bon_choix = True

    elif choix_client == "2":
        print()
        val_pouce = input("Veuillez Donner la valeur en Pouce : ")
        val_pouce = float(val_pouce)
        resultat_conv = round(2.54 * val_pouce,2)
        print(f"La valeur resultat_conversation de {val_pouce} Pouce est egal a {resultat_conv} Cm")
        bon_choix = True

    elif choix_client == "3":
        print()
        print ("Programme Terminé !!!")
        fin_program = True
        bon_choix = True
    else:

        print("Veuillez Entree un choix valid :")
        bon_choix = False










