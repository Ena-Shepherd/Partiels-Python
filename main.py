"""

 Author: Yannis STEFANELLI

 Creation Date: 07-03-2023 08:47:30

 Description :

"""
from exo1 import exercice1
from exo2 import exercice2
from exo3 import exercice3

def menu() -> int:
    while (1):
        choice = int(input("Entrer numéro exercice (1-3), sinon quitter\n"))
        match choice:
            case 1:
                exercice1()
            case 2:
                exercice2()
            case 3:
                exercice3()
            case _:
                exit()

menu()
