import os

# # print (choix_client)
# bon_choix = False
# fin_program = False
#
# while not bon_choix or not fin_program:
#
#     # print("1 - Cm ----> Pouce")
#     # print("2 - Pouce-------Cm")
#     # choix_client = input(" Faite votre Choix 1 Ou 2 Ou 3 : ")
#
#     if choix_client == "1":
#         val_cm = input("Veuillez Donner la valeur en Cm : ")
#         val_cm = float (val_cm)
#         resultat_conv = 0, 394 * val_cm
#         print(resultat_conv)
#         bon_choix = True
#
#     elif choix_client == "2":
#         val_pouce = input("Veuillez Donner la valeur en Pouce : ")
#         val_pouce = float(val_pouce)
#         resultat_conv = 2.54 * val_pouce
#         print(resultat_conv)
#         bon_choix = True
#
#     elif choix_client == "3":
#         print ("Programme Terminé !!!")
#         fin_program = True
#         bon_choix = True
#     else:
#         print("Veuillez Entree un choix valid :")
#         bon_choix = False
#
#
#
#

def affiche_menu():
    print ("1 - Cm ----> Pouce")
    print ("2 - Pouce-------Cm")
    print ("3 - Pour  Quitter" )
    choix_operation = input ("Faite Votre Choix : ")
    return choix_operation

def cm_to_pouce ():
    validite_val = False
    while not validite_val:
        try :
            val_cm = input("Veuillez Donner la valeur en Cm : ")
            val_cm = float(val_cm)
            resultat_conv = round((0.394 * val_cm),2)
            print (f"la valeur {val_cm} Cm converti est de {resultat_conv} Pouce ")
            validite_val = True
        except :
            print ("ERROR entree une valure valable EN CM")

def pouce_to_cm ():
    validite_val = False
    while not validite_val:
        try:
            val_pouce = input("Veuillez Donner la valeur en pouce : ")
            val_pouce = float(val_pouce)
            resultat_conv = round((0.394 * val_pouce),2)
            print(resultat_conv)
            validite_val =True
        except:
            print ("entree une valure EN Pouce :")

def opertaion (choix):

            if choix == "1":
                cm_to_pouce()
            elif choix == "2":
                pouce_to_cm()
            elif choix == "3" :
                print ("program terminée ..!!")
                return True
            else:
                print("Entree une valeur Valid")
                return  False

#main

termin_prog = False
while not termin_prog :
    print()
    choix_client = affiche_menu()
    termin_prog = opertaion(choix_client)






