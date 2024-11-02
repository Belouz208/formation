import random

def demander_nombre(nbr_min,nbr_max):
    # quel est le nombre magic (entre 1 et 10)
    nbr_int = 0
    while nbr_int == 0 :
        nbr_str = input(f"Quelle est le nombre magic entre {nbr_min} et {nbr_max} ?")
        try:
            nbr_int = int(nbr_str)
        except:
            print ("ERR : Veuillez entree un nombre Valid..")
        else:
            if nbr_int < nbr_min or nbr_int > nbr_max:
                print (f"ERR le nombre doit etre entre {nbr_min} et {nbr_max}")
                nbr_int = 0

    return nbr_int

#LE NOMBRE MAGIC EST PLUS PETIT
#LE NOMBRE MAGIC EST PLUS GRAND
#BRAVO VOUS AVEZ GAGNÉ


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIC = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NBR_VIES = 4



# nombre = 0
# vies = NBR_VIES
# print (NOMBRE_MAGIC)
# while not nombre == NOMBRE_MAGIC and vies> 0:
#     print(f"Il vous Reste {vies} vie(s)")
#     nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
#     if nombre == NOMBRE_MAGIC:
#         print("BRAVO VOUS AVEZ GAGNÉ")
#     elif nombre > NOMBRE_MAGIC:
#         print("LE NOMBRE MAGICI EST PLUS PETIT")
#         vies -= 1
#     else:
#         print("LE NOMBRE MAGIC EST PLUS GRAND")
#         vies -= 1
# if vies == 0:
#     print (f"Vous avez perdu le nombre magic etait {NBR_MAGIC}")
vies = 4
Victoire=False
print (NOMBRE_MAGIC)
for i in range (1,vies+1):
    print(f"Il vous Reste {vies} vie(s)")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIC:
        print("Bravo")
        Victoire=True
        break
    elif nombre > NOMBRE_MAGIC:
        print("LE NOMBRE MAGICI EST PLUS PETIT")
        vies -= 1
    else:
        print("LE NOMBRE MAGIC EST PLUS GRAND")
        vies -= 1
if  Victoire == False:
     print (f"Vous avez perdu le nombre magic etait {NOMBRE_MAGIC}")









