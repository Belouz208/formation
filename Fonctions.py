


def poser_question (question,r1,r2,r3,r4,bonne_reponse):
    print(f"Quelle est la capitale de {question} :")
    print(f"(a)- {r1}")
    print(f"(b)- {r2}")
    print(f"(c)- {r3}")
    print(f"(d)- {r4}")
    reponse = input ("votre reponse : ")
    if reponse == bonne_reponse :
        print("Bonne Reponse")
    else:
        print("Mauvaise Réponse")


poser_question("algerie","alger","oran","batna","setif","a")





# def quelle_est_la_capital_algerie():
#     capital ="alger"
#     print ("quelle est la capital de l'algerie ?")
#
#     if choix == capital:
#         print("Bonne Reponse")
#     else:
#         print("mauvaise Reponse")
#
#
# quelle_est_la_capital_algerie()
#
#
#
#
#





#
#
# def afficher_table_multiplication (n,min=1,max=10):
#     if min > max :
#         print ("ERROR le minimum est superier au maximum")
#         return
#     # val_initial = 1 * n
#     # min =val_initial
#     # max =0
#     resultat = 0
#
#
#     for i in range (min,max):
#         resultat = i * n
#         if resultat < min:
#             min = resultat
#         elif resultat > max :
#             max = resultat
#
#
#         print (f"{i} * {n} = {resultat}")
#
#     print (f"la valeur minimum est {min} et la valeur maximum est {max}")
#
#
# afficher_table_multiplication(4,100,30)
#
#
#
# """
#     def recup_info_personne(numero_personne):
#     nom = input(f"Quelle est le nom de la personne numero {numero_personne} :")
#     age = input(f"Quelle est l'age de la personne numero {numero_personne} :")
#     return nom,int(age)
#
# def afficher_info_personne (numero_personne,nom,age):
#     print (f"la personne numero {numero_personne} s'appel {nom} son age est {age} ans" )
#     print (f"le nom possed {len(nom)} caracters..")
#     if est_majeur(age):
#         print(f"{nom} est majeur ")
#     else:
#         print(f"{nom} est mineur ")
#
#
# def recupere_et_afficher_infos_personne(numero_personne):
#     nom,age=    recup_info_personne(numero_personne)
#     afficher_info_personne(numero_personne,nom,age)
#
# def est_majeur(age):
#     if age <= 18:
#         return False
#     return True
#
#
# nbr_de_personne = 2
#
# for i in range (nbr_de_personne):
#     recupere_et_afficher_infos_personne(i+1)
#
# afficher_info_personne("007","Hamidi",40)
#
#
#
#
#
#
#
#
#
#
#
#
#
# def afficher_infos_personne (nom,age=0):
#     print()
#     if nom =="":
#         print("vous navez pas entree de nom")
#     else:
#         if age == 0:
#             print(f"La personne est {nom} ")
#         else:
#             print(f"La personne est {nom} , son age est {age} ans")
#     print(f"le nom comport {len(nom)} caracter")
#
#
# print ("Debut de programme")
#
# afficher_infos_personne("toto halim")
#
# print("Fin de programme")
#
# """