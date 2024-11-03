

# print (choix_client)
bon_choix = False
fin_program = False

while not bon_choix or not fin_program:

    print("1 - Cm ----> Pouce")
    print("2 - Pouce-------Cm")
    choix_client = input(" Faite votre Choix 1 Ou 2 Ou 3 : ")

    if choix_client == "1":
        val_cm = input("Veuillez Donner la valeur en Cm : ")
        val_cm = float (val_cm)
        resultat_conv = 0, 394 * val_cm
        print(resultat_conv)
        bon_choix = True

    elif choix_client == "2":
        val_pouce = input("Veuillez Donner la valeur en Pouce : ")
        val_pouce = float(val_pouce)
        resultat_conv = 2.54 * val_pouce
        print(resultat_conv)
        bon_choix = True

    elif choix_client == "3":
        print ("Programme Terminé !!!")
        fin_program = True
        bon_choix = True
    else:
        print("Veuillez Entree un choix valid :")
        bon_choix = False










