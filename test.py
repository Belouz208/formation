#from Convertisseur import fin_program

def cm_to_pouce (x):
    val_cm = input("Veuillez Donner la valeur en Cm : ")
    val_cm = float(val_cm)
    resultat_conv = 0, 394 * val_cm
    return resultat_conv


def affiche_menu():
    print ("1 - Cm ----> Pouce")
    print ("2 - Pouce-------Cm")
    choix_client = input ("3-Pour Quitter " )
    return choix_client

def opertaion (choix :str):
    if choix == "1":
        print ("1")
    elif choix == "2":
        print("2")
    elif choix == ("3") :
        print("3")

choix_client = affiche_menu()
opertaion(choix_client)












