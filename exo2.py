"""

 Author: Yannis STEFANELLI

 Creation Date: 07-03-2023 09:27:14

 Description :

"""

def suite(A, B, N):
    Un_1 = A
    Un = B
    print(f"U0 = {A:.3f}")
    print(f"U1 = {B:.3f}")
    for i in range(2, N+1):
        Un_1, Un = Un, 2/(1/Un_1 + 1/Un)
        print(f"U{i-1} = {Un_1:.3f}")
        print(f"U{i} = {Un:.3f}")
    return Un


def exercice2():
    a = int(input("Entrez A\n"))
    b = int(input("Entrez B\n"))
    n = int(input("Entrez N\n"))

    suite(a, b, n)