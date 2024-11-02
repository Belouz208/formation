

import  random

NOMBRE_MIN = 1
NOMBRE_MAX = 10


def poser_question ():
    a = random.randint(NOMBRE_MIN,NOMBRE_MAX)
    b = random.randint(NOMBRE_MAX,NOMBRE_MAX)
    reponse_str = input (f"Calculer {a} + {b}= ")
    reponse_int= int (reponse_str)

    if reponse_int == a+b :
        print ("Good Job")
    else :
        print ("Bad Answer")


poser_question()

