import time


def menu_c ():
    validite_rep = False
    print()
    print("a) Ouefs à la coque (3 min)")
    print("b) Ouefs mollets (6 min)")
    print("c) Ouefs dur (9 min)")
    print("q) Quitter le programme")
    choix = input("Votre Choix :")
    return choix

def coque ():

    d = 180
    min= d// 60
    sec = d-min*60


    print("...")

    while d > 0:
        print (f"temp restant {min:02d} : {sec:02d}, {d}")
        for i in range (3):
            time.sleep(1)
            print (".",end="",flush=True)

    d = d - 10


def mollets ():
    pass

def dur():
    pass

def quitter():
    pass


def traitement_choix_user(choix):

    if choix == "a":
        coque()
    elif choix == "b":
        mollets()
    elif choix == "c":
        dur()
    elif choix == "q":
        quitter()


#main
choix = menu_c()
traitement_choix_user(choix)
