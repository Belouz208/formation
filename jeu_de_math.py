

import  random

from scipy.stats import false_discovery_control

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_DE_QUESTION = 4


def poser_question ():

        a = random.randint(NOMBRE_MIN,NOMBRE_MAX)
        b = random.randint(NOMBRE_MAX,NOMBRE_MAX)
        o = random.randint(0,1)
        if o == 1:
            operation ="*"
            reponse_str = input(f"calculer {a} {operation} {b} = ")
            reponse_int = int(reponse_str)
            calcule = a * b
            if calcule == reponse_int:
                return True
            else:
                return False
        elif o == 0:
            operation = "+"
            reponse_str = input(f"calculer {a} {operation} {b} = ")
            reponse_int = int(reponse_str)
            calcule = a + b
            if calcule == reponse_int:
                return True
            else:
                return False





nbr_point = 0

for i in range (0,NOMBRE_DE_QUESTION):
    print()
    print(f"Question N° {i+1} sur {NOMBRE_DE_QUESTION}")
    if poser_question() == True:
        nbr_point += 1
        print("Well donne")
    else:
        print("Bad Answer")
print()

moyenne = int(NOMBRE_DE_QUESTION/2)

if nbr_point == NOMBRE_DE_QUESTION:
    print("Excellent Job")
elif nbr_point == 0:
    print("روح تقرا")
elif nbr_point >= moyenne:
    print ("Pas mal")
else :
    print('Peut Mieux Faire')


print(f"Votre Score Est de : {nbr_point} / {NOMBRE_DE_QUESTION}")









