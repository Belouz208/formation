

def recup_info_personne(numero_personne):
    nom = input(f"Quelle est le nom de la personne numero {numero_personne} :")
    age = input(f"Quelle est l'age de la personne numero {numero_personne} :")
    return nom,age

def afficher_info_personne (numero_personne,nom,age):
    print (f"la personne numero {numero_personne} s'appel {nom} son age est {age} ans" )
    print (f"le nom possed {len(nom)} caracters..")

def recupere_et_afficher_infos_personne(numero_personne):
    nom,age=    recup_info_personne(numero_personne)
    afficher_info_personne(numero_personne,nom,age)

nbr_de_personne = 2

for i in range (nbr_de_personne):
    recupere_et_afficher_infos_personne(i+1)
    










"""


def afficher_infos_personne (nom,age=0):
    print()
    if nom =="":
        print("vous navez pas entree de nom")
    else:
        if age == 0:
            print(f"La personne est {nom} ")
        else:
            print(f"La personne est {nom} , son age est {age} ans")
    print(f"le nom comport {len(nom)} caracter")


print ("Debut de programme")

afficher_infos_personne("toto halim")

print("Fin de programme")

"""