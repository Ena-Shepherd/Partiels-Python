"""

 Author: Yannis STEFANELLI

 Creation Date: 07-03-2023 08:49:15

 Description :

"""

def seuil(p, t):
    n = 0
    while p < 1000:
        print(f"P = {p:.2f} | N = {n}")
        p = p * t
        n += 1
    return n - 1



def exercice1():
    p = float(input("Entrez P\n"))
    t = float(input("Entrez T\n"))
    print(seuil(p, t))